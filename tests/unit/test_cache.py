import time

import mock
import pytest

from awspricing import cache


class TestCache(object):

    def test_build_path(self):
        assert cache._build_path('test') == '/tmp/awspricing/test'

    def test_build_path_invalid(self):
        with pytest.raises(ValueError):
            cache._build_path('../strange/things')
        with pytest.raises(ValueError):
            cache._build_path('test$@')
        with pytest.raises(ValueError):
            cache._build_path('..test')

    @mock.patch('os.path.getmtime')
    def test_is_cache_expired_no_file(self, getmtime):
        filename = '/tmp/nonexistent-file'
        getmtime.side_effect = OSError()
        assert cache._is_cache_expired(filename)
        getmtime.assert_called_once_with(filename)

    @mock.patch('os.path.getmtime')
    @mock.patch.object(cache, 'cache_minutes')
    def test_is_cache_expired_old(self, cache_minutes, getmtime):
        filename = '/tmp/some-cache'
        getmtime.return_value = time.time() - 600  # modified 10 minutes ago
        cache_minutes.return_value = 5
        assert cache._is_cache_expired(filename)
        getmtime.assert_called_once_with(filename)
        cache_minutes.assert_called_once()

    @mock.patch('os.path.getmtime')
    @mock.patch.object(cache, 'cache_minutes')
    def test_is_cache_expired_new(self, cache_minutes, getmtime):
        filename = '/tmp/some-cache'
        getmtime.return_value = time.time() - 60  # modified 1 minute ago
        cache_minutes.return_value = 5
        assert not cache._is_cache_expired(filename)
        getmtime.assert_called_once_with(filename)
        cache_minutes.assert_called_once()
