from http_client import SyncClient, AsyncClient
from config_manager import ClearBladeConfigManager
from pagers import ListDevicesPager
from device_types import *

class ClearBladeDeviceManager():

    def __init__(self) -> None:
        #create the ClearBladeConfig object
        self._config_manager = ClearBladeConfigManager()
        self._config_manager.registry_name = "gargi_python"

    def _prepare_for_send_command(self,
                                  request: SendCommandToDeviceRequest,
                                  name: str = None,
                                  binary_data: bytes = None,
                                  subfolder: str = None):
        has_flattened_params = any([name, binary_data])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        if request is None:
            request = SendCommandToDeviceRequest(name, binary_data, subfolder)
        params = {'name':request.name,'method':'sendCommandToDevice'}
        body = {'binaryData':request.binary_data.decode("utf-8")}

        return params,body

    def _create_device_body(self, device: Device) :
        return {'id':device.name, 'name':device.name,
                'credentials':device.credentials, 'lastErrorStatus':device.last_error_status,
                'config':device.config, 'state':device.state,
                'loglevel':device.log_level, 'metadata':device.meta_data,
                'gatewayConfig':device.config}

    def _create_device_from_response(self, json_response) -> Device :
        return Device.from_json(json=json_response)

    def _prepare_modify_cloud_config_device(self,
                                            request: ModifyCloudToDeviceConfigRequest,
                                            name, binary_data, version_to_update):

        has_flattened_params = any([name, binary_data])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        if request is None:
            request = ModifyCloudToDeviceConfigRequest(name=name,version_to_update=version_to_update, binary_data=binary_data)

        params = {'name': request.name, 'method': 'modifyCloudToDeviceConfig'}
        body = {'binaryData': request.binary_data.decode("utf-8"), 'versionToUpdate':request.version_to_update}

        return params, body

    def _create_device_config(self, response):
        return DeviceConfig.from_json(response)

    def _create_device_list_from_response(self, json_response):
        devicesList = []
        print(json_response['devices'])
        for deviceJson in json_response['devices']:
            devicesList.append(Device.from_json(json=deviceJson))
        return devicesList

    def send_command(self,
                    request: SendCommandToDeviceRequest,
                    name: str = None,
                    binary_data: bytes = None,
                    subfolder: str = None):

        params, body = self._prepare_for_send_command(request, name, binary_data, subfolder)
        sync_client = SyncClient(clearblade_config=self._config_manager.regional_config)
        return sync_client.post(api_name="cloudiot_devices", request_params=params, request_body=body)

    async def send_command_async(self,
                                 request: SendCommandToDeviceRequest = None,
                                 name: str = None,
                                 binary_data: str = None,
                                 subfolder: str = None ):

        params, body = self._prepare_for_send_command(request, name, binary_data, subfolder)
        async_client = AsyncClient(clearblade_config=await self._config_manager.regional_config_async)
        return await async_client.post(api_name="cloudiot_devices",
                                       request_params=params,
                                       request_body=body)

    def create(self, request: CreateDeviceRequest,
                     parent: str = None,
                     device: Device = None) -> Device:
        body = self._create_device_body(request.device)
        sync_client = SyncClient(clearblade_config=self._config_manager.regional_config)
        response = sync_client.post(api_name="cloudiot_devices",
                                    request_body=body)

        # return the device only if status code is 200
        # other wise return None
        if response.status_code == 200:
            return self._create_device_from_response(response.json())
        return None

    async def create_async(self, request: CreateDeviceRequest,
                           parent: str = None,
                           device: Device = None) -> Device:

        body = self._create_device_body(request.device)
        async_client = AsyncClient(clearblade_config= await self._config_manager.regional_config_async)
        response = await async_client.post(api_name="cloudiot_devices", request_body=body)

        if response.status_code == 200:
            return self._create_device_from_response(response.json())
        return None

    def modify_cloud_device_config(self,
                                   request: ModifyCloudToDeviceConfigRequest,
                                   name:str = None,
                                   version_to_update : int = None,
                                   binary_data: bytes = None):
        params, body = self._prepare_modify_cloud_config_device(request=request, name=name,
                                                                binary_data=binary_data,
                                                                version_to_update=version_to_update)
        sync_client = SyncClient(clearblade_config=self._config_manager.regional_config)
        response = sync_client.post(api_name="cloudiot_devices", request_params=params, request_body=body)

        if response.status_code == 200:
            return self._create_device_config(response.json)

        return None

    async def modify_cloud_device_config_async(self,
                                        request: ModifyCloudToDeviceConfigRequest,
                                        name:str = None,
                                        version_to_update : int = None,
                                        binary_data: bytes = None):
        params, body = self._prepare_modify_cloud_config_device(request=request, name=name,
                                                                binary_data=binary_data,
                                                                version_to_update=version_to_update)
        async_client = AsyncClient(clearblade_config=await self._config_manager.regional_config_async)
        response = await async_client.post(api_name="cloudiot_devices",
                                           request_params=params,
                                           request_body=body)
        if response.status_code == 200:
            return self._create_device_config(response.json)
        return None

    def get_device_list_response(self, request:ListDevicesRequest):
        sync_client = SyncClient(clearblade_config= self._config_manager.regional_config)

        params = request._prepare_params_for_list()
        response = sync_client.get(api_name="cloudiot_devices",request_params=params)

        if response.status_code == 200:
            return ListDevicesResponse.from_json(response.json())
        return None

    def list(self,
             request: ListDevicesRequest):

        device_list_response = self.get_device_list_response(request=request)
        #devices = device_list_response.devices
        #yield from devices

        if device_list_response:
            return ListDevicesPager(method=self.get_device_list_response,
                                    request=request, response=device_list_response)
        return None

    async def list_async(self,
                         request: ListDevicesRequest):
        async_client = AsyncClient(clearblade_config=self._config_manager.regional_config)
        params = request._prepare_params_for_list()
        response = await async_client.list(api_name="cloudiot_devices",request_params=params)

        if response.status_code == 200:
            return response.json()
        return None

    def get(self,
            request: GetDeviceRequest) -> Device:

        params = {'name':request.name}
        sync_client = SyncClient(clearblade_config=self._config_manager.regional_config)
        response = sync_client.get(api_name="cloudiot_devices", request_params=params)

        if response.status_code == 200:
            return self._create_device_from_response(response.json())
        return None

    async def get_async(self,
                        request: GetDeviceRequest) -> Device:
        params = {'name':request.name}
        async_client = AsyncClient(clearblade_config=await self._config_manager.regional_config_async)
        response = await async_client.get(api_name="cloudiot_devices", request_params=params)

        if response.status_code == 200:
            return self._create_device_from_response(response.json())
        return None

    def delete(self,
               request: DeleteDeviceRequest):
        params = {'name':request.name}
        sync_client = SyncClient(clearblade_config=self._config_manager.regional_config)
        response = sync_client.delete(api_name="cloudiot_devices",request_params=params)
        return response

    async def delete_async(self,
               request: DeleteDeviceRequest):
        params = {'name':request.name}
        async_client = AsyncClient(clearblade_config=await self._config_manager.regional_config_async)
        response = await async_client.delete(api_name="cloudiot_devices", request_params=params)
        return response

    def update(self,
               request: UpdateDeviceRequest) -> Device:
        params, body = request._prepare_params_body_for_update()
        sync_client = SyncClient(clearblade_config=self._config_manager.regional_config)
        response = sync_client.patch(api_name= "cloudiot_devices",request_body=body, request_params=params)

        if response.status_code == 200:
            return self._create_device_from_response(json_response=response.json())
        return None

    async def update_async(self,
                           request: UpdateDeviceRequest) -> Device:
        async_client = AsyncClient(clearblade_config=await self._config_manager.regional_config_async)
        params, body = request._prepare_params_body_for_update()
        response = await async_client.patch(api_name="cloudiot_devices",request_body=body, request_params=params)

        if response.status_code == 200:
            return self._create_device_from_response(json_response=response.json())
        return None


    def bindGatewayToDevice(self,
            request: BindUnBindGatewayDeviceRequest) :
        sync_client = SyncClient()
        body = {'deviceId':request.deviceId, 'gatewayId':request.gatewayId}
        params = {'method':'bindDeviceToGateway'}
        response = sync_client.post(api_name="cloudiot", request_params=params, request_body=body)

        return response

    async def bindGatewayToDevice_async(self,
            request: BindUnBindGatewayDeviceRequest) :
        async_client = AsyncClient()
        body = {'deviceId':request.deviceId, 'gatewayId':request.gatewayId}
        params = {'method':'bindDeviceToGateway'}
        response = await async_client.post(api_name="cloudiot", request_params=params, request_body=body)
        return response

    def unbindGatewayFromDevice(self,
            request: BindUnBindGatewayDeviceRequest) :
        sync_client = SyncClient()
        body = {'deviceId':request.deviceId, 'gatewayId':request.gatewayId}
        params = {'method':'unbindDeviceFromGateway'}
        response = sync_client.post(api_name="cloudiot", request_params=params, request_body=body)
        return response

    async def unbindGatewayFromDevice_async(self,
            request: BindUnBindGatewayDeviceRequest) :
        async_client = AsyncClient()
        body = {'deviceId':request.deviceId, 'gatewayId':request.gatewayId}
        params = {'method':'unbindDeviceFromGateway'}
        response = await async_client.post(api_name="cloudiot",request_params=params, request_body=body)
        return response

    def getDeviceSatesList(self,
            request: GetDeviceStatesList):
        sync_client = SyncClient()
        params = {'name':request.name, 'numStates':request.numStates}
        response = sync_client.get(api_name="cloudiot_devices_states",request_params=params)

        if response.status_code == 200:
            return response.json()
        return None

    async def getDeviceSatesList_async(self,
            request: GetDeviceRequest):
        async_client = AsyncClient()
        params = {'name':request.name, 'numStates':request.numStates}
        response = await async_client.get(request_params=params)

        if response.status_code == 200:
            return response.json()
        return None

    def getDeviceConfigVersionsList(self,
            request: GetDeviceConfigVersionsList):
        sync_client = SyncClient()
        params = {'name':request.name, 'numVersions':request.numVersions}
        response = sync_client.get(api_name="cloudiot_devices_configVersions",request_params=params)

        if response.status_code == 200:
            return response.json()
        return None

    async def getDeviceConfigVersionsList_async(self,
            request: GetDeviceConfigVersionsList):
        async_client = AsyncClient()
        params = {'name':request.name, 'numVersions':request.numVersions}
        response = await async_client.get(api_name="cloudiot_devices_configVersions", request_params=params)

        if response.status_code == 200:
            return response.json()
        return None
