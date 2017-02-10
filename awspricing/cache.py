import os
import json
import logging
import re
import time


_USE_CACHE = None
_CACHE_PATH = None
_CACHE_MINUTES = None


DEFAULT_USE_CACHE = '0'  # False
DEFAULT_CACHE_PATH = os.path.join('/tmp', 'awspricing')
DEFAULT_CACHE_MINUTES = '1440'  # 1 day


logger = logging.getLogger(__name__)


def use_cache():
    global _USE_CACHE
    if _USE_CACHE is None:
        setting = os.getenv('AWSPRICING_USE_CACHE', DEFAULT_USE_CACHE)
        if setting not in ['0', '1']:
            raise ValueError("Unknown value '{}' for AWSPRICING_USE_CACHE."
                             .format(setting))
        _USE_CACHE = bool(int(setting))
    return _USE_CACHE


def cache_path():
    global _CACHE_PATH
    if _CACHE_PATH is None:
        setting = os.getenv('AWSPRICING_CACHE_PATH', DEFAULT_CACHE_PATH)
        if not os.path.isdir(setting):
            try:
                os.makedirs(setting)
            except:
                logger.exception("Unable to create cache directory: {}"
                                 .format(setting))
                raise
        _CACHE_PATH = setting
    return _CACHE_PATH


def cache_minutes():
    global _CACHE_MINUTES
    if _CACHE_MINUTES is None:
        setting = os.getenv('AWSPRICING_CACHE_MINUTES', DEFAULT_CACHE_MINUTES)
        try:
            _CACHE_MINUTES = int(setting)
        except ValueError:
            raise ValueError("Unknown value '{}' for AWSPRICING_CACHE_MINUTES. "
                             "Expected an integer.".format(setting))
    return _CACHE_MINUTES


def _is_cache_expired(path):
    try:
        mod_time = os.path.getmtime(path)
    except (OSError, IOError):
        return True
    cache_lifetime_seconds = time.time() - mod_time
    return cache_lifetime_seconds > cache_minutes() * 60


def _build_path(cache_key):
    if not re.match(r'^[A-Za-z0-9_\-]*$', cache_key):
        raise ValueError("Cache key '{}' contains invalid characters."
                         .format(cache_key))
    return os.path.join(cache_path(), cache_key)


def maybe_read_from_cache(cache_key):
    if not use_cache():
        return None

    path = _build_path(cache_key)
    if not os.path.exists(path):
        return None  # not in cache
    elif _is_cache_expired(path):
        os.remove(path)
        return None
    with open(path) as f:
        return json.load(f)


def maybe_write_to_cache(cache_key, data):
    if not use_cache():
        return

    path = _build_path(cache_key)
    if _is_cache_expired(path):
        with open(path, 'w') as f:
            f.write(json.dumps(data))
