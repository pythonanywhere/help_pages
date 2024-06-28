<!--
.. title: Running Django code in consoles, scheduled and always-on tasks with custom management commands
.. slug: DjangoManagementCommands
.. date: 2024-06-28 15:00:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Django is a really useful and powerful web framework; indeed, the web interface
and API for PythonAnywhere itself are all Django-based.

One thing that makes it
particularly useful is its powerful ORM system, where you can work with the data that
your website needs just by using normal Python classes and objects.  If you want
to set the field to say that the user with username `joe` is active, you can just
write this:

```python
from django.contrib.auth.models import User

# ...

user = User.objects.get(username="joe")
user.is_active = True
user.save()
```

All of the complexities of connecting to the database -- including finding the
connections details in your `settings.py` file -- and generating appropriate SQL
code are hidden from you.

The downside is that this code will only work in the context of a Django site --
that is, if you don't do some extra work, it has to be inside a function that forms part of your website's code.  If
you were to run a script that used that code directly from a console, it would
error out:

```
Traceback (most recent call last):
  File "/home/gt20240628u1/deactivate.py", line 1, in <module>
    from django.contrib.auth.models import User
  File "/usr/local/lib/python3.10/site-packages/django/contrib/auth/models.py", line 3, in <module>
    from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
  File "/usr/local/lib/python3.10/site-packages/django/contrib/auth/base_user.py", line 49, in <module>
    class AbstractBaseUser(models.Model):
  File "/usr/local/lib/python3.10/site-packages/django/db/models/base.py", line 127, in __new__
    app_config = apps.get_containing_app_config(module)
  File "/usr/local/lib/python3.10/site-packages/django/apps/registry.py", line 260, in get_containing_app_config
    self.check_apps_ready()
  File "/usr/local/lib/python3.10/site-packages/django/apps/registry.py", line 137, in check_apps_ready
    settings.INSTALLED_APPS
  File "/usr/local/lib/python3.10/site-packages/django/conf/__init__.py", line 87, in __getattr__
    self._setup(name)
  File "/usr/local/lib/python3.10/site-packages/django/conf/__init__.py", line 67, in _setup
    raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment
 variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
```

This is because all of the setup -- reading the settings, connecting to the database,
and so on -- is handled when a Django website is started, so your view functions
run in that context, but throwaway scripts need something to do all of that setup
for them.

From the error message, you can see that there is a way to write some extra code
to do it.  But we'd recommend a different way: [custom `django-admin`
commands](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/),
also known as custom management commands.  The Django documentation page we
linked to just there is a useful resource, but here are some simpler examples.


## Custom management commands for use in consoles and scheduled tasks

Imagine that you were writing a site where people could leave comments, but you
wanted all comments that were more than 24 hours old to be deleted once a day
-- kind of like Snapchat, or the vanishing messages in WhatsApp.  You might
have a `Comment` class like this:

```python
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1024)
```

Now, you could put something complicated into your view functions that hid or
deleted comments that were older than 24 hours, but a nice simple solution would
be to have a [scheduled task](/pages/ScheduledTasks/) that kicked off every day at the same time and ran
code like this:

```python
Comment.objects.filter(timestamp__lt=datetime.now() - timedelta(days=1)).delete()
```

If you were to put that (with the appropriate imports) into a script and run
it, you'd get the `ImproperlyConfigured` exception shown above.  However,
you can get it working with a management command.  Let's say that the code for
your `Comment` class was in `~/mysite/comments/models.py`.  You could create a
new file at `~/mysite/comments/management/commands/delete_old_comments.py`, and
in there you would put code like this:

```python
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from comments.models import Comment


class Command(BaseCommand):
    help = "Deletes comments more than 24 hours old"

    def handle(self, *args, **options):
        Comment.objects.filter(timestamp__lt=datetime.now() - timedelta(days=1)).delete()
```

With that, you could easily run it ad-hoc in a Bash console:

```bash
cd ~/mysite
./manage.py delete_old_comments
```

That would start up Django's normal `manage.py` system, which of course
loads in all of the settings and connects to the database for you, then run the
code in side the `handle` function, doing the work you need.

But you could also call it in a scheduled task.  Let's say that your Django site is *not*
using a virtualenv; you could just schedule this:

```bash
~/mysite/manage.py delete_old_comments
```

If you *were* using a virtualenv -- say, one that you had created using `mkvirtualenv`
and called `myenv` -- you would just need to activate it first:

```bash
workon myenv; ~/mysite/manage.py delete_old_comments
```

