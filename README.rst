Python Client for ClearBlade Internet of Things (IoT) Core API
================================================================

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. Install pip package - ```pip install clearblade-cloud-iot```


2. Set an environment variable CLEARBLADE_CONFIGURATION which should point to your clearblade service account json file.


Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Code samples and snippets
~~~~~~~~~~~~~~~~~~~~~~~~~

Code samples and snippets live in the `samples/clearblade` folder.


Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Our client libraries are compatible with all current `active`_ and `maintenance`_ versions of
Python.

Python >= 3.7

.. _active: https://devguide.python.org/devcycle/#in-development-main-branch
.. _maintenance: https://devguide.python.org/devcycle/#maintenance-branches

Unsupported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Python <= 3.6

If you are using an `end-of-life`_
version of Python, we recommend that you update as soon as possible to an actively supported version.

.. _end-of-life: https://devguide.python.org/devcycle/#end-of-life-branches

Mac/Linux
^^^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate

Next Steps
~~~~~~~~~~

- clone the github repository.

- and execute the setup.py file like , python setup.py install.

- mostly if you change you imports from from google.cloud to clearblade.cloud everything else should work.

Note about types of times and binaryData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default time parameters (e.g. 'cloudUpdateTime', 'deviceAckTime', 'updateTime') are returned as RFC3339 strings (e.g. "2023-01-12T23:38:07.732Z").
To return times formatted as 'DatetimeWithNanoseconds' (defined in the 'google.api_core.datetime_helpers' module) as per the Google IoTCore Python SDK, set environment variable TIME_FORMAT to exactly 'datetimewithnanoseconds'.
If this environment variable is not set, or is set to any other value, then the default format is returned.

By default CONFIG binaryData is returned as a base64-encoded string and STATE binaryData is returned as a string (non-base64-encoded).
To return CONFIG and STATE binaryData as BYTE ARRAYS (non-base64-encoded) as per the Google IoTCore Python SDK, set environment variable BINARYDATA_FORMAT to exactly 'bytes'. If this environment variable is not set, or is set to any other value, then the default formats are returned.