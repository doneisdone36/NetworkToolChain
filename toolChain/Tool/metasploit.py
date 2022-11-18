import subprocess

def metasploit():
    print("""
---------------------------------------------
[1]Manual
[2]Run
---------------------------------------------
""")

    choice = input("Select Menu -->")
    try:
        if choice =="1":
            subprocess.run(["msfconsole","-h"])
        if choice =="2":
            subprocess.run("msfconsole")

    except KeyboardInterrupt:
        print("exit...")
        sleep(2)
        

