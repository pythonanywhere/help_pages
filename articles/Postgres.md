
<!--
.. title: Can I use Postgres on PythonAnywhere?
.. slug: Postgres
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



Yes! You'll need to upgrade to a paying account. 

Currently, Postgres is only available via the **Custom** account type. Enable Postgres, set your disk quota, and then choose the other features (number of web apps etc) as appropriate 

In more detail: 

  * If you have a free account, go to the Account page, and click on the "Change your custom plan" button. Switch the Postgres option on, choose how much disk space you want for your PG databases, choose any other paid features you want, and then click "Upgrade to this custom plan". This will take you through a payment confirmation process. 
  * If you already have a custom plan, go to the Account page, and click on the "Change your custom plan" button. The popup window will be pre-configured with all of your current custom plan settings, so you just need to switch the Postgres option on, choose how much disk space you want for your PG databases, and then click "Switch to this custom plan". This will take you through the normal payment confirmation process. 
  * If you have a Hacker, Web Dev, or Startup account it's a little more complicated -- you can go to the Account page and click on the "Build a custom plan" button, but right now, the popup won't be initialised with your current account's settings (we're working on a fix for this). So you'll need to set the sliders to match those as well as switch on Postgres -- there's a table of the correct settings below. Once you've configured a custom plan with your settings and with Postgres enabled, you can click on "Switch to this custom plan" and do the payment confirmation. Sorry for the inconvenience -- we only realised that this annoyance was there right at the end of development and we didn't want to delay the Postgres release while we tinkered with the UI. 

Here are the settings for the Custom plan popup to mimic the non-custom plans: 

| 

Hacker  | 

Web Developer  | 

Startup  
---|---|---|---  

CPU time per day:  | 

3000  | 

3000  | 

50000   

Number of web apps:  | 

1  | 

3  | 

8   

Number of web workers:  | 

2  | 

3  | 

5   

Disk space (GB):  | 

0.5  | 

5  | 

50   
