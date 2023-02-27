from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests

import json

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

username = 'SE000104'
password = 'Jaggillarstorkok911!'


def get_auth_token():
    driver = webdriver.Chrome(
        executable_path='./chromedriver.exe', chrome_options=options)

    driver.get(
        'https://webgate.electroluxprofessional.com/WF_Login.aspx?ReturnUrl=%2f')

    name_element = driver.find_element(
        By.ID, "_ctl0_ContentPlaceHolder1_txtWGName")
    password_element = driver.find_element(
        By.ID, "_ctl0_ContentPlaceHolder1_txtWGPassword")

    button_element = driver.find_element(
        By.ID, "_ctl0_ContentPlaceHolder1_btnOK")

    name_element.send_keys(username)
    password_element.send_keys(password)

    button_element.click()

    auth_token = driver.get_cookies()[5]['value']

    driver.close()

    return auth_token


token = get_auth_token()

headers = {
    'cookie': f'WG_lang=0; WG_Remember=name={username}&password={password}; WinUser=; DbUser=SE000104; AuthType=WinForms; ASP.NET_SessionId=5wyqsrfmvqm4lgmugr3lb4pr; pub=; .wgauth={token}; JSESSIONID=0001HY1nxGqllJNP3ocEUkadFoo:2BK3TRVSTV'
}

url = 'https://webgate.electroluxprofessional.com/serviceepr/3s/actHeaderDetail.do?action=loadExisting&idAct=47588'

response = requests.get(url, headers=headers)

print(response.text)
