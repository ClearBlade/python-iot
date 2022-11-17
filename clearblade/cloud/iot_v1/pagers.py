from device_types import Device, ListDevicesResponse, ListDevicesRequest
from typing import Any, Awaitable, AsyncIterator, Callable

class ListDevicesPager:

    def __init__(self, method: Callable[..., ListDevicesResponse],
                 request: ListDevicesRequest,
                 response:ListDevicesResponse) -> None:
        self._method = method
        self._request = request
        self._response = response

    @property
    def pages(self):
        yield self._response
        while self._response.next_page_token:
            # call the method to fetch the next page.
            self._request.page_token = self._response.next_page_token
            self._response = self._method(request = self._request)
            yield self._response

    def __iter__(self):
        for page in self.pages:
            yield from page.devices

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)

class ListDevicesAsyncPager:
    """A pager for iterating through ``list_devices`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.iot_v1.types.ListDevicesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``devices`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDevices`` requests and continue to iterate
    through the ``devices`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.iot_v1.types.ListDevicesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[ListDevicesResponse]],
        request: ListDevicesRequest,
        response: ListDevicesResponse,
        ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (ListDevicesRequest):
                The initial request object.
            response (ListDevicesResponse):
                The initial response object.
        """
        self._method = method
        self._request = request
        self._response = response

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[ListDevicesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request)
            yield self._response

    def __aiter__(self) -> AsyncIterator[Device]:
        async def async_generator():
            async for page in self.pages:
                for response in page.devices:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)