from http_client import SyncClient, AsyncClient

class Device():
    """
    Data class for Clearblade Device
    """
    #TODO: find a better way to construct the Device object. I dont like so much parameter in a constructor
    def __init__(self, id: str = None, name: str = None, num_id: str=None,
                 credentials: list=[], last_heartbeat_time: str = None, last_event_time: str = None,
                 last_state_time: str = None, last_config_ack_time: str = None,
                 last_config_send_time: str = None, blocked: bool = False,
                 last_error_time: str = None, last_error_status_code: dict = {"code":None, "message":""},
                 config: dict = {"cloudUpdateTime":None, "version":""} ,
                 state: dict = {"updateTime":None, "binaryData":None},
                 log_level: str = "NONE", meta_data: dict = {}, gateway_config : dict = {}  ) -> None:

        self._id = id
        self._name = name
        self._num_id = num_id
        self._credentials = credentials
        self._last_heartbeat_time = last_heartbeat_time
        self._last_event_time = last_event_time
        self._last_state_time = last_state_time
        self._last_config_ack_time = last_config_ack_time
        self._last_config_send_time = last_config_send_time
        self._blocked = blocked
        self._last_error_time = last_error_time
        self._last_error_status_code = last_error_status_code
        self._config = config
        self._state =  state
        self._log_level = log_level
        self._meta_data = meta_data
        self._gateway_config = gateway_config

    @staticmethod
    def from_json(json):
        return Device(id= json['id'], name= json['name'], num_id= json['numId'],
                      credentials= json['credentials'], last_heartbeat_time= json['lastHeartbeatTime'],
                      last_event_time= json['lastEventTime'], last_state_time= json['lastStateTime'],
                      last_config_ack_time= json['lastConfigAckTime'], last_config_send_time= json['lastConfigSendTime'],
                      blocked= json['blocked'], last_error_time= json['lastErrorTime'],
                      last_error_status_code= json['lastErrorStatus'], config= json['config'],
                      state= json['state'], log_level= json['logLevel'], meta_data= json['metadata'],
                      gateway_config= json['gatewayConfig'])

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def num_id(self):
        return self._num_id

    @property
    def credentials(self):
        return self._credentials

    @property
    def last_error_status(self):
        return self._last_error_status_code

    @property
    def config(self):
        return self._config

    @property
    def state(self):
        return self._state

    @property
    def log_level(self):
        return self._log_level

    @property
    def meta_data(self):
        return self._meta_data

    @property
    def gateway_config(self):
        return self._gateway_config

    @property
    def log_level(self):
        return self._log_level

#classes to mock googles request & response

class Request():
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

class SendCommandToDeviceRequest(Request):
    def __init__(self, name: str = None,
                binary_data: bytes = None,
                subfolder: str = None) -> None:
        super().__init__(name)
        self._binary_data = binary_data
        self._subfolder = subfolder

    @property
    def binary_data(self):
        return self._binary_data

    @property
    def sub_folder(self):
        return self._subfolder

class CreateDeviceRequest(Request):
    def __init__(self, name: str = None,
                       device: Device = None) -> None:
        super().__init__(name)
        self._device = device

    @property
    def device(self):
        return self._device

class ModifyCloudToDeviceConfigRequest(Request):
    def __init__(self, name:str = None ,
                 version_to_update: int = -1,
                 binary_data: bytes = None) -> None:
        super().__init__(name)
        self._version_to_update = version_to_update
        self._binary_data = binary_data

    @property
    def version_to_update(self):
        return self._version_to_update

    @property
    def binary_data(self):
        return self._binary_data

class DeviceConfig(Request):
    def __init__(self, name,
                 version,
                 cloud_ack_time,
                 device_ack_time,
                 binary_data) -> None:
        super().__init__(name)
        self._version = version
        self._cloud_ack_time = cloud_ack_time
        self._device_ack_time = device_ack_time
        self._binary_data = binary_data

    def version(self):
        return self._version

    def cloud_ack_time(self):
        return self._cloud_ack_time

    def device_ack_time(self):
        return self._device_ack_time

    def binary_data(self):
        return self._binary_data

    @staticmethod
    def from_json(json):
        return DeviceConfig(version=json['version'], cloud_ack_time=json['cloudUpdateTime'],
                            device_ack_time=json['deviceAckTime'], binary_data=json['binaryData'])

class DeleteDeviceRequest(Request):
    def __init__(self, name: str = None) -> None:
        super().__init__(name)

class GetDeviceRequest(Request):
    def __init__(self, name: str = None) -> None:
        super().__init__(name)

class BindUnBindGatewayDeviceRequest(Request):
    def __init__(self, deviceId: str = None,
                       gatewayId: str = None) -> None:
        self._deviceid=deviceId
        self._gatewayid=gatewayId

    def deviceId(self):
        return self._deviceid

    def gatewayId(self):
        return self._gatewayid


