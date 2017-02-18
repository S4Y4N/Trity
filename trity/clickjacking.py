import urllib2, sys
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
def clickjacking():    
    def check(url):
        try:
            if "http" not in url:
                url = "http://" + url
            data = urllib2.urlopen(url)
            headers = data.info()

            if not "X-Frame-Options" in headers:
                return True
        except:
            return False

    def Create_Poc(url):
        code = """<html>
   <head>
     <title>Clickjack test page</title>
   </head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="{}" width="500" height="500"></iframe>
   </body>
</html>
        """.format(url)
        try:
            f = open(url+".html","w")
            f.write(code)
            f.close()
        except:
	    print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Can't make .html file!" + color.END)

    def main():
        try:
	    f = open('sites.txt', 'r')
	    z = f.readlines()
       
        except:
            print "Error"
            print "sites.txt does not exist!"
            sys.exit(0)
        for x in z[0:]:
    	     print " \nChecking... "+x
    	     if check(x):
        	     print "*** The website is VULNERABLE to clickjacking! ***"
        	     Create_Poc(x)
        	     print " Created a poc and saved to Clickjacking.html"
    	     elif not check(x):
        	     print " The website is not vulnerable!"

    main()
