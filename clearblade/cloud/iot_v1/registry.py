from http_client import SyncClient, AsyncClient
from config_manager import ClearBladeConfigManager

class EventNotificationConfig:
    def __init__(self, pub_sub_topic_name, subfolder_matches=None) -> None:
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
                 eventNotificationConfigs:list = [],
                 stateNotificationConfig:dict = {'pubsubTopicName': ''},
                 mqttConfig:dict = {'mqttEnabledState':'MQTT_ENABLED'},
                 httpConfig:dict = {'httpEnabledState':'HTTP_ENABLED'},
                 logLevel:str = 'NONE', credentials:list = []) -> None:
        self._id = id
        self._name = name
        self._event_notification_configs = eventNotificationConfigs
        self._state_notification_config = stateNotificationConfig
        self._mqtt_config = mqttConfig
        self._http_config = httpConfig
        self._loglevel = logLevel
        self._credentials = credentials

    @staticmethod
    def from_json(registry_json):
        event_notification_configs_json = registry_json['eventNotificationConfigs']
        event_notification_configs = []

        for event_notification_config_json in event_notification_configs_json:
            if "subfolderMatches" in event_notification_config_json:
                event_notification_config = EventNotificationConfig(event_notification_config_json['pubsubTopicName'], event_notification_config_json["subfolderMatches"])
            else:
                event_notification_config = EventNotificationConfig(event_notification_config_json['pubsubTopicName'])
            event_notification_configs.append(event_notification_config)

        return DeviceRegistry(id=registry_json['id'], name=registry_json['name'],
                              eventNotificationConfigs=event_notification_configs,
                              stateNotificationConfig=registry_json['stateNotificationConfig'],
                              mqttConfig=registry_json['mqttConfig'],
                              httpConfig=registry_json['httpConfig'],
                              credentials=registry_json['credentials'],
                              logLevel=registry_json['loglevel'])

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
    
class CreateDeviceRegistryRequest:
    def __init__(self, parent:str = None,
                 device_registry:DeviceRegistry = None) -> None:
        self._parent = parent
        self._device_registry = device_registry
        if device_registry.name.startswith('projects') == False:
            device_registry._name = parent + '/registries/' + device_registry.name

    @property
    def parent(self) -> str:
        return self._parent

    @property
    def device_registry(self)-> DeviceRegistry:
        return self._device_registry

class GetDeviceRegistryRequest:
    def __init__(self, name:str = None) -> None:
        self._name = name
    
    @property
    def name(self):
        return self._name

class DeleteDeviceRegistryRequest:
    def __init__(self, name:str = None) -> None:
        self._name = name
    
    @property
    def name(self):
        return self._name


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
        self._cb_config.registry_name = "MandarTest1"

    def _create_registry_body(self, registry: DeviceRegistry) :
        registry_json = {'id':registry.id, 'name':registry.name}
        if registry.credentials is not None:
            registry_json['credentials']=registry.credentials
        if registry.http_config is not None:
            registry_json['httpConfig']=registry.http_config
        if registry.mqtt_config is not None:
            registry_json['mqttConfig']=registry.mqtt_config
        if registry.state_notification_config is not None:
            registry_json['stateNotificationConfig']=registry.state_notification_config
        if registry.event_notification_configs is not None:
            registry_json['eventNotificationConfigs']=registry.event_notification_configs
        if registry.log_level is not None:
            registry_json['loglevel']=registry.log_level
        return registry_json
            
    def _prepare_params_for_registry_list(self, request:ListDeviceRegistriesRequest):
        request_params = {'parent':request.parent}
        if request.page_size:
            request_params['page_size'] = request.page_size
        if request.page_token:
            request_params['page_token'] = request.page_token
        return request_params

    def create(self,
        request: CreateDeviceRegistryRequest = None)->DeviceRegistry:
        body = self._create_registry_body(request.device_registry)
        params = {'parent':request.parent}
        print(body)
        sync_client = SyncClient(clearblade_config=self._cb_config.admin_config)
        response = sync_client.post(api_name = "cloudiot",request_body=body,request_params=params)
        print(response.json())
        return DeviceRegistry.from_json(response.json())

    async def create_async(self,
        request: CreateDeviceRegistryRequest = None)->DeviceRegistry:
        body = self._create_registry_body(request.device_registry)
        params = {'parent':request.parent}
        print(body)
        async_client = AsyncClient(clearblade_config=self._cb_config.admin_config)
        response = await async_client.post(api_name = "cloudiot",request_body=body,request_params=params)
        print(response.json())
        return DeviceRegistry.from_json(response.json())

    def get(self,
            request: GetDeviceRegistryRequest = None):
        sync_client = SyncClient(clearblade_config=self._cb_config.regional_config)
        response = sync_client.get(api_name = "cloudiot")
        print(response.json())
        return DeviceRegistry.from_json(response.json())

    async def get_async(self,
            request: GetDeviceRegistryRequest = None):
        async_client = AsyncClient(clearblade_config=await self._cb_config.regional_config_async)
        response = await async_client.get(api_name = "cloudiot")
        print(response.json())
        return DeviceRegistry.from_json(response.json())

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

    def delete(self,
            request: DeleteDeviceRegistryRequest = None):
        params = {'name':request.name}
        sync_client = SyncClient(clearblade_config=self._cb_config.admin_config)
        response = sync_client.delete(api_name = "cloudiot",request_params=params)
        return response

    async def delete_async(self,
            request: DeleteDeviceRegistryRequest = None):
        params = {'name':request.name}
        async_client = AsyncClient(clearblade_config=self._cb_config.admin_config)
        response = await async_client.delete(api_name = "cloudiot",request_params=params)
        return response
