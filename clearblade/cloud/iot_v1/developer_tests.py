from client import DeviceManagerClient, DeviceManagerAsyncClient
from devices import SendCommandToDeviceRequest, CreateDeviceRequest, Device, ModifyCloudToDeviceConfigRequest, DeleteDeviceRequest, GetDeviceRequest
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
    device = Device(id="Python_101", name="Python_101")
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

def test_delete_device():
    client =  DeviceManagerClient()
    delete_device_request = DeleteDeviceRequest(name='Python_12')
    response = client.delete_device(request=delete_device_request)
    print(response)

async def test_delete_device_async():
    async_client =  DeviceManagerAsyncClient()
    delete_device_request = DeleteDeviceRequest(name='Python_10')
    response = await async_client.delete_device(request=delete_device_request)
    print(response)

def test_get_device():
    client =  DeviceManagerClient()
    get_device_request = GetDeviceRequest(name='Python_101')
    response = client.get_device(request=get_device_request)
    print(response)

async def test_get_device_async():
    async_client =  DeviceManagerAsyncClient()
    get_device_request = GetDeviceRequest(name='Python_10')
    response = await async_client.get_device(request=get_device_request)
    print(response)

if __name__ ==  '__main__':
    #test_send_command()
    #asyncio.run(test_send_command_async())
    #test_create_device()
    #asyncio.run(test_create_device_async())
    #test_modify_cloud_to_device_config()
    #test_delete_device()
    #asyncio.run(test_delete_device_async())
    test_get_device()
    #asyncio.run(test_get_device_async())
