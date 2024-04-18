username = input("请输入用户名：")
while True:
    if username == "admin":
        pwd = input("请输入密码：")
        if pwd == "123456":
            print("恭喜你登录成功！")
            break
        else:
            print("您的密码输入错误，请重试")
    elif username == "exit":
        break
    else:
        print("您的用户名错误！！")
