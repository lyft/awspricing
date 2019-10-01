from typing import Dict, Type, List
import boto3
import json
import datetime

from .offers import AWSOffer, get_offer_class  # noqa
from .cache import maybe_read_from_cache, maybe_write_to_cache


__version__ = "2.0.3"

_SERVICES = {}  # type: Dict[str, Type[AWSOffer]]
service_list = []  # type: List[str]

client = boto3.client('pricing', region_name='us-east-1')

TIME_FORMAT = '%b_%y_%Z'  # month, year, and timezone


def _fetch_offers():
    cache_key = 'offers'
    offers = maybe_read_from_cache(cache_key)
    if offers is not None:
        return offers

    maybe_write_to_cache(cache_key, offers)
    return offers


def _get_services():
    global service_list
    if not service_list:
        service_list = all_services_names()
    return service_list


def _fetch_offer(offer_name, version=None):
    services = _get_services()
    if offer_name not in services:
        raise ValueError('Unknown offer name, no corresponding AWS Service: {}'.format(offer_name))
    if not version:
        version = datetime.datetime.utcnow().strftime(TIME_FORMAT)

    cache_key = 'offer_{}_{}'.format(offer_name, version)
    offer = maybe_read_from_cache(cache_key)
    if offer is not None:
        return offer

    paginator = client.get_paginator('get_products')
    resp_pages = paginator.paginate(ServiceCode=offer_name, FormatVersion='aws_v1')
    offer = {}
    for page in resp_pages:
        for product in page['PriceList']:
            product_offer = json.loads(product)
            sku = product_offer['product']['sku']
            offer[sku] = product_offer

    maybe_write_to_cache(cache_key, offer)
    return offer


def all_services_names():
    paginator = client.get_paginator('describe_services')
    resp_pages = paginator.paginate()
    services = []
    for page in resp_pages:
        services.extend([x['ServiceCode'] for x in page['Services']])
    return services


def offer(service_name, version=None):
    if service_name not in _SERVICES:
        offer_data = _fetch_offer(service_name, version=version)
        _SERVICES[service_name] = get_offer_class(service_name)(offer_data)
    return _SERVICES[service_name]
