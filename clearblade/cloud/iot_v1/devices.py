from http_client import SyncClient

class Device():
    """
    Data class for Clearblade Device
    """
    def __init__(self) -> None:
        self._id = None
        self._name = None
        self._num_id = None
        self._state = {"updateTime":None, "binaryData":None}

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

#classes to mock googles request & response
class SendCommandToDeviceRequest():
    def __init__(self, name, binary_data) -> None:
        self._name = name
        self._binary_data = binary_data

    @property
    def name(self):
        return self._name

    @property
    def binary_data(self):
        return self._binary_data

class ClearBladeDeviceManager():

    def send_command(self, request: SendCommandToDeviceRequest):
        sync_client = SyncClient()
        params = {'name':request.name,'method':'sendCommandToDevice'}
        body = {'binaryData':request.binary_data.decode("utf-8")}
        return sync_client.post(request_params=params, request_body=body)

    def create(self):
        pass

    def list(self):
        pass
    
    def get(self):
        pass

    def delete(self):
        pass
