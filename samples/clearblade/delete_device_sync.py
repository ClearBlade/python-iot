from clearblade.cloud import iot_v1

async def sample_device_delete():
    client = iot_v1.DeviceManagerClient()

    request = iot_v1.DeleteDeviceRequest(name='Python_12')

    response = await client.delete_device(request)