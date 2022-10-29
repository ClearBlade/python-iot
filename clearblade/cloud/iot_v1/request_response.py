class SendCommandToDeviceRequest():
    def __init__(self, name, binary_data) -> None:
        self._name = name
        self._binary_data = binary_data

    @property
    def name(self):
        return self._name

    @property
    def binary_data(self):
        return self._binary_data

