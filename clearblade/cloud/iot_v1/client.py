from devices import ClearBladeDevice
from request_response import SendCommandToDeviceRequest

class DeviceManagerClient():
    def __init__(self) -> None:
        pass

    def send_command_to_device(self,request:SendCommandToDeviceRequest):
        cb_device = ClearBladeDevice()
        return cb_device.send_command(request)

