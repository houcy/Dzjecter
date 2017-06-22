import urllib
import urllib2
import re
import os
from platform import system
from base64 import b64encode , b64decode
def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
clear()
banner = '''
                                       .--.
                                     .' ,--.`.
                                   ,' ,'    `|
                                ,'  ,'      '                         
                              ,'   '
                            ,'    '
                         _,-    ,'   \033[96m
                      _,'       |                           ____,-------.
                   _,'           `.                   _,---'   ___,----. `.   
                _,'             _,---.             ,-'      ,-'         `.|    
             _,'            _,-'  _   `.        ,' __     ,'             |'    
           ,'   .--.    _,-'__,--' `.   `.   ,'_,-'  `. ,'              ,'     
        ,'  , '    `. ,'_,-'        `.    .,'-'-.      `.                      
      ,', '         ,','   DZJECTER   `.          `-. `. `.                     
    ,','          ,''`)`.    V1.0    ,`.         `.  `.`-.`. 
   ,,'           ((  '   `.        ,'     _,-=-.  `\  `\ |`.\  \033[92m 
  ' (             ``       `.    ,'     ,'-,'  `.  `)  `)`  )) 
 (   `                       ` .'     ,'-,'     |  ,;   ;   '' 
  `                           `:     |---|      `.     ,'
                               :     |---|       '.    :
                               :     `.--`.       '.   : 
                               `      `    `       ',`__)
                             >>> Bism Allah <<< \033[91m
                       Script Name : DZJECTER V 1.0 \033[92m
                 Script by: Joker-Security / Yacine Mohamed \033[96m
                        website : http://dev-labs.co \033[91m
                   
'''
print banner
def menu():
   print'''
\033[91m
\033[91m 1 \033[92m)\033[96m Get All Websites
\033[91m 2 \033[92m)\033[96m Get Wordpress  Websites
\033[91m 3 \033[92m)\033[96m Get Joomla Websites
\033[91m 4 \033[92m)\033[96m Find Admin Panel
\033[91m 5 \033[92m)\033[96m Upload Shell 
\033[91m 6 \033[92m)\033[96m Sql Scanner
\033[91m 7 \033[92m)\033[96m Base64 Encode
'''
menu()
def ext():
    ex = raw_input ('\033[92mContinue/Exit [C/E] -> ')
    if ex[0].upper() == 'E' :
           print 'Exiting!!!'
           exit()
    else:
           clear()
           print banner
           menu()
           select()

