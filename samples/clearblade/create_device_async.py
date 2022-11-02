from clearblade.cloud import iot_v1

async def sample_send_command_to_device():
    client = iot_v1.DeviceManagerAsyncClient()

    device = iot_v1.Device(id="Python_12", name="Python_12")
    request = iot_v1.CreateDeviceRequest(device=device)

    response = await client.create_device(request)
