import subprocess 

def tshark():
    try:
        choice = input("Do you have access authority??\n Y/N\t")
        if choice == 'n' or 'N':
            AcessAutority()                 
        else:
            subprocess.call("tshark")

    except KeyboardInterrupt:
        print("exit...")
        sleep(2)


    def AcessAutority():
        subprocess.call(["sudo","chown","kimgyujin","/dev/bpf*"])
        print("Acess Autority Successfully")
        return True
