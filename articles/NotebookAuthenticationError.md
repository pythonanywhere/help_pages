<!--
.. title: Notebook authentication error
.. slug: NotebookAuthenticationError
.. date: 2021-11-23 16:54:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

If these persist after you have logged out and logged in again, they may be the
result of something in your browser interfering with the authentication.

The usual suspects in this case are extensions that block cross-site cookies.
Try disabling extensions and trying again to see whether that is the case. Then
you can check each extension seperately to see which is causing the issue.

## Safari
We have had one user let us know that disabling "Hide IP address from trackers"
and "Prevent cross-site Tracking" in the privacy preferences allowed them to
authenticate to the notebook.
