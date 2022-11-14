import json
import httpx
from config import *

class HttpClient():
    def __init__(self,
                 clearblade_config:ClearBladeConfig = None) -> None:

        self._clearblade_config = clearblade_config
        self._system_key = self._clearblade_config.system_key
        self._auth_token = self._clearblade_config.token

        print("System Key : {} \n Auth token : {}".format(self._system_key, self._auth_token))

        self._post_url : str = None
        self._request_headers : dict = None
        self._post_body : dict = None

    def _get_api_url(self, api_name:str = None, is_web_hook:bool = True) -> str:
        api_web_hook_path = "api/v/4/webhook/execute"
        if not is_web_hook:
            api_web_hook_path = "api/v/1/code"

        return "{}:{}/{}/{}/{}?".format(self._clearblade_config.api_url,
                                        "443",
                                        api_web_hook_path,
                                        self._system_key,
                                        api_name)

    def _headers(self):
        return {'ClearBlade-UserToken':self._clearblade_config.token, 'Content-Type':'application/json'}

    def _process_request_body(self, request_body = {}):
        return json.dumps(request_body)

    def get(self,api_name:str = None):
        self._post_url = self._get_api_url(api_name=api_name)
        self._request_headers = self._headers()

    def post(self, api_name:str = None,
             is_webhook_folder:bool = True,
             request_body:dict = {}):

        self._post_url = self._get_api_url(api_name=api_name, is_web_hook=is_webhook_folder)
        self._request_headers = self._headers()
        self._post_body = self._process_request_body(request_body=request_body)

    def delete(self,api_name:str = None):
        self._post_url = self._get_api_url(api_name=api_name)
        self._request_headers = self._headers()

    def patch(self, api_name:str = None, request_body:dict = {}):
        self._post_url = self._get_api_url(api_name=api_name)
        self._request_headers = self._headers()
        self._post_body = self._process_request_body(request_body=request_body)

class SyncClient(HttpClient):

    def get(self, api_name:str = None, request_params:dict = {}):
        super().get(api_name=api_name)
        httpx_sync_client = httpx.Client()
        response = httpx_sync_client.request("GET", url=self._post_url,
                                            headers=self._request_headers,
                                            params=request_params)
        return response

    def post(self, api_name:str = None,
             is_webhook_folder:bool = True,
             request_params = {}, request_body = {}):
        super().post(api_name=api_name, is_webhook_folder=is_webhook_folder,
                     request_params=request_params, request_body=request_body)
        #send the request and return the response
        httpx_sync_client = httpx.Client()
        response = httpx_sync_client.request("POST", url=self._post_url,
                                            headers=self._request_headers,
                                            params=request_params,
                                            data=self._post_body)
        return response

    def delete(self, api_name:str = None, request_params:dict = None):
        super().delete(api_name = api_name)
        httpx_sync_client = httpx.Client()
        response = httpx_sync_client.request("DELETE", url=self._post_url,
                                            headers=self._request_headers,
                                            params=request_params)
        return response

    def patch(self, api_name: str = None, request_body: dict = {}, request_params:dict = {}):
        super().patch(api_name, request_body)
        httpx_sync_client= httpx.Client()
        response = httpx_sync_client.request("PATCH", url=self._post_url,
                                            headers=self._request_headers,
                                            params = request_params,
                                            data=self._post_body)
        return response

class AsyncClient(HttpClient):

    async def get(self, api_name:str = None, request_params:dict = {}):
        super().get(api_name=api_name)
        httpx_async_client= httpx.AsyncClient()
        response = await httpx_async_client.request("GET", url=self._post_url,
                                            headers=self._request_headers,
                                            params=request_params)
        await httpx_async_client.aclose()
        return response

    async def post(self, api_name:str = None,
                   is_webhook_folder:bool = True,
                   request_params = {}, request_body={}):
        super().post(api_name=api_name, is_webhook_folder=is_webhook_folder,
                     request_params=request_params, request_body=request_body)
        httpx_async_client= httpx.AsyncClient()
        response = await httpx_async_client.request("POST", url=self._post_url,
                                                    headers=self._request_headers,
                                                    params=request_params,
                                                    data=self._post_body)
        await httpx_async_client.aclose()
        return response

    async def delete(self, api_name:str = None, request_params:dict = {}):
        super().delete(api_name=api_name)
        httpx_async_client= httpx.AsyncClient()
        response = await httpx_async_client.request("DELETE", url=self._post_url,
                                            headers=self._request_headers,
                                            params=request_params)
        await httpx_async_client.aclose()
        return response

    async def patch(self, api_name:str = None, request_params:dict = {}, request_body:dict = {}):
        super().patch(api_name = api_name, request_body=request_body)
        httpx_async_client= httpx.AsyncClient()
        response = await httpx_async_client.request("PATCH", url=self._post_url,
                                            headers=self._request_headers,
                                            params = request_params,
                                            data=self._post_body)
        return response
