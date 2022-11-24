from .devices import *
from .registry import *
from .device_types import *
from .registry_types import *

class DeviceManagerClient():

    def send_command_to_device(self,
                               request:SendCommandToDeviceRequest,
                               name:str = None,
                               binary_data:bytes = None,
                               subfolder:str = None):
        r"""Sends a command to the specified device. In order for a device
        to be able to receive commands, it must:

        1) be connected to Cloud IoT Core using the MQTT protocol, and
        2) be subscribed to the group of MQTT topics specified by
           /devices/{device-id}/commands/#. This subscription will
           receive commands at the top-level topic
           /devices/{device-id}/commands as well as commands for
           subfolders, like /devices/{device-id}/commands/subfolder.
           Note that subscribing to specific subfolders is not
           supported. If the command could not be delivered to the
           device, this method will return an error; in particular, if
           the device is not subscribed, this method will return
           FAILED_PRECONDITION. Otherwise, this method will return OK.
           If the subscription is QoS 1, at least once delivery will be
           guaranteed; for QoS 0, no acknowledgment will be expected
           from the device.

        .. code-block:: python

            from clearblade.cloud import iot_v1

            def sample_send_command_to_device():
                # Create a client
                client = iot_v1.DeviceManagerClient()

                # Initialize request argument(s)
                request = iot_v1.SendCommandToDeviceRequest(
                    name="name_value",
                    binary_data=b'binary_data_blob',
                )

                # Make the request
                response = client.send_command_to_device(request=request)

                # Handle the response
                print(response)

        Args:
            request (clearblade.cloud.iot_v1.device_types.SendCommandToDeviceRequest):
                The request object. Request for `SendCommandToDevice`.
            name (str):
                Required. The name of the device. For example,
                ``projects/p0/locations/us-central1/registries/registry0/devices/device0``
                or
                ``projects/p0/locations/us-central1/registries/registry0/devices/{num_id}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            binary_data (bytes):
                Required. The command data to send to
                the device.

                This corresponds to the ``binary_data`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            subfolder (str):
                Optional subfolder for the command.
                If empty, the command will be delivered
                to the /devices/{device-id}/commands
                topic, otherwise it will be delivered to
                the
                /devices/{device-id}/commands/{subfolder}
                topic. Multi-level subfolders are
                allowed. This field must not have more
                than 256 characters, and must not
                contain any MQTT wildcards ("+" or "#")
                or null characters.

                This corresponds to the ``subfolder`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

        Returns:
            clearblade.cloud.iot_v1.device_types.SendCommandToDeviceResponse:
                Response for SendCommandToDevice.
        """

        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.send_command(request=request,
                                              name=name,
                                              binary_data=binary_data,
                                              ssubfolder=subfolder)

    def create_device(self,
                      request:CreateDeviceRequest,
                      parent:str = None,
                      device:Device= None)->Device:
        r"""Creates a device in a device registry.

        .. code-block:: python

            from clearblade.cloud import iot_v1

            async def sample_create_device():
                # Create a client
                client = iot_v1.DeviceManagerAsyncClient()

                # Initialize request argument(s)
                request = iot_v1.CreateDeviceRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_device(request=request)

                # Handle the response
                print(response)

        Args:
            request (clearblade.cloud.iot_v1.device_types.CreateDeviceRequest):
                The request object. Request for `CreateDevice`.
            parent (:class:`str`):
                Required. The name of the device registry where this
                device should be created. For example,
                ``projects/example-project/locations/us-central1/registries/my-registry``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            device (:class:`clearblade.cloud.iot_v1.device_types.Device`):
                Required. The device registration details. The field
                ``name`` must be empty. The server generates ``name``
                from the device registry ``id`` and the ``parent``
                field.

                This corresponds to the ``device`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
        Returns:
            clearblade.cloud.iot_v1.device_types.Device:
                The device resource.
        """
        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.create(request=request,
                                        parent=parent,
                                        device=device)

    def modify_cloud_to_device_config(self, request: ModifyCloudToDeviceConfigRequest,
                                      name: str = None,
                                      version_to_update = "",
                                      binary_data:bytes = None) -> DeviceConfig:
        r"""Modifies the configuration for the device, which is
        eventually sent from the Cloud IoT Core servers. Returns
        the modified configuration version and its metadata.

        .. code-block:: python

            def sample_modify_cloud_to_device_config():
                # Create a client
                client = iot_v1.DeviceManagerClient()

                # Initialize request argument(s)
                request = iot_v1.ModifyCloudToDeviceConfigRequest(
                    name="name_value",
                    binary_data=b'binary_data_blob',
                )

                # Make the request
                response = client.modify_cloud_to_device_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (clearblade.cloud.iot_v1.device_types.ModifyCloudToDeviceConfigRequest):
                The request object. Request for
                `ModifyCloudToDeviceConfig`.
            name (str):
                Required. The name of the device. For example,
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            binary_data (bytes):
                Required. The configuration data for
                the device.

                This corresponds to the ``binary_data`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

        Returns:
            clearblade.cloud.iot_v1.device_types.DeviceConfig:
                The device configuration. Eventually
                delivered to devices.

        """

        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.modify_cloud_device_config(request=request,
                                                            name=name,
                                                            version_to_update=version_to_update,
                                                            binary_data=binary_data)

    def delete_device(self, request):
        r"""Deletes a device.

        .. code-block:: python

            from clearblade.cloud import iot_v1

            def sample_delete_device():
                # Create a client
                client = iot_v1.DeviceManagerClient()

                # Initialize request argument(s)
                request = iot_v1.DeleteDeviceRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_device(request=request)

        Args:
            request (clearblade.cloud.iot_v1.device_types.DeleteDeviceRequest, dict):
                The request object. Request for `DeleteDevice`.
        """
        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.delete(request=request)

    def get_device(self, request) -> Device:
        r"""Gets details about a device.

        .. code-block:: python

            from clearblade.cloud import iot_v1

            def sample_get_device():
                # Create a client
                client = iot_v1.DeviceManagerClient()

                # Initialize request argument(s)
                request = iot_v1.GetDeviceRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_device(request=request)

                # Handle the response
                print(response)

        Args:
            request (clearblade.cloud.iot_v1.device_types.GetDeviceRequest):
                The request object. Request for `GetDevice`.

        Returns:
            clearblade.cloud.iot_v1.device_types.Device:
                The device resource.
        """

        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.get(request=request)

    def bind_device_to_gateway(self, request : BindDeviceToGatewayRequest):
        r"""Associates the device with the gateway.

        .. code-block:: python

            from clearblade.cloud import iot_v1

            def sample_bind_device_to_gateway():
                # Create a client
                client = iot_v1.DeviceManagerClient()

                # Initialize request argument(s)
                request = iot_v1.BindDeviceToGatewayRequest(
                    parent="parent_value",
                    gateway_id="gateway_id_value",
                    device_id="device_id_value",
                )

                # Make the request
                response = client.bind_device_to_gateway(request=request)

                # Handle the response
                print(response)

        Args:
            request (clearblade.cloud.iot_v1.device_types.BindDeviceToGatewayRequest):
                The request object. Request for `BindDeviceToGateway`.

        Returns:
            clearblade.cloud.iot_v1.device_types.BindDeviceToGatewayResponse:
                Response for BindDeviceToGateway.
        """

        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.bindGatewayToDevice(request=request)

    def unbind_device_from_gateway(self, request : UnbindDeviceFromGatewayRequest):
        r"""Deletes the association between the device and the
        gateway.

        .. code-block:: python

            def sample_unbind_device_from_gateway():
                # Create a client
                client = iot_v1.DeviceManagerClient()

                # Initialize request argument(s)
                request = iot_v1.UnbindDeviceFromGatewayRequest(
                    parent="parent_value",
                    gateway_id="gateway_id_value",
                    device_id="device_id_value",
                )

                # Make the request
                response = client.unbind_device_from_gateway(request=request)

                # Handle the response
                print(response)

        Args:
            request (clearblade.cloud.iot_v1.device_types.UnbindDeviceFromGatewayRequest):
                The request object. Request for
                `UnbindDeviceFromGateway`.
        """

        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.unbindGatewayFromDevice(request=request)

    def list_device_states(self, request : ListDeviceStatesRequest):
        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.states_list(request=request)

    def list_device_config_versions(self, request : ListDeviceConfigVersionsRequest):
        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.config_versions_list(request=request)

    def list_devices(self, request : ListDevicesRequest):
        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.list(request=request)

    def update_device(self, request : UpdateDeviceRequest):
        cb_device_manager = ClearBladeDeviceManager()
        return cb_device_manager.update(request=request)

    def list_device_registries(self, request: ListDeviceRegistriesRequest):
        cb_registry_manager = ClearBladeRegistryManager()
        return cb_registry_manager.list(request=request)

    def get_device_registry(self, request=GetDeviceRegistryRequest):
        cb_registry_manager = ClearBladeRegistryManager()
        return cb_registry_manager.get(request=request)

    def create_device_registry(self, request=CreateDeviceRegistryRequest):
        cb_registry_manager = ClearBladeRegistryManager()
        return cb_registry_manager.create(request=request)

    def delete_device_registry(self, request=DeleteDeviceRegistryRequest):
        cb_registry_manager = ClearBladeRegistryManager()
        return cb_registry_manager.delete(request=request)

    def update_device_registry(self, request=UpdateDeviceRegistryRequest):
        cb_registry_manager = ClearBladeRegistryManager()
        return cb_registry_manager.patch(request=request)

