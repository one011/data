from colorama import Fore,Style
from getpass import getpass
from service.user_service import UserService
from service.order_service import OrderService
from service.role_service import RoleService
from service.type_service import TypeDao
import os
import sys
import time

__user_service=UserService()
__order_service=OrderService()
__role_service=RoleService()
__type_service=TypeDao
while True:
    os.system("cls")
    print(Fore.GREEN,"\n\t*************************")
    print(Fore.GREEN,"\n\t预约挂号")
    print(Fore.GREEN,"\n\t*************************")
    print(Fore.LIGHTGREEN_EX,"\t\n1.登录")
    print(Fore.LIGHTGREEN_EX, "\t\n2.注册")
    print(Fore.LIGHTGREEN_EX, "\t\n3.退出")
    print(Style.RESET_ALL)
    opt=input("\n\t输入1、2或3：")
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
                    os.system("cls")
                    title = input("\n\t输入症状：")
                    user_id=input("\n\t请输入ID号：")
                    #repassword = getpass("\n\t请输入科室号：")
                    state = input("\n\t请输入（预约成功）：")
                    '''if password != repassword:
                        print("\n\t密码不一致（3秒后返回）")
                        time.sleep(3)
                        continue
                    qq = input("\n\tQQ：")'''
                    #result1=__user_service.search_user_id()
                    result = __type_service.search_list()
                    for index in range(len(result)):
                        one = result[index]
                        print(Fore.LIGHTRED_EX,"\n\t%d.%s"%(index+1,one[1]))
                    print(Style.RESET_ALL)
                    opt = input("\n\t角色编号：")
                    #user_id=result[int(opt)]
                    type_id = result[int(opt) - 1][0]
                    __order_service.insert(title,user_id,type_id,state)
                    print("\n\t预约成功（3秒后自动返回）")
                    time.sleep(3)
                    #print("test")
                elif role=="医生":
                    os.system("cls")
                    print(Fore.LIGHTRED_EX,"\n\t1.需就诊名单")
                    print(Fore.LIGHTRED_EX, "\n\t2.所有预约就诊名单")
                    print(Fore.LIGHTRED_EX, "\n\tback.返回")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入1或2：")
                    if opt=="1":
                         page=1
                         while True:
                             os.system("cls")
                             count_page=__order_service.search_unreview_count_page()
                             result=__order_service.search_unreview_list(page)
                             for index in range(len(result)):
                                one=result[index]
                                print(Fore.LIGHTGREEN_EX,"\n\t%d\t%s\t%s\t%s"%(index+1,one[1],one[2],one[3]))
                             print(Fore.GREEN, "\n\t*************************")
                             print(Fore.LIGHTGREEN_EX,"\n\t%d/%d"%(page,count_page))
                             print(Fore.GREEN, "\n\t*************************")
                             print(Fore.LIGHTRED_EX, "\n\tback.返回")
                             print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                             print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                             print(Style.RESET_ALL)
                             opt = input("\n\t输入已就诊完成病人序列号")
                             if opt=="back":
                                 break
                             elif opt=="prev" and page>1:
                                 page-=1
                             elif opt=="next" and page<count_page:
                                 page+=1
                             elif int(opt)>=1 and int(opt)<=10:
                                 order_id=result[int(opt)-1][0]
                                 __order_service.update_unreview_order(order_id)
                    elif opt=="2":
                         page = 1
                         while True:
                             os.system("cls")
                             count_page = __order_service.search_count_page()
                             result = __order_service.search_list(page)
                             for index in range(len(result)):
                                 one = result[index]
                                 print(Fore.LIGHTGREEN_EX, "\n\t%d\t%s\t%s\t%s" % (index + 1, one[1], one[2], one[3]))
                             print(Fore.GREEN, "\n\t*************************")
                             print(Fore.LIGHTGREEN_EX, "\n\t%d/%d" % (page, count_page))
                             print(Fore.GREEN, "\n\t*************************")
                             print(Fore.LIGHTRED_EX, "\n\tback.返回")
                             print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                             print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                             print(Style.RESET_ALL)
                             opt = input("\n\t输入需要删除记录序号:")
                             if opt == "back":
                                 break
                             elif opt == "prev" and page > 1:
                                 page -= 1
                             elif opt == "next" and page < count_page:
                                 page += 1
                             elif int(opt) >= 1 and int(opt) <= 10:
                                 order_id = result[int(opt) - 1][0]
                                 __order_service.delete_by_id(order_id)


                    elif opt=="back":
                        break;
                    elif opt=="exit":
                        sys.exit(0)
        else:
            print("\n\t登录失败(3秒后返回上层)")
            time.sleep(3)

    elif opt=="2":
        while True:
            os.system("cls")
            print(Fore.LIGHTRED_EX, "\n\t1.添加用户")
            print(Fore.LIGHTRED_EX, "\n\t2.注销用户")
            print(Fore.LIGHTRED_EX, "\n\tback.返回")
            print(Style.RESET_ALL)
            opt = input("\n\t输入1或2：")
            if opt=="back":
                break
            elif opt=="1":
                os.system("cls")
                username=input("\n\t用户名：")
                password=getpass("\n\t密码：")
                repassword=getpass("\n\t再输入一次：")
                if password!=repassword:
                    print("\n\t密码不一致（3秒后返回）")
                    time.sleep(3)
                    continue
                qq=input("\n\tQQ：")
                result=__role_service.search_list()
                for index in range(len(result)):
                    one=result[index]
                    print(Fore.LIGHTRED_EX,"\n\t%d.%s"%(index+1,one[1]))
                print(Style.RESET_ALL)
                opt=input("\n\t角色编号：")
                role_id=result[int(opt)-1][0]
                __user_service.insert(username,password,qq,role_id)
                print("\n\t注册成功（3秒后自动返回）")
                time.sleep(3)


    elif opt == "3":
        sys.exit(0)