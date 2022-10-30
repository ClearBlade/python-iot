from devices import ClearBladeDeviceManager
from request_response import SendCommandToDeviceRequest

class DeviceManagerClient():
    def __init__(self) -> None:
        pass

    def send_command_to_device(self,request:SendCommandToDeviceRequest):
        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.send_command(request)
