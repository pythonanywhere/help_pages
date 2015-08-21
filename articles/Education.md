
<!--
.. title: PythonAnywhere Education beta
.. slug: Education
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




##What's in it for me?


  * **Zero setup means you can start teaching straight away**. Avoid all the hassles of getting Python installed on everyone's laptop, and making sure everyone can pip install all the right packages. 
  * **All your students have the same environment**: the same operating system, the same console, the same text editor -- save yourself from having to customise your lessons and instructions for windows/mac/linux, and from having to debug issues in different shells and editors. 
  * **Distributing assignments and monitoring progress is easy**. We give you full access to your students' files and folders, so you can ensure that the student has all your exercises and files, ready in their home area when they log in. 
  * **Helping your students, and having them collaborate, is easy**. You can view your students' consoles at any time and help them debug, and students can use shared consoles to work together. 
  * **Start work at work or at school, and continue at home**. Because PythonAnywhere is web-based, it can follow you around on any PC with a browser, so you or your students can work from wherever you like. 


##What does it cost?


It's free! Our basic accounts are free, and we only charge for more advanced services (like professional web app hosting, or big number-crunching requirements), none of which are needed for basic "intro to programming" type courses. We're happy to have more people on board; we just hope that every so often one of your students might graduate into becoming a professional software developer, and then maybe they'll decide they want to pay for an account to use for work or on a personal project. 


##How do I get started?


The first thing to do is to get familiar with your normal account and how plain-old PythonAnywhere works. We've had lots of teachers and students on the site over the years, finding it useful with its current set of features. So if you haven't signed up for an account already, do that now! Start a console, navigate to the Files menu, edit and save a Python file and run it. Your students will be able to do all that. 

In the education beta, we're just seeing if we can add a little icing to the cake to make it even more appealing. 


##Adding students to your account


Users have the ability to nominate their teacher via the [Account page](https://www.pythonanywhere.com/account). So one option is to get your students to sign up for PythonAnywhere accounts one by one, and enter your username into the "teacher" field. This can also be a good way to check out the features of the education beta, by signing up for a second account, and using it as a "fake" student account. 

Alternatively, we can bulk-create accounts for all your students if you like. Just get in touch! [support@pythonanywhere.com](mailto:support@pythonanywhere.com). 


##Viewing your students' stuff


Once you have some students set up, you'll see a new drop-down at the top right of your dashboard. From there you'll be able to click through and view your students' pages. 

![](/students_dropdown.png)

You'll be able to view their Files, Consoles, Database, and Web app config. 

While you're in there, you can type into their consoles, see what they're typing, and also view (and modify) their files. Use your newfound power responsibly! 


##Copying files to and from student accounts


Students' home folders will be mounted into your own account. So just as your home folder lives at /home/yourusername, you'll be able to see /home/yourstudentusername, and access any files in there. 


###A worked example


*Miss Iolanta is preparing for week 3 of her Python class. The assignment consists of a "complete the code" challenge, where Iolanta has prepared a python file with some half-written functions, where the student has to complete the body, something like this, say:*

       1     def add(number1, number2):
       2         # what should this function return?
       3 
       4     def say_hello(name):
       5          # adjust the next step so that, if someone calls the function with "Xerxes", the function prints "Hello, Xerxes"
       6          message = "?"  
       7          print(message)



*She saves this file as complete_the_code.py in her own file space, maybe in a folder called "assignments". Now she wants to put a copy of it into each student's home directory. She opens up a Bash console and does this:*

       1     $ ls /home
       2     iolanta
       3     bertrand
       4     iphigenea
       5     clarence



*Aha! She thinks, I now see my three students in there, as well as my own home folder! Let's copy the assignment across:*

       1     $ mkdir /home/bertrand/week3
       2     $ mkdir /home/iphigenea/week3
       3     $ mkdir /home/clarence/week3
       4     $ cp /home/iolanta/assignments/complete_the_code.py /home/bertrand/week3/complete_the_code.py
       5     $ cp /home/iolanta/assignments/complete_the_code.py /home/iphigenea/week3/complete_the_code.py
       6     $ cp /home/iolanta/assignments/complete_the_code.py /home/clarence/week3/complete_the_code.py



*And now, when any of her students log in to their accounts, they'll see a new folder in the "Files" area called "week3", and they will each get their own copy of "complete_the_code.py" in there.*

*Later on, Iolanta can use the Bash console to actually run each student's python code and see if it works.*

  * Incidentally, there are smarter ways of copying multiple files around in the Bash shell, using wildcards like *, ask us! 


##Some limitations



###No graphics :/


PythonAnywhere is a server-side, no-gui sort of environment, so we currently don't support any sort of graphics (unless you count web apps). So things like turtle and pygame are out. Which is a shame because graphics are so great, particularly for the student's first few experiences with programming. You may want to check out <https://trinket.io> as an alternative for the first few classes. 


###No young children :/


We're waiting on some legal advice re: data protection, so for now, we have to restrict the service to ages 13 and above. 


###Console sharing is dynamic, Editor sessions are not (for now)


  * In consoles, sharing will be dynamic. You can see each keystroke the student enters into their console, and type your own, and they'll see yours, etc 
  * In files, it won't be dynamic. You would have to hit "refresh" every so often to see if a student has made changes and saved them. If you both edit the same file, there's a potential for conflict, but the system will warn you if that happens ("this file has changed on disk!"). We're doing some experiments with a dynamic version... Also- note that if you open files using a terminal-based editor (such as vim/emacs) from within your consoles, then you would be able to share dynamically. 


###No IPython Notebook


Whilst we support the basic IPython console, we don't yet support the "notebook" UI, which is popular, particularly in scientific fields... 


#Contact us, we want to help!


We're determined to make sure that the first few teachers using our platform have a great experience and get some good success stories out of it. So, do get in touch and let us know what you need -- we'll try and go the extra mile, if it means doing manual work in the background to get things working. We're always available via [support@pythonanywhere.com](mailto:support@pythonanywhere.com)
