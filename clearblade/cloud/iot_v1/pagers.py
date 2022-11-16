from device_types import ListDevicesResponse, ListDevicesRequest
from typing import Callable

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
            yield from page.devices()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)

