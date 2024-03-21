
from cymruwhois import Client
import xlrd
import openpyxl
import requests
import colorama
from colorama import *

print (f'''
{Fore.BLUE}
                $$$$$$\ $$$$$$$\        $$$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\$
                \_$$  _|$$  __$$\       \__$$  __|$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\$
                  $$ |  $$ |  $$ |         $$ |   $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ |
                  $$ |  $$$$$$$  |         $$ |   $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  |
                  $$ |  $$  ____/{Fore.GREEN}          $$ |   $$  __$$< $$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$<
                  $$ |  $$ |               $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ |\033[1;31m--v1.0--\033[1;31m
                $$$$$$\ $$ |               $$ |   $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |
                \______|\__|               \__|   \__|  \__|\__|  \__| \______/ \__|  \__|\________|\__|  \__|\033[1;32m
\033[1;33m
''')
print(f"{Fore.LIGHTCYAN_EX}=================================================================================================={Fore.LIGHTGREEN_EX} CREAT BY CT89")

def ip_1():

    select = input('chọn 1 IP (1) hoặc lấy list IP từ file(2): 1 or 2: ')
    # print(select)
    if select =='1':
        IP = input('nhập IP: ')
        c = Client()
        r= c.lookup(IP)
        print('AS '+ r.asn + ' NAME: '+ r.owner )
        track_location2(IP)
    if select == '2':
        file_exel = 'Book1.xlsx'
        wb = xlrd.open_workbook_xls(file_exel)
        sheet = wb.sheet_by_index(0)
        row = sheet.nrows
        # colums = sheet.ncols
        for i in range(1,row):
            if '10.28.' not in sheet.cell_value(i,1):
                print(sheet.cell_value(i,1))
                c = Client()
                r= c.lookup(sheet.cell_value(i,1))
                print(sheet.cell_value(i,1)+ "--" + r.asn + "---"+ r.owner +"\n" )

def ip_2():
    select = input('chọn 1 IP (1) hoặc lấy list IP từ file(2): 1 or 2: ')
    # print(select)
    if select == '1':
        IP = input('nhập IP: ')
        c = Client()
        r = c.lookup(IP)
        print('AS ' + r.asn + ' NAME: ' + r.owner)
    elif select == '2':
        file_excel = 'Book3.xlsx'
        wb = openpyxl.load_workbook(file_excel)
        sheet = wb.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if '10.28.' not in row[1]:
                print(row[1])
                c = Client()
                r = c.lookup(row[1])
                name = str (row[1] + "--" + r.asn + "---" + r.owner)
                index = name.find("VINAGAME-AS-VN")
                index2 = name.find("FACEBOOK")
                # print(row[1] + "--" + r.asn + "---" + r.owner + "\n")
                with open ("ip.txt","a")as f:
                    if index !=-1 or index2!=-1:          #'VINAGAME-AS-VN VNG Corporation, VN' or 'FACEBOOK, US'
                        f.write(row[1] + " -- " + r.asn + " --- " + r.owner + "\n")
                        f.close
def track_location(ip):
    ip_address = ip
    response = requests.get(f'https://api.iplocation.net/?ip={ip_address}')
    print(response)
    data = response.json()
    location_data = {
                    "Ip Address":ip_address,
                    "city": data.get("city"),
                    "ip_number": data.get("ip_number"),
                    "ip_version": data.get("ip_version"),
                    "country": data.get("country_name"),
                    "country_code2": data.get("country_code2"),
                    "isp": data.get("isp"),
                    "Browser": data.get("browser"),
                   
                }
    print(Fore.LIGHTGREEN_EX + str(location_data))

def track_location2(ip):
    ip_address = ip
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    print(response)
    data = response.json()
    location_data = {
            "IP": data.get("query"),
            "status": data.get("status"),
            "continent": data.get("continent"),
            "continentCode": data.get("continentCode"),
            "country": data.get("country"),
            "countryCode": data.get("countryCode"),
            "region": data.get("region"),
            "regionName": data.get("regionName"),
            "city": data.get("city"),
            "district":data.get("district"),
            "zip": data.get("zip"),
            "lat": data.get("lat"),
            "lon": data.get("lon"),
            "timezone": data.get("timezone"),
            "offset": data.get("offset"),
            "currency": data.get("currency"),
            "isp": data.get("isp"),
            "org": data.get("org"),
            "as": data.get("as"),
            "asname": data.get("asname"),
            "mobile":data.get("mobile"),
            "proxy": data.get("proxy"),
            "hosting": data.get("hosting")
        }
    print(Fore.LIGHTGREEN_EX + str(location_data))

if __name__=="__main__":
    ip_1()
    # track_location2("117.2.91.179")