class ClearBladeDeviceManager():

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

    def send_command(self,
                    request: SendCommandToDeviceRequest,
                    name: str = None,
                    binary_data: bytes = None,
                    subfolder: str = None):

        params, body = self._prepare_for_send_command(request, name, binary_data, subfolder)
        sync_client = SyncClient()
        return sync_client.post(request_params=params, request_body=body)

    async def send_command_async(self,
                                 request: SendCommandToDeviceRequest = None,
                                 name: str = None,
                                 binary_data: str = None,
                                 subfolder: str = None ):
        params, body = self._prepare_for_send_command(request, name, binary_data, subfolder)
        async_client = AsyncClient()
        return await async_client.post(request_params=params, request_body=body)

    def create(self, request: CreateDeviceRequest,
                     parent: str = None,
                     device: Device = None) -> Device:
        sync_client = SyncClient()
        body = self._create_device_body(request.device)
        response = sync_client.post(request_body=body)

        # return the device only if status code is 200
        # other wise return None
        if response.status_code is 200:
            return self._create_device_from_response(response.json())
        return None

    async def create_async(self, request: CreateDeviceRequest,
                           parent: str = None,
                           device: Device = None) -> Device:

        async_client = AsyncClient()
        body = self._create_device_body(request.device)
        response = await async_client.post(request_body=body)

        if response.status_code is 200:
            return self._create_device_from_response(response.json())
        return None

    def modify_cloud_device_config(self,
                                   request: ModifyCloudToDeviceConfigRequest,
                                   name:str = None,
                                   version_to_update : int = None,
                                   binary_data: bytes = None):
        sync_client = SyncClient()
        params, body = self._prepare_modify_cloud_config_device(request=request, name=name,
                                                                binary_data=binary_data, version_to_update=version_to_update)
        response = sync_client.post(request_params=params, request_body=body)
        if response.status_code is 200:
            return self._create_device_config(response.json)
        print("Error occurred , with status code {} respose text {}".format(response.status_code, response.text))
        return None

    async def modify_cloud_device_config_async(self,
                                        request: ModifyCloudToDeviceConfigRequest,
                                        name:str = None,
                                        version_to_update : int = None,
                                        binary_data: bytes = None):
        params, body = self._prepare_modify_cloud_config_device(request=request, name=name,
                                                                binary_data=binary_data, version_to_update=version_to_update)
        async_client = AsyncClient()
        response = await async_client.post(request_params=params, request_body=body)
        if response.status_code is 200:
            return self._create_device_config(response.json)
        print("Error occurred , with status code {} respose text {}".format(response.status_code, response.text))
        return None

    def list(self):
        pass

    def get(self,
            request: GetDeviceRequest) -> Device:
        sync_client = SyncClient()
        params = {'name':request.name}
        response = sync_client.get(request_params=params)
        
        if response.status_code is 200:
            return self._create_device_from_response(response.json())
        return None

    async def get_async(self,
            request: GetDeviceRequest):
        async_client = AsyncClient()
        params = {'name':request.name}
        response = await async_client.get(request_params=params)

        if response.status_code is 200:
            return self._create_device_from_response(response.json())
        return None

    def delete(self,
               request: DeleteDeviceRequest):
        sync_client = SyncClient()
        params = {'name':request.name}
        response = sync_client.delete(request_params=params)

        return response

    async def delete_async(self,
               request: DeleteDeviceRequest):
        async_client = AsyncClient()
        params = {'name':request.name}
        response = await async_client.delete(request_params=params)

        return response
    
    def bindGatewayToDevice(self, 
            request: BindUnBindGatewayDeviceRequest) :
        sync_client = SyncClient()
        body = {'deviceId':request.deviceId(), 'gatewayId':request.gatewayId()}
        params = {'method':'bindDeviceToGateway'}
        response = sync_client.post(request_params=params, request_body=body)

        return response

    async def bindGatewayToDevice_async(self, 
            request: BindUnBindGatewayDeviceRequest) :
        async_client = AsyncClient()
        body = {'deviceId':request.deviceId(), 'gatewayId':request.gatewayId()}
        params = {'method':'bindDeviceToGateway'}
        response = await async_client.post(request_params=params, request_body=body)

        return response

    def unbindGatewayFromDevice(self, 
            request: BindUnBindGatewayDeviceRequest) :
        sync_client = SyncClient()
        body = {'deviceId':request.deviceId(), 'gatewayId':request.gatewayId()}
        params = {'method':'unbindDeviceFromGateway'}
        response = sync_client.post(request_params=params, request_body=body)

        return response

    async def unbindGatewayFromDevice_async(self, 
            request: BindUnBindGatewayDeviceRequest) :
        async_client = AsyncClient()
        body = {'deviceId':request.deviceId(), 'gatewayId':request.gatewayId()}
        params = {'method':'unbindDeviceFromGateway'}
        response = await async_client.post(request_params=params, request_body=body)

        return response
