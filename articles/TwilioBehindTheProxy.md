<!--
.. title: How to get Twilio to work on Free accounts with the proxy (fixing requests ConnectonError in HTTPSConnectionPool)
.. slug: TwilioBehindTheProxy
.. date: 2018-02-05 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


If you're trying to use Twilio on a PythonAnywhere free account, you're likely to
run into an error that looks like this:

```python
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.twilio.com', port=443): Max retries exceeded with url: /2010-04-01/Accounts/xxxxxx/Messages.json (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7fe7acca1630>: Failed to establish a new connection: [Errno 111] Connection refused',))
```

That's because the Twilio API client currently has a [bug whereby it doesn't work behind a proxy server](https://github.com/twilio/twilio-python/issues/409).


However there is a simple fix, based on creating a custom "http client" object when
you instantiate your Twilio API client:


```python
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

account_sid = 'your account id here'
auth_token = 'your twilio token here'

client = Client(account_sid, auth_token, http_client=proxy_client)

# twilio api calls will now work from behind the proxy:
message = client.messages.create(to="...", from_='...', body='...')

```


