import requests

class LoginApi:
    def login(self,mobile,password):
        jsonData = {"mobile": mobile, "password": password}
        reque = requests.post(url="http://182.92.81.159/api/sys/login",
                      json=jsonData)
        return reque
if __name__ == '__main__':
    login_api = LoginApi()
    login_api.login("1","2")
