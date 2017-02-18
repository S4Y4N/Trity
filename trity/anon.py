import mechanize
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
def anon():
    br = mechanize.Browser()

    to = raw_input(''+T+'' + color.UNDERLINE + 'Victim>' + color.END)
    subject = raw_input(''+T+'' + color.UNDERLINE + 'Subject>' + color.END)
    message = raw_input(''+T+'' + color.UNDERLINE + 'Message>' + color.END)

#proxy = "http://127.0.0.1:8080"

    url = "http://anonymouse.org/anonemail.html"
    headers = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
    br.addheaders = [('User-agent', headers)]
    br.open(url)
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_debug_http(False)
    br.set_debug_redirects(False)
   #br.set_proxies({"http": proxy})

    br.select_form(nr=0)

    br.form['to'] = to
    br.form['subject'] = subject
    br.form['text'] = message

    result = br.submit()

    response = br.response().read()


    if "The e-mail has been sent anonymously!" in response:
        print (''+G+'' + color.UNDERLINE + 'Email has been sent successfully!' + color.END)
    else:
       print (''+R+'' + color.UNDERLINE + 'Failed to send email!' + color.END)
