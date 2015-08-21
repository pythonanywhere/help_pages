
<!--
.. title: Javascript
.. slug: Javascript
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




To set up a Jasmine tested JS project, you would do something like the following: 

       1 git clone git@github.com:jasmine/jasmine.git temp-jasmine-git-folder
       2 mkdir -p jasmine-tested-project/jasmine
       3 unzip jasmine/dist/jasmine-standalone-2.2.0.zip -d jasmine-tested-project/jasmine
       4 rm -r temp-jasmine-git-folder



and then you would set up a test runner html file such as `jasmine-tested-project/SpecRunner.html` that would take code files such as `jasmine-tested-project/code-to-be-tested.js` as well as test files such as `jasmine-tested-project/code-to-be-testedSpec.js`. 

       1 <html>
       2   <head>
       3     <title>Jasmine Spec Runner v2.0.2</title>
       4     <link rel="shortcut icon" type="image/png" href="jasmine/lib/jasmine-2.2.0/jasmine_favicon.png">
       5     <link rel="stylesheet" type="text/css" href="jasmine/lib/jasmine-2.2.0/jasmine.css">
       6 
       7     <script type="text/javascript" src="jasmine/lib/jasmine-2.0.0/jasmine.js"></script>
       8     <script type="text/javascript" src="jasmine/lib/jasmine-2.0.0/jasmine-html.js"></script>
       9     <script type="text/javascript" src="jasmine/lib/jasmine-2.0.0/boot.js"></script>
      10 
      11     <!-- the js source files being tested -->
      12     <script type="text/javascript" src="code-to-be-tested.js"></script>
      13     <!-- the test files -->
      14     <script type="text/javascript" src="code-to-be-testedSpec.js"></script>
      15   </head>
      16   <body>
      17   </body>
      18 </html>



If you then host the whole jasmine-tested-project dir via static files, this could create interesting pair programming/teaching scenarios. 

For example, if you share your console with a class of students, and edit/change your tests and js code there, then your students can navigate to the test runner page and see the test results change from red to green in real time as you save your files. Alternatively, your students could be working on their own versions of the code, and serving the test runner on their respective PythonAnywhere websites. Then you would be able to look at their progress and then help them if they are having any problems. 
