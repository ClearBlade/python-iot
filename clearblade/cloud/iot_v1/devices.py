from request_response import SendCommandToDeviceRequest
from http_client import HttpClient

class ClearBladeDevice():
    def __init__(self) -> None:
        pass

    def send_command(self, request: SendCommandToDeviceRequest):
        client = HttpClient()
        params = {'name':request.name,'method':'sendCommandToDevice'}
        body = {'binaryData':request.binary_data}
        return client.post(request_params=params, request_body=body)

    def list(self):
        pass
    
    def get(self):
        pass

    def delete(self):
        pass