def  select():
  try:
    joker = raw_input("\033[96mEnter 1/7 : ")
    if joker == "4":
        def unique(seq):
            chf = set()
            return [chf.add(Y) or Y for Y in seq if Y not in chf]
        def getal(ip) :
                pg = 1
                ipsrv = ip
                wbs = []
                while pg <= 101:
                        try:
                            bng = "http://www.bing.com/search?q=ip%3A" + ipsrv + "+&count=50&first=" + str(pg)
                            obng = urllib2.urlopen(bng)
                            rbng = obng.read()
                            fwbs = re.findall('<h2><a href="(.*?)"', rbng)
                            for i in range(len(fwbs)):
                                    alcls = fwbs[i]
                                    findal = re.findall('http://(.*?)/', alcls)
                                    for xdd, itt in enumerate(findal):
                                      if 'www' not in itt:
                                        findal[xdd] = 'http://www.' + itt + '/'
                                      else:
                                        findal[xdd] = 'http://' + itt + '/'
                                    wbs.extend(findal)
                            pg += 50
                        except urllib2.URLError:
                                pass
                wbss = unique(wbs)
                adm = ['admin/login.php', 'admin/' , 'cp/' , '_admin/' , 'panel/' , 'admin/login.php']
                for site in wbss :
                    for admn in adm :
                        if urllib.urlopen(site + admn).getcode() == 200 :
                          print "[+] Found -> ", site + admn
                        else:
                          print "[+] Not_Found -> ", site + admn
        svrip=raw_input("\033[91mServer IP -> ")
        getal(svrip )
        ext()
    elif joker == "5":
        def unique(seq):
            chf = set()
            return [chf.add(Y) or Y for Y in seq if Y not in chf]
        def getal(ip) :
                pg = 1
                ipsrv = ip
                wbs = []
                while pg <= 101:
                        try:
                            bng = "http://www.bing.com/search?q=ip%3A" + ipsrv + "+&count=50&first=" + str(pg)
                            obng = urllib2.urlopen(bng)
                            rbng = obng.read()
                            fwbs = re.findall('<h2><a href="(.*?)"', rbng)
                            for i in range(len(fwbs)):
                                    alcls = fwbs[i]
                                    findal = re.findall('http://(.*?)/', alcls)
                                    for xdd, itt in enumerate(findal):
                                      if 'www' not in itt:
                                        findal[xdd] = 'http://www.' + itt + '/'
                                      else:
                                        findal[xdd] = 'http://' + itt + '/'
                                    wbs.extend(findal)
                            pg += 50
                        except urllib2.URLError:
                                pass
                wbss = unique(wbs)
                adm = ['up.php' , 'upload.php' , 'file_upload.php', 'admin/up.php' , 'admin/upload.php' , 'admin/file_upload.php']
                for site in wbss :
                    for admn in adm :
                        if urllib.urlopen(site + admn).getcode() == 200 :
                            print "[+] Found -> ", site + admn
                        if urllib.urlopen(site + admn).getcode() == 404 :
                            print "[-] Not_Found -> ", site + admn
                        if urllib.urlopen(site + admn).getcode() == 302 :
                            print "[*] Redirect -> ", site + admn
        svrip=raw_input("\033[92mServer IP -> ")
        getal(svrip )
        ext()
    elif joker == "6":
        def sql(srvip  ):
         srv= srvip
         start=1
         end=101
         while start<=end :
             try:
               bng = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A'+srv+"+php?id=&count=50&first="+str(start))
               bngg = open(bng[0])
               rdd=bngg.read()
               find=re.findall('<h2><a href="(.*?)"',rdd)
               start = start+50
             except IOError:
               print "[->] Network Error [<-]"
             try :
               for i in range(len(find)):
                       rez=find[i]+"'"
                       tst = urllib.urlretrieve(rez)
                       tstf = open(tst[0])
                       tstdd= tstf.read()
                       tstfind=re.findall('/error in your SQL syntax|mysql_fetch_array()|execute query|mysql_fetch_object()|mysql_num_rows()|mysql_fetch_assoc()|mysql_fetch_row()|SELECT * FROM|supplied argument is not a valid MySQL|Syntax error|Fatal error/i|You have an error in your SQL syntax|Microsoft VBScript runtime error',tstdd)
                       if(tstfind):
                         print "[Injectable] -> "+ rez 
             except :
                pass
        svr = raw_input("\033[96mServer IP -> ")
        sql(svr)

        ext()
    elif joker == "1":
        def unique(seq):
            chf = set()
            return [chf.add(Y) or Y for Y in seq if Y not in chf]
        def getal(ip) :
                pg = 1
                ipsrv = ip
                wbs = []
                while pg <= 101:
                        try:
                            bng = "http://www.bing.com/search?q=ip%3A" + ipsrv + "+&count=50&first=" + str(pg)
                            obng = urllib2.urlopen(bng)
                            rbng = obng.read()
                            fwbs = re.findall('<h2><a href="(.*?)"', rbng)
                            for i in range(len(fwbs)):
                                    alcls = fwbs[i]
                                    findal = re.findall('http://(.*?)/', alcls)
                                    for xdd, itt in enumerate(findal):
                                      if 'www' not in itt:
                                        findal[xdd] = 'http://www.' + itt + '/'
                                      else:
                                        findal[xdd] = 'http://' + itt + '/'
                                    wbs.extend(findal)
                            pg += 50
                        except urllib2.URLError:
                                pass
                wbss = unique(wbs)
                for site in wbss :
                   print site
 
        svrip=raw_input("\033[91mServer IP -> ")
        getal(svrip )
        ext()
    elif joker == '2':
        def unique(seq):
            chf = set()
            return [chf.add(Y) or Y for Y in seq if Y not in chf]
        def wpget(ip ) :
                pg = 1
                ipsrv = ip
                wbs = []
                while pg <= 101:
                        try:
                                bng = "http://www.bing.com/search?q=ip%3A" + ipsrv + "+?page_id=&count=50&first=" + str(pg)
                                obng = urllib2.urlopen(bng)
                                rbng = obng.read()
                                fwbs = re.findall('<h2><a href="(.*?)"', rbng)
                                for i in range(len(fwbs)):
                                        wpcls = fwbs[i]
                                        findwp = re.findall('(.*?)\?page_id=', wpcls)
                                        wbs.extend(findwp)
                                pg += 50
                        except:
                                pass
                wbs = unique(wbs)
                for site in wbs :
                    print site
        svrip=raw_input("\033[92mServer IP -> ")
        wpget(svrip)
        ext()
    elif joker == '3':
        def unique(seq):
            chf = set()
            return [chf.add(Y) or Y for Y in seq if Y not in chf]
        def wpget(ip ) :
                pg = 1
                ipsrv = ip
                wbs = []
                while pg <= 101:
                        try:
                                bng = "http://www.bing.com/search?q=ip%3A" + ipsrv + "+index.php?option=com&count=50&first=" + str(pg)
                                obng = urllib2.urlopen(bng)
                                rbng = obng.read()
                                fwbs = re.findall('<h2><a href="(.*?)"', rbng)
                                for i in range(len(fwbs)):
                                        wpcls = fwbs[i]
                                        findwp = re.findall('(.*?)index.php', wpcls)
                                        wbs.extend(findwp)
                                pg += 50
                        except:
                                pass
                wbs = unique(wbs)
                for site in wbs :
                    print site
        svrip=raw_input("\033[96mServer IP -> ")
        wpget(svrip)
        ext()
    elif joker == '7':
      print """
      \033[92m 1) \033[91mEncode
      \033[92m 2) \033[93mDecode
      """
      def bsencode():
        js = raw_input("Enter Your Text To Encode -> ")
        b = b64encode(js.encode("utf-8"))
        d = b.decode('utf-8')
        print d
        ext()
      def bsdecode():
        js = raw_input("Enter Base64 To Decode -> ")
        s = b64decode(js.decode("utf-8"))
        print s
        ext()
      bs = raw_input("Enter 1/2 -> ")
      if bs == "1":
        bsencode()
      elif bs == "2":
        bsdecode()
  except(KeyboardInterrupt):
    print "\nCtrl + C -> Exiting!!"
select()