class DeviceManagerAsyncClient():

    async def send_command_to_device(self,
                                     request:SendCommandToDeviceRequest,
                                     name:str = None,
                                     binary_data:bytes = None,
                                     subfolder:str = None):
        r"""Sends a command to the specified device. In order for a device
        to be able to receive commands, it must:

        1) be connected to Cloud IoT Core using the MQTT protocol, and
        2) be subscribed to the group of MQTT topics specified by
           /devices/{device-id}/commands/#. This subscription will
           receive commands at the top-level topic
           /devices/{device-id}/commands as well as commands for
           subfolders, like /devices/{device-id}/commands/subfolder.
           Note that subscribing to specific subfolders is not
           supported. If the command could not be delivered to the
           device, this method will return an error; in particular, if
           the device is not subscribed, this method will return
           FAILED_PRECONDITION. Otherwise, this method will return OK.
           If the subscription is QoS 1, at least once delivery will be
           guaranteed; for QoS 0, no acknowledgment will be expected
           from the device.

        .. code-block:: python

            from clearblade.cloud import iot_v1

            def sample_send_command_to_device():
                # Create a client
                client = iot_v1.DeviceManagerClient()

                # Initialize request argument(s)
                request = iot_v1.SendCommandToDeviceRequest(
                    name="name_value",
                    binary_data=b'binary_data_blob',
                )

                # Make the request
                response = client.send_command_to_device(request=request)

                # Handle the response
                print(response)

        Args:
            request (clearblade.cloud.iot_v1.device_types.SendCommandToDeviceRequest):
                The request object. Request for `SendCommandToDevice`.
            name (str):
                Required. The name of the device. For example,
                ``projects/p0/locations/us-central1/registries/registry0/devices/device0``
                or
                ``projects/p0/locations/us-central1/registries/registry0/devices/{num_id}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            binary_data (bytes):
                Required. The command data to send to
                the device.

                This corresponds to the ``binary_data`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            subfolder (str):
                Optional subfolder for the command.
                If empty, the command will be delivered
                to the /devices/{device-id}/commands
                topic, otherwise it will be delivered to
                the
                /devices/{device-id}/commands/{subfolder}
                topic. Multi-level subfolders are
                allowed. This field must not have more
                than 256 characters, and must not
                contain any MQTT wildcards ("+" or "#")
                or null characters.

                This corresponds to the ``subfolder`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

        Returns:
            clearblade.cloud.iot_v1.device_types.SendCommandToDeviceResponse:
                Response for SendCommandToDevice.
        """
        cb_device_manager = ClearBladeDeviceManager()
        return await cb_device_manager.send_command_async(request=request,
                                                          name=name,
                                                          binary_data=binary_data,
                                                          subfolder=subfolder)

    async def create_device(self,
                            request:CreateDeviceRequest,
                            parent:str = None,
                            device:Device= None)->Device:
        r"""Creates a device in a device registry.

        .. code-block:: python

            from clearblade.cloud import iot_v1

            async def sample_create_device():
                # Create a client
                client = iot_v1.DeviceManagerAsyncClient()

                # Initialize request argument(s)
                request = iot_v1.CreateDeviceRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_device(request=request)

                # Handle the response
                print(response)

        Args:
            request (clearblade.cloud.iot_v1.device_types.CreateDeviceRequest):
                The request object. Request for `CreateDevice`.
            parent (:class:`str`):
                Required. The name of the device registry where this
                device should be created. For example,
                ``projects/example-project/locations/us-central1/registries/my-registry``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            device (:class:`clearblade.cloud.iot_v1.device_types.Device`):
                Required. The device registration details. The field
                ``name`` must be empty. The server generates ``name``
                from the device registry ``id`` and the ``parent``
                field.

                This corresponds to the ``device`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
        Returns:
            clearblade.cloud.iot_v1.device_types.Device:
                The device resource.
        """

        cb_device_manager = ClearBladeDeviceManager()
        return await cb_device_manager.create_async(request=request, parent=parent, device=device)

    async def modify_cloud_to_device_config(self, request: ModifyCloudToDeviceConfigRequest,
                                            name: str = None,
                                            version_to_update = "",
                                            binary_data:bytes = None):
        r"""Modifies the configuration for the device, which is
        eventually sent from the Cloud IoT Core servers. Returns
        the modified configuration version and its metadata.

        .. code-block:: python

            def sample_modify_cloud_to_device_config():
                # Create a client
                client = iot_v1.DeviceManagerClient()

                # Initialize request argument(s)
                request = iot_v1.ModifyCloudToDeviceConfigRequest(
                    name="name_value",
                    binary_data=b'binary_data_blob',
                )

                # Make the request
                response = client.modify_cloud_to_device_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (clearblade.cloud.iot_v1.device_types.ModifyCloudToDeviceConfigRequest):
                The request object. Request for
                `ModifyCloudToDeviceConfig`.
            name (str):
                Required. The name of the device. For example,
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            binary_data (bytes):
                Required. The configuration data for
                the device.

                This corresponds to the ``binary_data`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

        Returns:
            clearblade.cloud.iot_v1.device_types.DeviceConfig:
                The device configuration. Eventually
                delivered to devices.

        """

        cb_device_manager = ClearBladeDeviceManager()
        return await cb_device_manager.modify_cloud_device_config_async(request=request,
                                                            name=name,
                                                            version_to_update=version_to_update,
                                                            binary_data=binary_data)

    async def delete_device(self, request):
        r"""Deletes a device.

            from clearblade.cloud import iot_v1

            def sample_delete_device():
                # Create a client
                client = iot_v1.DeviceManagerClient()

                # Initialize request argument(s)
                request = iot_v1.DeleteDeviceRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_device(request=request)

        Args:
            request (clearblade.cloud.iot_v1.device_types.DeleteDeviceRequest):
                The request object. Request for `DeleteDevice`.
        """

        cb_device_manager = ClearBladeDeviceManager()
        return await cb_device_manager.delete_async(request=request)

    async def get_device(self, request) -> Device:
        r"""Gets details about a device.

        .. code-block:: python

            from clearblade.cloud import iot_v1

            def sample_get_device():
                # Create a client
                client = iot_v1.DeviceManagerClient()

                # Initialize request argument(s)
                request = iot_v1.GetDeviceRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_device(request=request)

                # Handle the response
                print(response)

        Args:
            request (clearblade.cloud.iot_v1.device_types.GetDeviceRequest):
                The request object. Request for `GetDevice`.

        Returns:
            clearblade.cloud.iot_v1.device_types.Device:
                The device resource.
        """

        cb_device_manager = ClearBladeDeviceManager()
        return await cb_device_manager.get_async(request=request)

    async def bind_device_to_gateway(self, request : BindDeviceToGatewayRequest):
        r"""Associates the device with the gateway.

        .. code-block:: python

            from clearblade.cloud import iot_v1

            def sample_bind_device_to_gateway():
                # Create a client
                client = iot_v1.DeviceManagerClient()

                # Initialize request argument(s)
                request = iot_v1.BindDeviceToGatewayRequest(
                    parent="parent_value",
                    gateway_id="gateway_id_value",
                    device_id="device_id_value",
                )

                # Make the request
                response = client.bind_device_to_gateway(request=request)

                # Handle the response
                print(response)

        Args:
            request (clearblade.cloud.iot_v1.device_types.BindDeviceToGatewayRequest):
                The request object. Request for `BindDeviceToGateway`.

        Returns:
            clearblade.cloud.iot_v1.device_types.BindDeviceToGatewayResponse:
                Response for BindDeviceToGateway.
        """

        cb_device_manager = ClearBladeDeviceManager()
        return await cb_device_manager.bindGatewayToDevice_async(request=request)

    async def unbind_device_from_gateway(self, request : UnbindDeviceFromGatewayRequest):
        r"""Deletes the association between the device and the
        gateway.

        .. code-block:: python

            def sample_unbind_device_from_gateway():
                # Create a client
                client = iot_v1.DeviceManagerClient()

                # Initialize request argument(s)
                request = iot_v1.UnbindDeviceFromGatewayRequest(
                    parent="parent_value",
                    gateway_id="gateway_id_value",
                    device_id="device_id_value",
                )

                # Make the request
                response = client.unbind_device_from_gateway(request=request)

                # Handle the response
                print(response)

        Args:
            request (clearblade.cloud.iot_v1.device_types.UnbindDeviceFromGatewayRequest):
                The request object. Request for
                `UnbindDeviceFromGateway`.
        """

        cb_device_manager = ClearBladeDeviceManager()
        return await cb_device_manager.unbindGatewayFromDevice_async(request=request)

    async def list_device_states(self, request : ListDeviceStatesRequest):
        cb_device_manager = ClearBladeDeviceManager()
        return await cb_device_manager.states_list_async(request=request)

    async def list_device_config_versions(self, request : ListDeviceConfigVersionsRequest):
        cb_device_manager = ClearBladeDeviceManager()
        return await cb_device_manager.config_versions_list_async(request=request)

    async def list_devices(self, request : ListDevicesRequest):
        cb_device_manager = ClearBladeDeviceManager()
        return await cb_device_manager.list_async(request=request)

    async def update_device(self, request : UpdateDeviceRequest):
        cb_device_manager = ClearBladeDeviceManager()
        return await cb_device_manager.update_async(request=request)

    async def list_device_registries(self, request: ListDeviceRegistriesRequest):
        cb_registry_manager = ClearBladeRegistryManager()
        return await cb_registry_manager.list_async(request=request)

    async def get_device_registry(self, request=GetDeviceRegistryRequest):
        cb_registry_manager = ClearBladeRegistryManager()
        return await cb_registry_manager.get_async(request=request)

    async def create_device_registry(self, request=CreateDeviceRegistryRequest):
        cb_registry_manager = ClearBladeRegistryManager()
        return await cb_registry_manager.create_async(request=request)

    async def delete_device_registry(self, request=DeleteDeviceRegistryRequest):
        cb_registry_manager = ClearBladeRegistryManager()
        return await cb_registry_manager.delete_async(request=request)

    async def update_device_registry(self, request=UpdateDeviceRegistryRequest):
        cb_registry_manager = ClearBladeRegistryManager()
        return await cb_registry_manager.patch_async(request=request)
