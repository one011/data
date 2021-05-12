from colorama import  Fore,Style
from service.user_service import UserService
import os
import sys
import time
from getpass import getpass

__user_service=UserService()
while True:
    os.system("cls")
    print(Fore.LIGHTGREEN_EX,"\n\t****************************")
    print(Fore.LIGHTGREEN_EX,"\n\t就诊预约")
    print(Fore.LIGHTGREEN_EX, "\n\t**************************")
    print(Fore.LIGHTGREEN_EX, "\n\t1.登录")
    print(Fore.LIGHTGREEN_EX, "\n\t2.退出")
    print(Style.RESET_ALL)
    opt=input("\n\t输入1或2：")
    if opt=="1":
        username=input("\n\t用户名：")
        password=getpass("\n\t密码：")
        result=__user_service.login(username,password)
        #登录成功
        if result==True:
            #查询角色
            role=__user_service.search_user_role(username)
            os.system("cls")
            while True:
                if role=="病人":
                    print("test")
                elif role=="医生":
                    print(Fore.LIGHTRED_EX, "\n\t1.预约管理")
                    print(Fore.LIGHTRED_EX, "\n\t.2.用户管理")
                    print(Fore.LIGHTRED_EX, "\n\tback.返回")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入1或2：")
                    if opt=="back":
                        break;
                    elif opt=="exit":
                        sys.exit(0)
        else:
            print("\n\t登录失败(3秒后返回上一页)")
            time.sleep(3)
    elif opt=="2":
        sys.exit(0)