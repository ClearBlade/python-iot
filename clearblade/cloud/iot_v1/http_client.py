import json
import requests
from config import *

class HttpClient():
    def __init__(self) -> None:
        #TODO: we will need to set this when user constructs the client. 
        self._system_key = get_system_key()
        self._auth_token = get_auth_token()
        print("System Key : {} \n Auth token : {}".format(self._system_key, self._auth_token))
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

    def get(self, request_params, request_body):
        pass
    
    def post(self, request_params = {}, request_body = {}):
        pass

    def delete(self, request_params, request_body):
        pass

class SyncClient(HttpClient):
    
    def post(self, request_params = {}, request_body = {}):
        post_url = self._cb_api_url+ self._process_request_params(request_params=request_params)
        headers = self._headers()
        post_body = self._process_request_body(request_body=request_body)

        print("post_url = {}\nheaders = {}\nbody= {}\n".format(post_url,headers,post_body))

        #send the request and return the response
        response = requests.request("POST",post_url, headers=headers,data=post_body)
        return response


class AsyncClient():
    def __init__(self) -> None:
        super().__init__(self)

    def post(self, request_params = {}, request_body={}):
        pass

