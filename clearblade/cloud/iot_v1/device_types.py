from .utils import get_value
from typing import List

class Device():
    r"""The device resource.

    Attributes:
        id (str):
            The user-defined device identifier. The
            device ID must be unique within a device
            registry.
        name (str):
            The resource path name. For example,
            ``projects/p1/locations/us-central1/registries/registry0/devices/dev0``
            or
            ``projects/p1/locations/us-central1/registries/registry0/devices/{num_id}``.
            When ``name`` is populated as a response from the service,
            it always ends in the device numeric ID.
        num_id (int):
            [Output only] A server-defined unique numeric ID for the
            device. This is a more compact way to identify devices, and
            it is globally unique.
        credentials (Sequence):
            The credentials used to authenticate this device. To allow
            credential rotation without interruption, multiple device
            credentials can be bound to this device. No more than 3
            credentials can be bound to a single device at a time. When
            new credentials are added to a device, they are verified
            against the registry credentials. For details, see the
            description of the ``DeviceRegistry.credentials`` field.
        last_heartbeat_time (str):
            [Output only] The last time an MQTT ``PINGREQ`` was
            received. This field applies only to devices connecting
            through MQTT. MQTT clients usually only send ``PINGREQ``
            messages if the connection is idle, and no other messages
            have been sent. Timestamps are periodically collected and
            written to storage; they may be stale by a few minutes.
        last_event_time (str):
            [Output only] The last time a telemetry event was received.
            Timestamps are periodically collected and written to
            storage; they may be stale by a few minutes.
        last_state_time (str):
            [Output only] The last time a state event was received.
            Timestamps are periodically collected and written to
            storage; they may be stale by a few minutes.
        last_config_ack_time (str):
            [Output only] The last time a cloud-to-device config version
            acknowledgment was received from the device. This field is
            only for configurations sent through MQTT.
        last_config_send_time (str):
            [Output only] The last time a cloud-to-device config version
            was sent to the device.
        blocked (bool):
            If a device is blocked, connections or
            requests from this device will fail. Can be used
            to temporarily prevent the device from
            connecting if, for example, the sensor is
            generating bad data and needs maintenance.
        last_error_time (str):
            [Output only] The time the most recent error occurred, such
            as a failure to publish to Cloud Pub/Sub. This field is the
            timestamp of 'last_error_status'.
        last_error_status (str):
            [Output only] The error message of the most recent error,
            such as a failure to publish to Cloud Pub/Sub.
            'last_error_time' is the timestamp of this field. If no
            errors have occurred, this field has an empty message and
            the status code 0 == OK. Otherwise, this field is expected
            to have a status code other than OK.
        config (clearblade.cloud.iot_v1.device_types.DeviceConfig):
            The most recent device configuration, which is eventually
            sent from Cloud IoT Core to the device. If not present on
            creation, the configuration will be initialized with an
            empty payload and version value of ``1``. To update this
            field after creation, use the
            ``DeviceManager.ModifyCloudToDeviceConfig`` method.
        state (clearblade.cloud.iot_v1.device_types.DeviceState):
            [Output only] The state most recently received from the
            device. If no state has been reported, this field is not
            present.
        log_level (google.cloud.iot_v1.types.LogLevel):
            **Beta Feature**

            The logging verbosity for device activity. If unspecified,
            DeviceRegistry.log_level will be used.
        metadata (Mapping[str, str]):
            The metadata key-value pairs assigned to the device. This
            metadata is not interpreted or indexed by Cloud IoT Core. It
            can be used to add contextual information for the device.

            Keys must conform to the regular expression
            [a-zA-Z][a-zA-Z0-9-_.+~%]+ and be less than 128 bytes in
            length.

            Values are free-form strings. Each value must be less than
            or equal to 32 KB in size.

            The total size of all keys and values must be less than 256
            KB, and the maximum number of key-value pairs is 500.
        gateway_config (google.cloud.iot_v1.types.GatewayConfig):
            Gateway-related configuration and state.
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
        device_state:DeviceState = DeviceState.from_json(get_value(json,'state'))
        device_config:DeviceConfig = DeviceConfig.from_json(get_value(json, 'config'))
        return Device(id= json['id'], name= json['name'], num_id= json['numId'],
                      credentials= json['credentials'], last_heartbeat_time= json['lastHeartbeatTime'],
                      last_event_time= json['lastEventTime'], last_state_time= json['lastStateTime'],
                      last_config_ack_time= json['lastConfigAckTime'], last_config_send_time= json['lastConfigSendTime'],
                      blocked= json['blocked'], last_error_time= json['lastErrorTime'],
                      last_error_status_code= json['lastErrorStatus'], config= device_config,
                      state= device_state, log_level= json['logLevel'], meta_data= json['metadata'],
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

class DeviceState():
    def __init__(self, updated_time: str =None, binary_data:str = None) -> None:
        self._updated_time = updated_time
        self._binary_data = binary_data

    @property
    def updated_time(self):
        return self._updated_time

    @property
    def binary_data(self):
        return self._binary_data

    @staticmethod
    def from_json(response_json):
        return DeviceState(updated_time=get_value(response_json, 'updateTime'),
                           binary_data=get_value(response_json, 'binaryData'))

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
                 version_to_update: str = "",
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

    @property
    def version(self):
        return self._version

    @property
    def cloud_ack_time(self):
        return self._cloud_ack_time

    @property
    def device_ack_time(self):
        return self._device_ack_time

    @property
    def binary_data(self):
        return self._binary_data

    @staticmethod
    def from_json(json):
        return DeviceConfig(name='',
                            version=get_value(json, 'version'),
                            cloud_ack_time=get_value(json,'cloudUpdateTime'),
                            device_ack_time=get_value(json, 'deviceAckTime'),
                            binary_data=get_value(json,'binaryData'))

class DeleteDeviceRequest(Request):
    def __init__(self, name: str = None) -> None:
        super().__init__(name)

class GetDeviceRequest(Request):
    def __init__(self, name: str = None) -> None:
        super().__init__(name)

class BindUnBindGatewayDeviceRequest(Request):
    def __init__(self, parent:str = None,
                 deviceId: str = None,
                 gatewayId: str = None) -> None:
        self._parent = parent
        self._deviceid=deviceId
        self._gatewayid=gatewayId

    @property
    def parent(self):
        return self._parent

    @property
    def deviceId(self):
        return self._deviceid

    @property
    def gatewayId(self):
        return self._gatewayid

class BindDeviceToGatewayRequest(BindUnBindGatewayDeviceRequest):
    def __init__(self, parent: str = None,
                 deviceId: str = None,
                 gatewayId: str = None) -> None:
        super().__init__(parent, deviceId, gatewayId)

class UnbindDeviceFromGatewayRequest(BindUnBindGatewayDeviceRequest):
    def __init__(self, parent: str = None,
                 deviceId: str = None,
                 gatewayId: str = None) -> None:
        super().__init__(parent, deviceId, gatewayId)

class ListDeviceStatesRequest(Request):
    def __init__(self, name: str = None,
                num_states: int = None) -> None:
        super().__init__(name)
        self._num_states = num_states

    @property
    def num_states(self):
        return self._num_states

class ListDeviceStatesResponse():
    def __init__(self, device_states:List[DeviceState] = []) -> None:
        self._device_states = device_states

    @property
    def device_states(self):
        return self._device_states

    @staticmethod
    def from_json(response_json):
        device_states_json = get_value(response_json, 'deviceStates')
        device_states = []
        for device_state_json in device_states_json:
            device_state = DeviceState.from_json(device_state_json)
            device_states.append(device_state)

        return ListDeviceStatesResponse(device_states=device_states)



class ListDeviceConfigVersionsRequest(Request):
    def __init__(self, name: str = None,
                numVersions: int = None) -> None:
        super().__init__(name)
        self._numversions = numVersions

    @property
    def numVersions(self):
        return self._numversions

class ListDeviceConfigVersionsResponse():
    def __init__(self, device_configs) -> None:
        self._device_configs = device_configs

    @property
    def device_configs(self):
        return self._device_configs

    @staticmethod
    def from_json(response_json):
        device_configs_json = response_json['deviceConfigs']
        deviceConfigs = []
        for device_config_json in device_configs_json:
            deviceConfig = DeviceConfig.from_json(device_config_json)
            deviceConfigs.append(deviceConfig)

        return ListDeviceConfigVersionsResponse(device_configs=deviceConfigs)

class UpdateDeviceRequest(Request):
    def __init__(self, id: str = None, name: str = None, numId: str=None,
                 credentials: list=None, blocked: bool = None,
                 logLevel: str = None, metadata: dict = None, gatewayConfig : dict = None,
                 updateMask: str = None) -> None:
        self._id = id
        self._name = name
        self._num_id = numId
        self._credentials = credentials
        self._blocked = blocked
        self._log_level = logLevel
        self._meta_data = metadata
        self._gateway_config = gatewayConfig
        self._update_mask = updateMask

    def _prepare_params_body_for_update(self):
        params = {'name': self._name}
        if self._update_mask is not None:
            params['updateMask'] = self._update_mask

        body = {}
        if self._id is not None:
            body['id'] = self._id
        if self._name is not None:
            body['name'] = self._name
        if self._log_level is not None:
            body['logLevel'] = self._log_level
        if self._gateway_config is not None:
            body['gatewayConfig'] = self._gateway_config
        if self._meta_data is not None:
            body['metadata'] = self._meta_data
        if self._blocked is not None:
            body['blocked'] = self._blocked
        if self._credentials is not None:
            body['credentials'] = self._credentials

        return params, body

class ListDevicesRequest(Request):
    def __init__(self, parent:str = None ,
                 deviceNumIds: str = None,
                 deviceIds: str = None,
                 fieldMask: str = None,
                 gatewayListOptions: dict = None,
                 pageSize: int = None,
                 pageToken: str = None) -> None:
        self._parent = parent
        self._device_num_ids = deviceNumIds
        self._device_ids = deviceIds
        self._field_mask = fieldMask
        self._gateway_list_options = gatewayListOptions
        self._page_size = pageSize
        self._page_token = pageToken

    @property
    def parent(self):
        return self._parent

    @property
    def device_num_ids(self):
        return self._device_num_ids

    @property
    def device_ids(self):
        return self._device_ids

    @property
    def field_mask(self):
        return self._field_mask

    @property
    def gateway_list_options(self):
        return self._gateway_list_options

    @property
    def page_size(self):
        return self._page_size

    @property
    def page_token(self):
        return self._page_token

    @page_token.setter
    def page_token(self, page_token):
        self._page_token = page_token

    def _prepare_params_for_list(self):
        params = {'parent':self.parent}
        if self.page_size:
            params['pageSize'] = self.page_size
        if self.device_num_ids:
            params['deviceNumIds'] = self.device_num_ids
        if self.device_ids:
            params['deviceIds'] = self.device_ids
        if self.field_mask:
            params['fieldMask'] = self.field_mask
        if self.gateway_list_options :
            params['gatewayListOptions'] = self.gateway_list_options
        if self.page_token:
            params['pageToken'] = self.page_token

        return params

class ListDevicesResponse():

    def __init__(self, devices, next_page_token) -> None:
        self._devices = devices
        self._next_page_token = next_page_token

    @property
    def raw_pages(self):
        return self

    @property
    def devices(self):
        return self._devices

    @property
    def next_page_token(self):
        return self._next_page_token

    @staticmethod
    def from_json(devices_list_json):
        devices = []
        next_page_token = None
        if 'devices' in devices_list_json:
            devices_json = devices_list_json['devices']
            for device_json in devices_json:
                device = Device.from_json(device_json)
                devices.append(device)

        if 'nextPageToken' in devices_list_json:
            next_page_token = devices_list_json['nextPageToken']

        return ListDevicesResponse(devices=devices, next_page_token=next_page_token)

