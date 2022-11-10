from clearblade.cloud import iot_v1

async def sample_get_device_configversions_list_async():
    async_client = iot_v1.DeviceManagerAsyncClient()

    request = iot_v1.GetDeviceConfigVersionsList(name='Rashmi_Device_Test', numVersions=3)
    response = await async_client.list_device_config_versions(request)
    