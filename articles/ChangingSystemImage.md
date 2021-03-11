<!--
.. title: Changing your system image
.. slug: ChangingSystemImage
.. date: 2021-02-18 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

You can change your account's system image from the "Account" page. This will
leave all of your files and data as they are, but will change the operating
system files to provide different versions of Python and different pre-installed
Python modules. This means that you can use the latest and greatest stuff :-)

However, **you may need to change your code to make it work with the new
system image**.

## Changing the system image

Just click on the "pencil" icon next to the name of your current image, and
you'll get a dropdown where you can select the one to switch to. The most
recent one will be at the bottom of the list.

> You will not be able to switch to a system image that is older than the one
> it had when you originally signed up.

## Using the new system image

Once you have changed the image, code that is currently running will
continue to use the old one, but new consoles you start will
have the new one. Any scheduled tasks and
websites will pick it up the next time they're (re)started. Always-on tasks
will need to be disabled, then enabled again to pick it up.
If you're using Jupyter/IPython notebooks, you'll need to kill
any existing ones using the process list on the "Consoles" page
to make them restart fully to pick up the new Python versions.

## Code changes

Updating the system image means that you may need to change your code afterwards
to make it work again.

### Pre-installed Python packages

Because the pre-installed Python modules will be upgraded,
the change might break any code you have that relies on the old
installed versions.

You can check what packages are installed in which system image [here](https://www.pythonanywhere.com/batteries_included/).

### Virtualenvs

Because of the changes to the point releases of Python
(for example, 3.7.0 might be replaced with 3.7.5), any
virtualenvs you have might break -- virtualenvs are not always portable from one
point release to another.

## Default Python versions

Along with system image each PythonAnywhere account has a set of
default Python versions.

One of them is the default Python 3 version used by `python3` and
`pip3` in Bash consoles.

Another one is the default Python used when "Run" button in our
in-browser editor is pressed.

Each system image has a range of available Python versions.
When one of those defaults is not available after the system
image change it will be automaticaly set to the most recent available
Python version.

For example you might have system image set to "classic" with default
`python3` set to `python3.3`. You update your system image to
"fishnchips" in which Python 3.3 is not available any more. So your
default `python3` is automaticaly set to `python3.8` which is the
default "fishnchips" Python version.

### Available Python versions for system images

<table class="python-versions">
  <thead>
    <tr>
      <th></th>
      <th>2.6</th>
      <th>2.7</th>
      <th>3.3</th>
      <th>3.4</th>
      <th>3.5</th>
      <th>3.6</th>
      <th>3.7</th>
      <th>3.8</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>classic</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>dangermouse</td>
      <td></td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>earlgrey</td>
      <td></td>
      <td>X</td>
      <td></td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td></td>
    </tr>
    <tr>
      <td>fishnchips</td>
      <td></td>
      <td>X</td>
      <td></td>
      <td></td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
      <td>X</td>
    </tr>
  </tbody>
</table>
