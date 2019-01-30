
In the Application Builder, set the Persistent connection attribute in the Project parameters to false.

Use pip to install Jam.py. Open up a new Bash console from your [Dashboard](https://www.pythonanywhere.com/consoles) and run (for Python 3.7)

    pip3.7 install --user jam.py

Create a zip archive of your project folder, upload the archive in the [Files tab](https://www.pythonanywhere.com/files) and unzip it.

We assume that you are registered as `username` and your project is now located in the `/home/username/project_folder` directory.

Go to the [Web Tab](https://www.pythonanywhere.com/web_app_setup) and hit **Add a new web app**. Choose **Manual Configuration**, and then choose the **Python version** -- make sure it's the same version as the one you used to install Jam.py

In the Code section specify Source code and Working directory as `/home/username/project_folder`

In the WSGI configuration file: `/var/www/username_pythonanywhere_com_wsgi.py` file add the following code

    :::python
    import os
    import sys
    path = '/home/username/project_folder'
    if path not in sys.path:
        sys.path.append(path)
    from jam.wsgi import create_application
    application = create_application(path)

Reload the server.
