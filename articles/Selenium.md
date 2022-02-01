
<!--
.. title: Using Selenium on PythonAnywhere
.. slug: selenium
.. date: 2017-01-28 13:35:28 UTC
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

*** NOTE *** These instructions are for the system image **fishnchips** or later.
If you have an older system image, you will need to [update your system
image](https://help.pythonanywhere.com/pages/ChangingSystemImage/) to use these
instructions. Also note that selenium will only work in tasks, web apps and
consoles. It will not work in notebooks and over SSH.

*If you're on the fishnchips system image*, you will need to update
selenium for your account/virtualenv to 3.141.0. For example, if you're using
Python 3.7, run this in a Bash console:

    pip3.7 install --user selenium==3.141.0

Note that selenium>=4.0.0 won't work on PythonAnywhere right now.

You can run Selenium with Chrome using code like this:

```python
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox”)
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)
try:
    browser.get("https://www.google.com")
    print("Page title was '{}'".format(browser.title))
finally:
    browser.quit()
```


## Cleaning up manually

If you fail to clean up properly in your code, you may find that you cannot
start new Chrome processes (you will get error messages saying Chrome crashed).
In that case, you can use the "process listing" buttons on the Consoles page
and the Tasks page to manually find and kill any leftover Chrome processes.


## Paid account may be required

Free users are currently restricted to a
[whitelist](https://www.pythonanywhere.com/whitelist/)
of sites.  If you want to use Selenium to talk to a site
that's not on the list, you'll need to upgrade to a paid
account.


## Don't use selenium from your web app

Selenium and Firefox are too slow to start up, and the request/response
cycle is meant to be fast.  Instead, build some sort of queue of jobs,
and use a scheduled task to process those jobs.  More info [here](/pages/AsyncInWebApps/)


