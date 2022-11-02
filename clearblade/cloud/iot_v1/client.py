from devices import SendCommandToDeviceRequest, CreateDeviceRequest, ClearBladeDeviceManager

class DeviceManagerClient():

    def send_command_to_device(self,request:SendCommandToDeviceRequest):
        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.send_command(request)

    def create_device(self, request):
        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.create(request=request)



class DeviceManagerAsyncClient():

    async def send_command_to_device(self, request:SendCommandToDeviceRequest):
        cb_device_manager = ClearBladeDeviceManager()
        return await cb_device_manager.send_command_async(request)