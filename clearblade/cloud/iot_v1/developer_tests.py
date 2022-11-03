from client import DeviceManagerClient, DeviceManagerAsyncClient
from devices import SendCommandToDeviceRequest, CreateDeviceRequest, Device, ModifyCloudToDeviceConfigRequest
import asyncio

def test_send_command():
    client = DeviceManagerClient()
    request = SendCommandToDeviceRequest(name='python_1', binary_data=b'R2FyZ2l0ZXN0aW5n')
    response = client.send_command_to_device(request)
    print(response)

async def test_send_command_async():
    async_client = DeviceManagerAsyncClient()
    request = SendCommandToDeviceRequest(name='python_1', binary_data=b'R2FyZ2l0ZXN0aW5n')
    response = await async_client.send_command_to_device(request=request)
    print(response)

def test_create_device():
    client = DeviceManagerClient()
    device = Device(id="Python_10", name="Python_10")
    request = CreateDeviceRequest(device=device)
    response = client.create_device(request=request)
    print(response)

async def test_create_device_async():
    async_client = DeviceManagerAsyncClient()
    device = Device(id="Python_12", name="Python_12")
    request = CreateDeviceRequest(device=device)
    response = await async_client.create_device(request=request)
    print(response)

def test_modify_cloud_to_device_config():
    client =  DeviceManagerClient()
    modify_cloud_config_device_request = ModifyCloudToDeviceConfigRequest(name='python_1', binary_data=b'QUJD', version_to_update=1)
    response = client.modify_cloud_to_device_config(request=modify_cloud_config_device_request)
    print(response.text)

if __name__ ==  '__main__':
    #test_send_command()
    #asyncio.run(test_send_command_async())
    #test_create_device()
    #asyncio.run(test_create_device_async())
    test_modify_cloud_to_device_config()
