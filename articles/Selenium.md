
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

*** NOTE *** These instructions are for the system image **fishnchips, glastonbury or haggis**.
If you have an older system image, you will need to [update your system
image](https://help.pythonanywhere.com/pages/ChangingSystemImage/) to use these
instructions. Also note that selenium will only work in tasks, web apps and
consoles. It will also work in notebooks, but only on **haggis**. It will not work over SSH.

The latest versions of selenium confirmed to be working are:

| System Image | Version | Confirmed  |
|--------------|---------|------------|
| fishnchips   | 4.1.3   | 2022-09-06 |
| glastonbury  | 4.4.3   | 2022-09-06 |
| haggis       | 4.7.2   | 2022-12-23 |

<br />

We recommend upgrading selenium for your account/virtualenv to this version.
For example, if you're using Python 3.7, run this in a Bash console:


```bash
    pip3.7 install --user selenium==4.1.3
```


You can run Selenium with Chrome using code like this:

```python
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
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
[allowlist](https://www.pythonanywhere.com/whitelist/)
of sites.  If you want to use Selenium to talk to a site
that's not on the list, you'll need to upgrade to a paid
account.


## Don't use selenium from your web app

Selenium with a browser are too slow to start up, and the request/response
cycle is meant to be fast.  Instead, build some sort of queue of jobs,
and use a scheduled task to process those jobs.  More info [here](/pages/AsyncInWebApps/)


## Page crash errors
Sometimes your code may fail with an error like this:

```
Message: unknown error: session deleted because of page crash
```

If you get this, try adding the option

```python
chrome_options.add_argument('--disable-dev-shm-usage')
```
