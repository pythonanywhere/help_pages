<!--
.. title: Securing your PythonAnywhere account
.. slug: SecuringYourAccount
.. date: 2017-03-31
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

###What we do

We do all we can to keep your PythonAnywhere account secure, along with the
files and data you have stored in it -- from fully-patched operating systems
and a [bug bounty program](https://help.pythonanywhere.com/pages/BugBounty) to
encourage security researchers to tell us about any issues before they become
problems, to strict internal policies determining when our support staff are
allowed to look at your stuff (basically, never without your permission unless
your code is causing major systemwide problems).

###What you can do

To make your account completely secure, there are things you can do too.

* Don't share consoles with people you don't know.  Even if you share it
  read-only, they can see what you're typing in there.  And if it's not read-only
  they can look at all of your files if you leave it shared with them and don't
  keep an eye on what they're up to.
* Don't make anyone your "Teacher" if they're not someone you trust implicitly --
  a teacher can access PythonAnywhere just as if they're their student, so you're
  giving them access to everything in your account (apart from your billing details).
* Be careful with your static files setup.  Any file within a directory specified
  in the static files table on the "Web" tab is potentially accessible to anyone
  in the world if they can guess its path.
* If you're sharing code with anyone (including on our forums), make sure that
  you don't post anything with passwords in it.  (Replace passwords with something
  like "xxxxxxx" if that part of the code is essential to the post.)
* Make sure you use a highly secure password for your PythonAnywhere login.
  We're big fans of using memorable but unguessable passwords of the kind
  [dreamed up by Randall Munroe of XKCD](https://xkcd.com/936/).  There's even
  [a Python package to generate them](https://pypi.python.org/pypi/xkcdpass/).
  A good alternative is to use completely-random passwords of at least 16
  characters and to store them in a password manager like
  [Keepass](http://keepass.info/).
* Make sure that any secondary passwords associated with your account --
  especially any that might appear in your code, like your MySQL and Postgres
  passwords -- are completely different to your main login password.
* It should go without saying these days, but look out for phishing.  We won't
  send you any emails asking for your password, and we will only ask for your
  password to be entered on `www.pythonanywhere.com`.  Check the address bar
  in your browser before typing in your password!
* Don't leave a computer that's logged in to PythonAnywhere unattended in a
  public area.
* Consider setting up two-factor authentication.

###Two-factor authentication

If you want the best possible security for your account, we recommend
you enable two-factor authentication (TFA).  This is a system that uses an app on your
phone to generate a number, once a minute.  When you log in to PythonAnywhere,
you have to enter that number as well as your username and password.  In other
words, someone who wants to break into your account not only needs to steal your
password, they also need to get hold of your phone.

One important warning about TFA: when you set it up, it
gives you some "emergency" codes, which you can use instead of the ones your
phone generates.   It's *super*-important that you keep these safe.  Once you've
set up TFA, you will not be able to access your account without a code, and our
support staff won't be able to help you override that.  So if you lose your
phone and didn't keep your emergency codes safe, then you're locked out forever.

