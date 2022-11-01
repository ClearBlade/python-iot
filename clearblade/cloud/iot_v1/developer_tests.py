from client import DeviceManagerClient
from devices import Device, SendCommandToDeviceRequest, CreateDeviceRequest 

def test_device_manager_client():
    client = DeviceManagerClient()
    request = SendCommandToDeviceRequest(name='python_1', binary_data=b'R2FyZ2l0ZXN0aW5n')
    response = client.send_command_to_device(request)
    print(response)

def test_create_device():
    client = DeviceManagerClient()
    device = Device(id="Python_9", name="Python_9")

    request = CreateDeviceRequest(device=device)
    response = client.create_device(request=request)
    print(response)

test_create_device()