import getpass

def login():
    CorrectUserName = "1"
    CorrectPassword = "1"

    try:
        loop="True"
        while(loop=="True"):
            username= input("Please Enter your Username\n")
            if(username == CorrectUserName):
                loop1 = "True"
                password =  getpass.getpass("Please Enter your Password\n")
                if(password == CorrectPassword):
                    print("Login Successfully.. Welcome\n")
                    loop="False"
                    loop1="False"
                else:
                    print("Login failed")
            else:
                print("Login failed")

    except KeyboardInterrupt:
        print("Exiting...")
        sleep(2)


