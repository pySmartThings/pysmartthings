"""Tests for the SmartThings file."""

from pysmartthings import create
from pysmartthings.app import App
from pysmartthings.oauth import OAuth
from pysmartthings.smartthings import SmartThings

from . import api_mock
from .utilities import get_json


class TestSmartThings:
    """Tests for the SmartThings class."""

    @staticmethod
    def test_create(requests_mock):
        """Tests the create method."""
        # Arrange
        api_mock.setup(requests_mock)
        # Act
        smartthings = create(api_mock.API_TOKEN)
        devices = smartthings.devices()
        # assert
        assert len(devices) == 4

    @staticmethod
    def test_devices(requests_mock):
        """Tests devices are retrieved"""
        # arrange
        api_mock.setup(requests_mock)
        smartthings = SmartThings(api_mock.API_TOKEN)
        # act
        devices = smartthings.devices()
        # assert
        assert len(devices) == 4

    @staticmethod
    def test_locations(requests_mock):
        """Tests locations are retrieved."""
        # arrange
        api_mock.setup(requests_mock)
        smartthings = SmartThings(api_mock.API_TOKEN)
        # act
        locations = smartthings.locations()
        # assert
        assert len(locations) == 2

    @staticmethod
    def test_apps(requests_mock):
        """Tests locations are retrieved."""
        # arrange
        api_mock.setup(requests_mock)
        smartthings = SmartThings(api_mock.API_TOKEN)
        # act
        apps = smartthings.apps()
        # assert
        assert len(apps) == 1

    @staticmethod
    def test_create_app(requests_mock):
        """Tests the create app method."""
        # Arrange
        api_mock.setup(requests_mock)
        smartthings = SmartThings(api_mock.API_TOKEN)
        app = App()
        data = get_json('app_post_request.json')
        data['appId'] = api_mock.APP_ID
        app.apply_data(data)
        # Act
        app, oauth = smartthings.create_app(app)
        # Assert
        assert app.app_id == 'c6cde2b0-203e-44cf-a510-3b3ed4706996'
        assert oauth.client_id == '7cd4d474-7b36-4e03-bbdb-4cd4ae45a2be'
        assert oauth.client_secret == '9b3fd445-42d6-441b-b386-99ea51e13cb0'

    @staticmethod
    def test_delete_app(requests_mock):
        """Tests the delete app method."""
        # Arrange
        api_mock.setup(requests_mock)
        smartthings = SmartThings(api_mock.API_TOKEN)
        # Act/Assert
        smartthings.delete_app('c6cde2b0-203e-44cf-a510-3b3ed4706996')
        # Assert

    @staticmethod
    def test_get_app_oauth(requests_mock):
        """Tests retrieval of OAuth settings."""
        # Arrange
        api_mock.setup(requests_mock)
        smartthings = SmartThings(api_mock.API_TOKEN)
        app_id = 'c6cde2b0-203e-44cf-a510-3b3ed4706996'
        # Act
        oauth = smartthings.get_app_oauth(app_id)
        # Assert
        assert oauth.app_id == app_id
        assert oauth.client_name == 'pysmartthings-test'
        assert oauth.scope == ['r:devices']

    @staticmethod
    def test_update_app_oauth(requests_mock):
        """Tests updating OAuth settings."""
        # Arrange
        api_mock.setup(requests_mock)
        smartthings = SmartThings(api_mock.API_TOKEN)
        app_id = 'c6cde2b0-203e-44cf-a510-3b3ed4706996'
        oauth = OAuth(app_id)
        oauth.client_name = 'pysmartthings-test'
        oauth.scope.append('r:devices')
        # Act
        oauth_entity = smartthings.update_app_oauth(oauth)
        # Assert
        assert oauth_entity.app_id == oauth.app_id
        assert oauth_entity.client_name == oauth.client_name
        assert oauth_entity.scope == oauth.scope
