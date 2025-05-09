# -*- coding: UTF-8 -*-
# @Author  : XUZHIHAO
# @Time    : 2025/5/9
# @File    : auto_connect.py
# @Function:auto_connect stu_net
import requests
import os
import threading
import pickle
import time
import sys
from bs4 import BeautifulSoup
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
# 配置
LOGIN_URL = 'https://a.stu.edu.cn/ac_portal/login.php'
FLUX_URL = 'https://a.stu.edu.cn/ac_portal/userflux'
LOGOUT_URL = 'https://a.stu.edu.cn/ac_portal/login.php'  # 注销 URL
COOKIE_FILE = 'cookies.pkl'
CRED_FILE = 'credentials.json'
def save_credentials(username, password):
    with open(CRED_FILE, 'w') as f:
        json.dump({'username': username, 'password': password}, f)
def load_credentials():
    if os.path.exists(CRED_FILE):
        with open(CRED_FILE, 'r') as f:
            data = json.load(f)
            return data['username'], data['password']
    return None, None
def switch_account(prompt_new=False):
    if not prompt_new:
        username, password = load_credentials()
        if username and password:
            print(f"\n[✓] 使用上次登录账号：{username}")
            return username, password

    print("\n请输入校园网账号和密码")
    username = input("账号: ")
    password = input("密码: ")
    save_credentials(username, password)
    if os.path.exists(COOKIE_FILE):
        os.remove(COOKIE_FILE)
    return username, password
def save_cookies(session, filename):
    with open(filename, 'wb') as f:
        pickle.dump(session.cookies, f)

def load_cookies(session, filename):
    with open(filename, 'rb') as f:
        session.cookies.update(pickle.load(f))

def is_logged_in(session):
    # 访问 userflux 看是否返回正常 HTML
    r = session.post(FLUX_URL, verify=False)
    r.encoding = 'utf-8'  # 显式指定编码
    # print(r.text)
    return '用户名称' in r.text

def login():
    session = requests.Session()
    USERNAME,PASSWORD=switch_account(prompt_new=False)
    login_data = {
        'opr': 'pwdLogin',
        'userName': USERNAME,
        'pwd': PASSWORD,
        'rememberPwd': '1'
    }
    headers = {
        'Referer': 'https://a.stu.edu.cn/ac_portal/default/pc.html?tabs=pwd',
        'User-Agent': 'Mozilla/5.0'
    }

    r = session.post(LOGIN_URL, data=login_data, headers=headers, verify=False)
    r.encoding = 'utf-8'  # 显式指定编码
    # print(r)
    if 'login_ok' in r.text or r.status_code == 200:
        print("[✓] 登录成功，正在保存 cookie...")
        save_cookies(session, COOKIE_FILE)
        return session
    else:
        print("[×] 登录失败")
        return None

def get_user_flux(session):
    r = session.post(FLUX_URL, verify=False)
    r.encoding = 'utf-8'  # 显式指定编码
    soup = BeautifulSoup(r.text, 'html.parser')

    data = {}
    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) == 2:
            key = cols[0].get_text(strip=True).replace('：', '')
            value = cols[1].get_text(strip=True)
            data[key] = value

    return data
def logout():
    # 发送注销请求
    session = requests.Session()
    USERNAME, PASSWORD = switch_account(prompt_new=False)
    login_data = {
        'opr': 'logout',
        'userName': USERNAME,
        'pwd': PASSWORD,
        'rememberPwd': '1'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://a.stu.edu.cn/ac_portal/default/pc.html',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }
    r = session.post(LOGOUT_URL,data=login_data,headers=headers, verify=False)
    # print(r.text)
    if r.status_code == 200:
        print("[✓] 注销成功")
    else:
        print("[×] 注销失败")
def print_account():
    session = requests.Session()
    flux_info = get_user_flux(session)
    print("\n[✓] 当前用户流量信息：")
    for k, v in flux_info.items():
        print(f"{k}: {v}")
def main():
    session = requests.Session()

    if os.path.exists(COOKIE_FILE):
        load_cookies(session, COOKIE_FILE)
        if not is_logged_in(session):
            print("[!] Cookie 无效，重新登录...")
            session = login()
        else:
            session = login()
            flux_info = get_user_flux(session)
            print(f'登录成功，欢迎{flux_info["用户名称"]}')
    else:
        session = login()

    if session:
        flux_info = get_user_flux(session)
        print("[✓] 当前用户流量信息：")
        for k, v in flux_info.items():
            print(f"{k}: {v}")
if __name__ == '__main__':
      print("ヽ(•‿•)ノ欢迎使用汕头大学校园网自动连接助手ヽ(•‿•)ノ")
      main()
      print("⌘•‿•⌘ by24级工学院徐志豪")