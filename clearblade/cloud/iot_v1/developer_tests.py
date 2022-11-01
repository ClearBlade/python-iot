from client import DeviceManagerClient
from devices import SendCommandToDeviceRequest

def test_device_manager_client():
    client = DeviceManagerClient()
    request = SendCommandToDeviceRequest(name='Rashmi_Device_Test', binary_data=b'R2FyZ2l0ZXN0aW5n')
    response = client.send_command_to_device(request)
    print(response)

test_device_manager_client()