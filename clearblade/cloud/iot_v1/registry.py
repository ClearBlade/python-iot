from http_client import SyncClient, AsyncClient
from config_manager import ClearBladeConfigManager

class EventNotificationConfig:
    def __init__(self, pub_sub_topic_name, subfolder_matches) -> None:
        self._pub_sub_topic_name = pub_sub_topic_name
        self._sub_folder_matches = subfolder_matches

    @property
    def pub_sub_topic_name(self):
        return self._pub_sub_topic_name
        
    @property
    def sub_folder_matches(self):
        return self._sub_folder_matches

class DeviceRegistry:
    def __init__(self, id:str = None, name:str = None, 
                 event_notification_configs:list = [EventNotificationConfig], 
                 state_notification_config:dict = {'pub_sub_topic_name':None},
                 mqtt_config:dict = {'mqttEnabledState':None}, 
                 http_config:dict = {'httpEnabledState':None},
                 log_level:str = None, credentials:list = []) -> None:
        self._id = id
        self._name = name
        self._event_notification_configs = event_notification_configs
        self._state_notification_config = state_notification_config
        self._mqtt_config = mqtt_config
        self._http_config = http_config
        self._loglevel = log_level
        self._credentials = credentials

    @staticmethod
    def from_json(registry_json):
        event_notification_configs_json = registry_json['event_notification_configs']
        event_notification_configs = []

        for event_notification_config_json in event_notification_configs_json:
           event_notification_config = EventNotificationConfig(event_notification_config_json['pubsubTopicName'])
           event_notification_configs.append(event_notification_config)
     
        return DeviceRegistry(id=registry_json['id'], name=registry_json['name'], 
                              event_notification_configs=event_notification_configs,
                              state_notification_config=registry_json['stateNotificationConfig'],
                              mqtt_config=registry_json['mqttConfig'],
                              http_config=registry_json['httpConfig'],
                              credentials=registry_json['credentials'])

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def event_notification_configs(self):
        return self._event_notification_configs

    @property
    def state_notification_config(self):
        return self._state_notification_config

    @property
    def mqtt_config(self):
        return self._mqtt_config

    @property
    def http_config(self):
        return self._http_config

    @property
    def log_level(self):
        return self._loglevel

    @property
    def credentials(self):
        return self._credentials
    

class ListDeviceRegistriesRequest:
    def __init__(self, parent:str = None, 
                 page_size:int = None, 
                 page_token:str = None) -> None:
        self._parent = parent
        self._page_size = page_size
        self._page_token = page_token

    @property
    def parent(self):
        return self._parent

    @property
    def page_size(self):
        return self._page_size

    @property
    def page_token(self):
        return self._page_token

class ListDeviceRegistriesResponse:
    def __init__(self) -> None:
        self._device_registries = None
        self._next_page_token = None

    @property
    def raw_page(self):
        return self

    @property
    def device_registries(self):
        return self._device_registries

    @property
    def next_page_token(self):
        return self._next_page_token
    
class ClearBladeRegistryManager():
    def __init__(self) -> None:
        self._cb_config = ClearBladeConfigManager()

    def _prepare_params_for_registry_list(self, request:ListDeviceRegistriesRequest):
        request_params = {'parent':request.parent}
        if request.page_size:
            request_params['page_size'] = request.page_size
        if request.page_token:
            request_params['page_token'] = request.page_token
        return request_params

    def create(self):
        pass

    def get(self):
        pass

    def list(self, 
            request: ListDeviceRegistriesRequest = None):

        request_params = self._prepare_params_for_registry_list(request=request)    
        sync_client = SyncClient(clearblade_config=self._cb_config.admin_config)
        response = sync_client.get(api_name = "cloudiot",request_params=request_params)
        print(response.json())

    def list_async(self):
        request_params = self._prepare_params_for_registry_list(request=request)    
        async_client = AsyncClient(clearblade_config= self._cb_config.admin_config)
        response = async_client.get(api_name = "cloudiot",request_params=request_params)
        print(response.json())

    def delete(self):
        pass