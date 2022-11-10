from client import DeviceManagerClient, DeviceManagerAsyncClient
from devices import SendCommandToDeviceRequest, CreateDeviceRequest, Device, ModifyCloudToDeviceConfigRequest, DeleteDeviceRequest, GetDeviceRequest, BindUnBindGatewayDeviceRequest, SetDeviceStateRequest
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
    print(response)

async def test_modify_cloud_to_device_config_async():
    async_client =  DeviceManagerAsyncClient()
    modify_cloud_config_device_request = ModifyCloudToDeviceConfigRequest(name='Python_101', binary_data=b'QUJD', version_to_update=2)
    response = await async_client.modify_cloud_to_device_config(request=modify_cloud_config_device_request)
    print(response)

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
    get_device_request = GetDeviceRequest(name='Python_101')
    response = await async_client.get_device(request=get_device_request)
    print(response)

def test_bind_gateway_device():
    client =  DeviceManagerClient()
    bind_device_request = BindUnBindGatewayDeviceRequest(deviceId='Python_101',gatewayId='gateway1')
    response = client.bind_device_to_gateway(request=bind_device_request)
    print(response)

async def test_bind_gateway_device_async():
    async_client =  DeviceManagerAsyncClient()
    bind_device_request = BindUnBindGatewayDeviceRequest(deviceId='mandar_device',gatewayId='gateway1')
    response = await async_client.bind_device_to_gateway(request=bind_device_request)
    print(response)

def test_unbind_gateway_device():
    client =  DeviceManagerClient()
    bind_device_request = BindUnBindGatewayDeviceRequest(deviceId='Python_101',gatewayId='gateway1')
    response = client.unbind_device_from_gateway(request=bind_device_request)
    print(response)

async def test_unbind_gateway_device_async():
    async_client =  DeviceManagerAsyncClient()
    bind_device_request = BindUnBindGatewayDeviceRequest(deviceId='mandar_device',gatewayId='gateway1')
    response = await async_client.unbind_device_from_gateway(request=bind_device_request)
    print(response)

def test_set_state():
    client = DeviceManagerClient()
    request = SetDeviceStateRequest(name='Rashmi_Registry_Test/Rashmi_Device_Test', binary_data=b'R2FyZ2l0ZXN0aW5n')
    response = client.set_device_state(request)
    print(response)

async def test_set_state_async():
    async_client = DeviceManagerAsyncClient()
    request = SetDeviceStateRequest(name='Rashmi_Registry_Test/Rashmi_Device_Test', binary_data=b'c3RhdGV0ZXN0')
    response = await async_client.set_device_state(request=request)
    print(response)


if __name__ ==  '__main__':
    #test_send_command()
    #asyncio.run(test_send_command_async())
    #test_create_device()
    #asyncio.run(test_create_device_async())
    #test_modify_cloud_to_device_config()
    #asyncio.run(test_modify_cloud_to_device_config_async())
    #test_delete_device()
    #asyncio.run(test_delete_device_async())
    #test_get_device()
    #asyncio.run(test_get_device_async())
    #test_bind_gateway_device()
    #asyncio.run(test_bind_gateway_device_async())
    #test_unbind_gateway_device()
    #asyncio.run(test_unbind_gateway_device_async())
    #test_set_state()
    asyncio.run(test_set_state_async())
