import requests
from requests.adapters import HTTPAdapter
from typing import Dict, Type  # noqa

from .offers import AWSOffer, get_offer_class  # noqa
from .cache import maybe_read_from_cache, maybe_write_to_cache


__version__ = "1.1.4"


session = requests.Session()
session.mount('http://', HTTPAdapter(max_retries=5))
session.mount('https://', HTTPAdapter(max_retries=5))


OFFER_BASE_URL = 'https://pricing.us-east-1.amazonaws.com'
OFFER_INDEX_ENDPOINT = '/offers/v1.0/aws/index.json'


_OFFERS = None
_SERVICES = {}  # type: Dict[str, Type[AWSOffer]]


def _fetch_offers():
    cache_key = 'offers'
    offers = maybe_read_from_cache(cache_key)
    if offers is not None:
        return offers

    resp = session.get(OFFER_BASE_URL + OFFER_INDEX_ENDPOINT)
    resp.raise_for_status()
    offers = resp.json()['offers']

    maybe_write_to_cache(cache_key, offers)
    return offers


def _fetch_available_versions(offers, offer_name):
    cache_key = 'offers_version_{}'.format(offer_name)
    offers_version = maybe_read_from_cache(cache_key)
    if offers_version is not None:
        return offers_version

    offers_version_endpoint = offers[offer_name]['versionIndexUrl']
    resp = session.get(OFFER_BASE_URL + offers_version_endpoint)
    resp.raise_for_status()
    offers_version = resp.json()['versions']

    maybe_write_to_cache(cache_key, offers_version)
    return offers_version


def _get_offers():
    global _OFFERS
    if not _OFFERS:
        _OFFERS = _fetch_offers()
    return _OFFERS


def _fetch_offer(offer_name, version='current'):
    offers = _get_offers()
    if offer_name not in offers:
        raise ValueError('Unknown offer name: {}'.format(offer_name))

    cache_key = 'offer_{}_{}'.format(offer_name, version)
    offer = maybe_read_from_cache(cache_key)
    if offer is not None:
        return offer

    if version == 'current':
        offer_endpoint = offers[offer_name]['currentVersionUrl']
    else:
        other_versions = _fetch_available_versions(offers, offer_name)
        if version in other_versions:
            offer_endpoint = other_versions[version]['offerVersionUrl']
        else:
            raise ValueError('Invalid version specified {}. Must be one of: [{}]'.format(
                version, ', '.join(sorted(other_versions.keys(), reverse=True))))

    resp = session.get(OFFER_BASE_URL + offer_endpoint)
    resp.raise_for_status()
    offer = resp.json()

    maybe_write_to_cache(cache_key, offer)
    return offer


def all_service_names():
    return _get_offers().keys()


def offer(service_name, version='current'):
    if service_name not in _SERVICES:
        offer_data = _fetch_offer(service_name, version=version)
        _SERVICES[service_name] = get_offer_class(service_name)(offer_data)
    return _SERVICES[service_name]