You could also make it more complex if you wanted; perhaps you might want to add in
a command-line option to change the number of days old a comment would have to
be before it was deleted.  Check out the [documentation](https://docs.djangoproject.com/en/latest/howto/custom-management-commands/)
for details.


## Custom management commands in always-on tasks

Custom management commands don't have to just be one-shot utility functions like that.
Let's say that you have simple bot that is connected to a messaging service.
It's a script that is started, and is expected to keep running forever. Ideally
you would like it to be re-started if it ever crashes (or if there's a hardware
issue or system maintenance on the machine where it's running, or something like
that).  The right way to set that up on PythonAnywhere would be to use an
[always-on task](/pages/AlwaysOnTasks).  But you want it to have access to the
Django stuff -- the objects that you have stored in your database.

How would you use a custom management command for that?  Let's say that what you
wanted was to receive messages from users of some messaging service like WhatsApp, Signal or Telegram.
Each incoming message would specify
the name of a user, and the bot would respond with a message containing that user's most recent comment on your site.  It's
an always-on task that is connected to the database via Django, and to the
messaging service.

Now, real messaging services have complex APIs that would make this example
unnecessarily complicated, so we'll imagine that we're using a new service with a
simpler one.  It's called WhatsSignaGram, and its API allows us to connect to it
as a particular bot user using a secret:

```python
bot_connection = whatssignagram.Connection(secret="z4vk14=yzfm*35+%c^=&yc*jcp9y$1al1^(^v-%ahk$j0ssz!k")
```

...then we can get the next message that was sent to our bot with a function that
just blocks if there is currently no message, and unblocks when one comes in:

```python
message = bot_connection.next_message()
```

The `message` has a `contents` field, and a `reply` method, so we could simply
echo stuff back by saying

```python
message.reply(f"You just said {message.contents}")
```

Let's use that imaginary API to write a custom management command that
implements the more complex bot that was described earlier, to reply to each message
with the most recent comment left on our site by the user with the username provided
in the message:

```python
import whatssignagram

from django.core.management.base import BaseCommand, CommandError
from comments.models import Comment


class Command(BaseCommand):
    help = "WhatsSignaGram bot to provide the most recent comment for a user"

    def handle(self, *args, **options):
        bot_connection = whatssignagram.Connection(secret="z4vk14=yzfm*35+%c^=&yc*jcp9y$1al1^(^v-%ahk$j0ssz!k")

        while True:
            message = bot_connection.next_message()

            username = message.contents
            comments = Comment.objects.filter(user__username=username).order_by("timestamp")
            if comments.count() == 0:
                message.reply(f"No comments found for user {username}")
            else:
                message.reply(f"Last comment for {username} was {comments.last().text}")
```

You would save that in (say) `~/mysite/comments/management/commands/comment_bot.py`
and it could be run with `manage.py` by providing the first parameter `comment_bot`.
So, just as with scheduled tasks, if you were *not* using a virtualenv; you could
just specify this as the command for your always-on task:

```bash
~/mysite/manage.py comment_bot
```

...and if you *were* using a virtualenv called `myenv`, you would just need to activate it first:

```bash
workon myenv; ~/mysite/manage.py comment_bot
```
So there you have it!  A custom management command that can connect to the
fictional WhatsSignaGram library and interact with its users and the Django-managed database, returning the
most recent comment for a user when asked, running as an always-on task.

Of course, in a real-world example your code for the bot would be likely to be
more complicated.  But there's no problem with splitting things out into multiple
functions, or indeed across multiple files.  For example, the above code could
just as easily be this:

```python
import whatssignagram

from django.core.management.base import BaseCommand, CommandError
from comments.models import Comment


def do_bot_loop():
    bot_connection = whatssignagram.Connection(secret="z4vk14=yzfm*35+%c^=&yc*jcp9y$1al1^(^v-%ahk$j0ssz!k")

    while True:
        message = bot_connection.next_message()

        username = message.contents
        comments = Comment.objects.filter(user__username=username).order_by("timestamp")
        if comments.count() == 0:
            message.reply(f"No comments found for user {username}")
        else:
            message.reply(f"Last comment for {username} was {comments.last().text}")


class Command(BaseCommand):
    help = "Comment WhatsSignaGram bot"

    def handle(self, *args, **options):
        do_bot_loop()
```

...and `do_bot_loop` could easily be split into different functions as the complexity
of the bot grew over time, and even moved to a separate module.


## Conclusion

Django's custom management commands are an easy way to be able to connect to your
Django site's functions and data from scripts that aren't running as part of the
website itself -- from one-shot helper scripts that perform a task and then exit,
to longer-running scripts that provide ongoing services.  We strongly recommend
that you use them for any Django code that you have that you would like to run
in consoles, scheduled tasks, or always-on tasks.





















