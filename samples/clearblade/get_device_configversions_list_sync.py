from clearblade.cloud import iot_v1

def sample_get_device_configversions_list():
    client = iot_v1.DeviceManagerClient()

    request = iot_v1.ListDeviceConfigVersionsRequest(name='Rashmi_Device_Test', numVersions=3)
    response = client.list_device_config_versions(request)
    print(response)
    