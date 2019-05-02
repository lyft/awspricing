import pytest
import mock

from awspricing.constants import Enum


class TestEnum(object):

    @mock.patch('awspricing.boto3.client')
    def test_simple_enum(self, mock_client):
        Color = Enum('red', 'green', 'blue')

        assert Color.RED == 'red'
        with pytest.raises(AttributeError):
            Color.PURPLE

        assert 'red' in Color.values()
        assert 'car' not in Color.values()

    def test_overriden_values(self):
        Years = Enum(one_year="1year", three_year="3year")
        assert Years.ONE_YEAR == '1year'
        assert '1year' in Years.values()

    def test_mixed_case(self):
        Seasons = Enum(season_SPRING="Spring", season_AUTUMN="Autumn")
        assert Seasons.SEASON_SPRING == 'Spring'
        assert 'Spring' in Seasons.values()
