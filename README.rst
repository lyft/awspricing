==========
awspricing
==========

A Python library for working with the `AWS Price List API <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html>`_.

Features:

* Simple boto3-like interface
* Service-specific helper functions (only EC2 thus far)
* Local caching support

Installation
------------

.. code-block:: sh

    $ pip install awspricing

Usage
-----

.. code-block:: python

    import awspricing

    ec2_offer = awspricing.offer('AmazonEC2')

    ec2_offer.search_skus(
      instance_type='c4.large',
      location='US East (N. Virginia)',
      operating_system='Linux',
    )  # {'4C7N4APU9GEUZ6H6', 'MBQPYDJSY3BY84BH', 'MDKVAJXMJGZFDJUE'}

    ec2_offer.reserved_hourly(
      'c4.xlarge',
      operating_system='Linux',
      lease_contract_length='3yr',
      offering_class='convertible',
      purchase_option='Partial Upfront',
      region='us-east-1'
    )  # 0.10845205479452055


Configuration
-------------

Cache
~~~~~

Cache can be configured via the following environment variables:

``AWSPRICING_USE_CACHE``: Whether to use a simple file-based cache. Valid values are ``0|1``. Defaults to ``0`` (false).

``AWSPRICING_CACHE_PATH``: Prefix to write cache files. Defaults to ``/tmp/awspricing``.

``AWSPRICING_CACHE_MINUTES``: Number of minutes to keep cache for. Defaults to ``1440`` (1 day).


Developing
----------

Environment setup
~~~~~~~~~~~~~~~~~

Run the following commands (preferably in a virtualenv) to setup your environment:

.. code-block:: sh
    python setup.py develop
    pip install -r test-requirements.txt

Running unit tests
~~~~~~~~~~~~~~~~~~

Simply run `make test` after environment setup to run unit tests.

Running mypy (type checker)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following commands can be used to run type checks. Note that a ``python3``
interpreter is required for mypy.

.. code-block:: sh

    pip install mypy
    make test_mypy
