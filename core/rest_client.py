import requests


class RestClient:

    def __init__(self, api_root_url, username=None, password=None, token=None):
        self.api_root_url = api_root_url
        self.session = requests.Session()
        if username and password:
            self.session.auth = (username, password)
        elif token:
            self.session.headers["Authorization"] = "token {}".format(token)

    def get(self, url, **kwargs):
        return self.request("get", url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request("post", url, data, json, **kwargs)

    def head(self, url, **kwargs):
        return self.request("head", url, **kwargs)

    def options(self, url, **kwargs):
        return self.request("options", url, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request("put", url, data, **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request("patch", url, data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request("delete", url, **kwargs)

    def request(self, method_name, url, data=None, json=None, **kwargs):
        url = "".join([self.api_root_url, url])
        if method_name == "get":
            return self.session.get(url, **kwargs)
        if method_name == "post":
            return self.session.post(url, data, json, **kwargs)
        if method_name == "head":
            return self.session.head(url, **kwargs)
        if method_name == "options":
            return self.session.options(url, **kwargs)
        if method_name == "put":
            return self.session.put(url, data, **kwargs)
        if method_name == "patch":
            return self.session.patch(url, data, **kwargs)
        if method_name == "delete":
            return self.session.delete(url, **kwargs)


if __name__ == '__main__':
    r = RestClient("https://github.com")
    x = r.get("/")
    print(x.status_code)
