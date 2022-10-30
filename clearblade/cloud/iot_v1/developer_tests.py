from client import DeviceManagerClient
from request_response import SendCommandToDeviceRequest

def test_device_manager_client():
    client = DeviceManagerClient()
    request = SendCommandToDeviceRequest(name='python_1', binary_data=b'QUJD')
    response = client.send_command_to_device(request)
    print(response)

test_device_manager_client()