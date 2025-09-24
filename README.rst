Python Client for ClearBlade IoT Core API
================================================================

Quick start
-----------
**Notes**

1. This SDK is for use with ClearBlade IoT Core Standard and ClearBlade IoT Core Enterprise.

2. ClearBlade IoT **Core** Enterprise is DIFFERENT from ClearBlade IoT Enterprise!!!

3. If you are using ClearBlade but not using ClearBlade IoT Core (Standard or Enterprise), then you need this different SDK: `<https://github.com/ClearBlade/ClearBlade-Python-SDK>`_.

4. To understand how IoT Core Enterprise differs from Standard, look here: `<https://docs.clearblade.com/iotenterprise/iot-core>`_.



To use this SDK, you first need to go through the following steps:

1. Install pip package - ```pip install clearblade-cloud-iot```

2. Set an environment variable **CLEARBLADE_CONFIGURATION**, pointing to your ClearBlade service account JSON file (see below).

3. Optionally set an environment variable **BINARYDATA_AND_TIME_GOOGLE_FORMAT** to True. Look at **Note about types of times and binaryData** below for details.


To create a service account and download a credentials JSON file look at the appropriate link below:

`ClearBlade IoT Core Standard <https://docs.clearblade.com/iotcore/manage-service-accounts-in-a-project-standard>`_

`ClearBlade IoT Core Enterprise <https://docs.clearblade.com/iotcore/manage-service-accounts-in-a-project-enterprise>`_



Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to create isolated Python environments. It addresses dependencies and versions and, indirectly, permissions.

With `virtualenv`_, it's possible to install this library without system install permissions and clashing with the installed system dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Code samples and snippets
~~~~~~~~~~~~~~~~~~~~~~~~~

Code samples and snippets live in the samples/clearblade folder.


Supported Python versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Our client libraries are compatible with all current `active`_ and `maintenance`_ versions of
Python.

Python >= 3.7

.. _active: https://devguide.python.org/devcycle/#in-development-main-branch
.. _maintenance: https://devguide.python.org/devcycle/#maintenance-branches

Unsupported Python versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Python <= 3.6

If you are using an `end-of-life`_ version of Python, we recommend you update it to an actively supported version as soon as possible.

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

Next steps
~~~~~~~~~~

- Clone the GitHub repository.

- Execute the setup.py file like Python setup.py install.

- Everything else should work if you change your imports from google.cloud to clearblade.cloud.

Note about types of times and binaryData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- By default, the following parameters are returned as the shown types:

1. All time parameters (e.g. **cloudUpdateTime**, **deviceAckTime**, **updateTime**): **RFC3339** strings (e.g. "2023-01-12T23:38:07.732Z")
2. **CONFIG binaryData**: **base64-encoded string**
3. **STATE binaryData**: **NON-base64-encoded string**


- To return these parameters using the same types used by the **Google IoTCore Python SDK**, set environment variable **BINARYDATA_AND_TIME_GOOGLE_FORMAT** to **True** (case-insensitive string). This will ensure the following parameters are returned as the shown types:

1. All times: **DatetimeWithNanoseconds** (defined in the **proto.datetime_helpers** module)
2. All **binaryData** (CONFIG, STATE etc.): **BYTE ARRAYS**

- If this environment variable is not set, or is set to any unexpected values, then the default types listed previously are used.

Note about performance:
~~~~~~~~~~~~~~~~~~~~~~~

- By default, calls to some SDK functions cause a REST request to be sent to acquire the registry API keys found on the IoTCore UI Registry Details page. Those keys are cached for subsequent operations to improve performance. However, these caches do not persist if the application is stopped and restarted, as would be the case with typical serverless functions (e.g., Google Cloud Functions, AWS Lambda, etc.). To improve those functions' performance, the REST call can be prevented by passing the API keys as environment variables:

1. **REGISTRY_URL**: **string**
2. **REGISTRY_SYSKEY**: **string**
3. **REGISTRY_TOKEN**: **string**

Note about running from the source instead of the PyPi (pip) module:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- To temporarily use the source code in this repo instead of the installed PyPi (pip) module, do the following:

1. Clone this repo.
2. Check out the desired branch using **git checkout <branch>**.
3. In your code find where **clearblade** or **clearblade.cloud** is being imported.
4. Precede that line with **import sys** and **sys.path.insert(0, <path_to_python-iot>)**. The path must end with python-iot. For example:

.. code-block:: console

    import sys
    sys.path.insert(0, "path/to/python-iot")

    from clearblade.cloud import iot_v1
