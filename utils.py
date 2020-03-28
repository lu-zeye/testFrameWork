# 存放自定义的工具类
import json

def read_login_data(filename):
    with open(filename,'r',encoding='utf-8') as f:

        login_data_list = json.load(f)
        print(login_data_list)
        read_list = []
        for login_data in login_data_list:
            read_list.append(tuple(login_data.values()))

    return read_list


if __name__ == '__main__':
    a = read_login_data("./data/login.json")

    print(a)