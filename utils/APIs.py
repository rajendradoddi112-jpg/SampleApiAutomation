import requests

class API:
    base_url="https://fakerestapi.azurewebsites.net"

    def __init__(self):
        self.header={
            "accept":"text/plain"
        }

    def get(self,endpoint):
        url=f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        response=requests.get(url,headers=self.header)
        return response

