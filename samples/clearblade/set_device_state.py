from clearblade.cloud import iot_v1

def sample_set_device_state():
    client = iot_v1.DeviceManagerClient()
    request = iot_v1.SetDeviceStateRequest(name='Rashmi_Registry_Test/Rashmi_Device_Test', binary_data=b'R2FyZ2l0ZXN0aW5n')
    response = client.set_device_state(request)
    print(response)