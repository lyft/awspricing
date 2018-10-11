==========
awspricing
==========

A Python library for working with the `AWS Price List API <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html>`_.

Features:

* Simple boto3-like interface
* Service-specific helpers (only EC2 and RDS thus far)
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

    ec2_offer.reserved_hourly_combinations(
      'c4.large'
    ) # [{'cost': 0.063, 'region': 'us-east-1', 'offering class': 'standard', 'purchase_option': 'No Upfront', 'lease_contract_length': '1yr'}, ...]

    ec2_offer.reserved_hourly_combinations_kthclosest(
        ec2_offer.reserved_hourly_combinations('c4.large'),
        1
    ) # {
            'cost': 0.05401674277016742, 
            'region': 'us-east-1', 
            'offering class': 'convertible', 
            'purchase_option': 'Partial Upfront', 
            'lease contract length': '3yr'
        } 

    rds_offer = awspricing.offer('AmazonRDS')

    rds_offer.search_skus(
      instance_type='db.m4.large',
      location='US East (N. Virginia)',
      database_engine='MySQL',
      license_model='No license required',
      deployment_option='Multi-AZ'
    ) # {'QPZNR6MYN432XTPU'}

    rds_offer.ondemand_hourly(
      'db.m4.large',
      'MySQL',
      license_model='No license required',
      deployment_option='Multi-AZ',
      region='us-east-1'
    ) # 0.35
..

**Note** : AWS provides the pricing list in json format with no warranty of format change.  If a format change by AWS causes a breaking change; the below mitigation can be used at the cost of "stale" pricing.

.. code-block:: python

    import awspricing

    # For finding EC2 price list versions see script below or download https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/index.json
    ec2_offer_old = awspricing.offer('AmazonEC2', version='some_other_version')

    # For finding RDS price list versions see script below or download https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/index.json
    rds_offer_old = awspricing.offer('AmazonRDS', version='some_other_version')


.. code-block:: sh

    $ # EC2
    $ curl https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/index.json | python -m json.tool

    $ # RDS
    $ curl https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/index.json | python -m json.tool


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