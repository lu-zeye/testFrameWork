import json
def read_login_data(filename):
    with open(filename,'r',encoding='utf-8') as f:
        login_read_data = json.load(f)
        read_list = []
        for login_data in login_read_data:
            read_list.append(tuple(login_data.values()))
    return read_list
if __name__ == '__main__':
    filename = "/data/login2.json"