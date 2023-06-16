# 编写程序实现用户输入用户名和密码功能，
# 当用户名为user且密码为123时，现实登陆成功，
# 否则登录失败，失败时允许重复输入三次。
count=0
while count<3:
    username=input("请输入用户名：")
    password=input("请输入密码：")
    if(username=="user"):
        print("用户名正确")
        if(password=="123"):
            print("登录成功")
            break
        else:
            print("密码错误")
            count+=1
    else:
        print("用户名和密码错误请重新输入")
        count+=1
