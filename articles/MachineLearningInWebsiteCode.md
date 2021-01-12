<!--
.. title: Machine learning in website code
.. slug: MachineLearningInWebsiteCode
.. date: 2018-10-04 19:10:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Some machine learning frameworks have problems in PythonAnywhere websites
because our web serving framework doesn't allow them to use threads.

## Tensorflow

If you try to use TensorFlow in a website's code on PythonAnywhere, it probably
won't work.  The crash is so serious that you probably won't even
see anything in the error log -- just a message in the server log saying that
your worker processes died.

### The solution

Unfortunately we don't have a good solution for this if you're using TensorFlow
*directly* :-(

However, if you're using Keras with a TensorFlow backend, you can work around
the issue -- just switch to using the Theano backend instead.   That has been
confirmed to work.


## PyTorch

PyTorch also does some slightly strange threading stuff, and will hang when you
call certain functions from websites' code.  However, there's a simple
solution to that:

```python
import torch
torch.set_num_threads(1)
```

*Many thanks to Eden Canlilar for that solution!*
