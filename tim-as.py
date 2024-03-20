
from cymruwhois import Client
import xlrd
import openpyxl
import pygeoip

print ('''
\033[1;33m
                $$$$$$\ $$$$$$$\        $$$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\$
                \_$$  _|$$  __$$\       \__$$  __|$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\$
                  $$ |  $$ |  $$ |         $$ |   $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ |
                  $$ |  $$$$$$$  |         $$ |   $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  |
                  $$ |  $$  ____/\033[1;33m          $$ |   $$  __$$< $$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$<
                  $$ |  $$ |               $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ |\033[1;31m{v1.0}\033[1;31m
                $$$$$$\ $$ |               $$ |   $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |
                \______|\__|               \__|   \__|  \__|\__|  \__| \______/ \__|  \__|\________|\__|  \__|\033[1;32m
\033[1;33m
''')
print("\033[1;33m==================================================================================================\033[1;33m \033[1;33m CREAT BY CT89")

def ip_1():

    select = input('chọn 1 IP (1) hoặc lấy list IP từ file(2): 1 or 2: ')
    # print(select)
    if select =='1':
        IP = input('nhập IP: ')
        c = Client()
        r= c.lookup(IP)
        print('AS '+ r.asn + ' NAME: '+ r.owner )
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
def track_location():
    gip = pygeoip.GeoIP("GeoLiteCity.dat")
    res=gip.record_by_addr('Enter the ip')
    for key,val in res.items():
        print('%s : %s' % (key,val))


if __name__=="__main__":
   ip_2()
