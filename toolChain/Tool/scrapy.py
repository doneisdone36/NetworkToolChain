import subprocess

class scrapy():
    def startproject():
        keyword = input("type search keyword : ")
        domain  = input("type domain site :")
        subprocess.run(["scrapy","startproject",keyword,domain])

  
