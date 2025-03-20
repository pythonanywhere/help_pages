<!--
.. title: Using Playwright on PythonAnywhere
.. slug: Playwright
.. date: 2024-05-22 18:30:00 UTC
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

> **PLEASE NOTE:** Playwright will only work in scheduled/always-on tasks, web apps and
> consoles. It will also work in notebooks, except on the legacy "glastonbury"
> [system image](/pages/ChangingSystemImage). It currently will **not work** over SSH.

If you have a paid account on PythonAnywhere, you can use Playwright to access
other sites using a headless browser -- for example, for scraping.  Installing
it is a little different to how you might do so locally.

You'll need to install it into a [virtualenv](/pages/VirtualenvsExplained), because it's not compatible with
some of our pre-installed packages.  So, for example:

```bash
mkvirtualenv my-playwright-env --python=python3.10
pip install playwright
```

It will take up about 130MiB disk when installed (perhaps using a bit more than
that during the install due to its temporary files).

The next step would normally to install the browsers using `playwright install`.
However, that won't work on PythonAnywhere -- but we do already have Chromium
installed, so you can use that by adding some extra config to your code.  Here's
a minimal example:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path="/usr/bin/chromium",
        args=["--disable-gpu", "--no-sandbox", "--headless"]
    )
    page = browser.new_page()
    page.goto("http://playwright.dev")
    print(page.title())
    browser.close()
```

Many thanks to **hcaptcha** [in our forums](https://www.pythonanywhere.com/forums/topic/30302/)
for working out what the the trick was to make it work!
