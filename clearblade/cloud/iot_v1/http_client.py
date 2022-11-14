import json
import httpx
from config import *

class HttpClient():
    def __init__(self) -> None:
        #TODO: we will need to set this when user constructs the client.
        self._system_key = get_system_key()
        self._auth_token = get_auth_token()

        print("System Key : {} \n Auth token : {}".format(self._system_key, self._auth_token))

        self._post_url : str = None
        self._request_headers : dict = None
        self._post_body : dict = None

        self._init_api_end_points()

    def _init_api_end_points(self):
        self._base_url = "https://iot-sandbox.clearblade.com"
        self._port = "443"
        self._api_version_webhook_path = "/api/v/4/webhook/execute"

        #TODO: this api name needs to come from service class
        self._api_folder_name = "cloudiot_devices"

        self._cb_api_url = "{}:{}{}/{}/{}?".format(self._base_url,self._port,
                                                   self._api_version_webhook_path,
                                                   self._system_key,self._api_folder_name)

    def _process_request_params(self, request_params = {}):
        return "&".join(f'{k}={v}'for k, v in request_params.items())

    def _headers(self):
        return {'ClearBlade-UserToken':self._auth_token, 'Content-Type':'application/json'}

    def _process_request_body(self, request_body = {}):
        return json.dumps(request_body)

    def get(self, request_params):
        self._post_url = self._cb_api_url+ self._process_request_params(request_params=request_params)
        self._request_headers = self._headers()        

    def getStateList(self, request_params):
        self._api_folder_name = "cloudiot_devices_states"
        self._cb_api_url = "{}:{}{}/{}/{}?".format(self._base_url,self._port,
                                                    self._api_version_webhook_path,
                                                    self._system_key,self._api_folder_name)
        self._post_url = self._cb_api_url+ self._process_request_params(request_params=request_params)
        self._request_headers = self._headers()        

    def getConfigVersionsList(self, request_params):
        self._api_folder_name = "cloudiot_devices_configVersions"
        self._cb_api_url = "{}:{}{}/{}/{}?".format(self._base_url,self._port,
                                                    self._api_version_webhook_path,
                                                    self._system_key,self._api_folder_name)
        self._post_url = self._cb_api_url+ self._process_request_params(request_params=request_params)
        self._request_headers = self._headers()        

    def list(self, request_params = {}):
        self._post_url = self._cb_api_url+ self._process_request_params(request_params=request_params)
        self._request_headers = self._headers()

    def update(self, request_params = {}, request_body = {}):
        self._post_url = self._cb_api_url+ self._process_request_params(request_params=request_params)
        self._request_headers = self._headers()
        self._post_body = self._process_request_body(request_body=request_body)

    def post(self, request_params = {}, request_body = {}):
        if request_params.get('method') is not None:
            if request_params['method'] == 'bindDeviceToGateway' or request_params['method'] == 'unbindDeviceFromGateway':
                self._api_folder_name = "cloudiot"
            
        self._post_url = self._cb_api_url+ self._process_request_params(request_params=request_params)
        self._request_headers = self._headers()
        self._post_body = self._process_request_body(request_body=request_body)

    def delete(self, request_params):
        self._post_url = self._cb_api_url+ self._process_request_params(request_params=request_params)
        self._request_headers = self._headers()

class SyncClient(HttpClient):

    def post(self, request_params = {}, request_body = {}):
        super().post(request_params=request_params, request_body=request_body)
        #send the request and return the response
        httpx_sync_client = httpx.Client()
        response = httpx_sync_client.request("POST", url=self._post_url,
                                            headers=self._request_headers, data=self._post_body)
        return response
    
    def delete(self, request_params):
        super().delete(request_params=request_params)
        httpx_sync_client = httpx.Client()
        response = httpx_sync_client.request("DELETE", url=self._post_url,
                                            headers=self._request_headers)
        return response

    def get(self, request_params = {}):
        super().get(request_params=request_params)
        httpx_sync_client = httpx.Client()
        response = httpx_sync_client.request("GET", url=self._post_url,
                                            headers=self._request_headers)
        return response

    def list(self, request_params = {}):
        super().list(request_params=request_params)
        httpx_sync_client = httpx.Client()
        response = httpx_sync_client.request("GET", url=self._post_url,
                                            headers=self._request_headers, data=self._post_body)
        return response

    def getStateList(self, request_params = {}):
        super().getStateList(request_params=request_params)
        httpx_sync_client = httpx.Client()
        response = httpx_sync_client.request("GET", url=self._post_url,
                                            headers=self._request_headers)
        return response

    def getConfigVersionsList(self, request_params = {}):
        super().getConfigVersionsList(request_params=request_params)
        httpx_sync_client = httpx.Client()
        response = httpx_sync_client.request("GET", url=self._post_url,
                                            headers=self._request_headers)
        return response

    def update(self, request_params = {}, request_body = {}):
        super().update(request_body=request_body, request_params=request_params)
        httpx_sync_client = httpx.Client()
        response = httpx_sync_client.request("PATCH", url=self._post_url,
                                            headers=self._request_headers, data=self._post_body)
        return response


class AsyncClient(HttpClient):

    async def post(self, request_params = {}, request_body={}):
        super().post(request_params=request_params, request_body=request_body)
        httpx_async_client= httpx.AsyncClient()
        response = await httpx_async_client.request("POST", url=self._post_url,
                                                    headers=self._request_headers, data=self._post_body)
        await httpx_async_client.aclose()
        return response

    async def delete(self, request_params):
        super().delete(request_params=request_params)
        httpx_async_client= httpx.AsyncClient()
        response = await httpx_async_client.request("DELETE", url=self._post_url,
                                            headers=self._request_headers)
        await httpx_async_client.aclose()
        return response

    async def get(self, request_params):
        super().get(request_params=request_params)
        httpx_async_client= httpx.AsyncClient()
        response = await httpx_async_client.request("GET", url=self._post_url,
                                            headers=self._request_headers)
        await httpx_async_client.aclose()
        return response

    async def list(self, request_params = {}):
        super().list(request_params=request_params)
        httpx_async_client= httpx.AsyncClient()
        response = await httpx_async_client.request("GET", url=self._post_url,
                                            headers=self._request_headers, data=self._post_body)
        await httpx_async_client.aclose()
        return response

    async def getStateList(self, request_params = {}):
        super().getStateList(request_params=request_params)
        httpx_async_client= httpx.AsyncClient()
        response = await httpx_async_client.request("GET", url=self._post_url,
                                            headers=self._request_headers)
        await httpx_async_client.aclose()
        return response

    async def getConfigVersionsList(self, request_params = {}):
        super().getConfigVersionsList(request_params=request_params)
        httpx_async_client= httpx.AsyncClient()
        response = await httpx_async_client.request("GET", url=self._post_url,
                                            headers=self._request_headers)
        await httpx_async_client.aclose()
        return response

    async def update(self, request_params = {}, request_body = {}):
        super().update(request_body=request_body, request_params=request_params)
        httpx_async_client= httpx.AsyncClient()
        response = await httpx_async_client.request("PATCH", url=self._post_url,
                                            headers=self._request_headers, data=self._post_body)
        return response
