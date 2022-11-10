from clearblade.cloud import iot_v1

async def sample_set_device_async():
    async_client = iot_v1.DeviceManagerAsyncClient()
    request = iot_v1.SetDeviceStateRequest(name='Rashmi_Registry_Test/Rashmi_Device_Test', binary_data=b'c3RhdGV0ZXN0')
    response = await async_client.set_device_state(request=request)
    print(response)