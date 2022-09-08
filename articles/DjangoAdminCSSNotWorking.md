
<!--
.. title: The Django Admin CSS isn't working!
.. slug: DjangoAdminCSSNotWorking
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



There are two ways to fix this.

The ugly/hacky way is to add a specific static files mapping pointing at the django admin css folder:

  * url: `/static/admin`
  * path: `/usr/local/lib/python3.10/dist-packages/django/contrib/admin/static/admin/` (or the path to the same folder inside your virtualenv, if you're using one)

But that's an ugly hack, and you'll soon run into problems with the rest of your CSS not loading.

The "proper" way to do it is to make sure you've got `django.contrib.admin` loaded in your `INSTALLED_APPS`, and then run `collectstatic`. There's a [full guide to django static files here](/pages/DjangoStaticFiles)
