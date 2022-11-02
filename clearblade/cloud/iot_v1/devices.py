from http_client import SyncClient, AsyncClient

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
    def __init__(self, name: str = None,
                binary_data: bytes = None,
                subfolder: str = None) -> None:
        self._name = name
        self._binary_data = binary_data
        self._subfolder = subfolder

    @property
    def name(self):
        return self._name

    @property
    def binary_data(self):
        return self._binary_data

    @property
    def sub_folder(self):
        return self._subfolder

class ClearBladeDeviceManager():

    def _prepare_for_send_command(self,
                                  request: SendCommandToDeviceRequest,
                                  name: str = None,
                                  binary_data: bytes = None,
                                  subfolder: str = None):
        has_flattened_params = any([name, binary_data, subfolder])
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
        response = await async_client.post(request_params=params, request_body=body)
        print(response)

    def create(self):
        pass

    def list(self):
        pass

    def get(self):
        pass

    def delete(self):
        pass
