import os, time
import requests as r
from bs4 import BeautifulSoup
if os.name=='nt':
    import msvcrt as m
else:
    import getch

W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray


def wait():
    if os.name=='nt':
        m.getch()
    else:
        getch.getch()
    os.system('cls' if os.name=='nt' else 'clear')

os.system('cls' if os.name=='nt' else 'clear')
def banner():
    print(C+"  __  ___"+R+" .__   __.")
    print(C+" |  |/  /"+R+" |  \ |  |")
    print(C+" |  '  / "+R+" |   \|  |"+W+"", time.ctime())
    print(C+" |    <  "+R+" |  . `  |"+C+ " kuso"+R+"nime"+W+".com")
    print(C+" |  .  \ "+R+" |  |\   |"+C+" github.com/"+R+"arzyware")
    print(C+" |__|\__\ "+R+"|__| \__|"+W+"")
    print("")

cka = True
while cka:
    try:
        banner()
        a = input(C+" Judul "+R+"> "+W)
        payload = {"s":a}
        response = r.get('https://kusonime.com/?s=', params=payload).text
        
        soup = BeautifulSoup(response, "html.parser")

        for i in soup.find_all('div',{'class':'venz'}):
            Judul = i.ul.div.div.div.find('a',title=True)
            link = i.ul.div.div.div.find('a',href=True)
        
        linx = link['href']
        
        resp = r.get(linx).text
        psoup = BeautifulSoup(resp, "html.parser")

        print(C+""+R+" > "+W,Judul['title'])

        for cont2 in psoup.find_all('div',{'class':'smokettl'})[0]:
            jdl = cont2
            print(B+" [ ",jdl,"]"""+W+"")
        for cont1 in psoup.find_all('div',{'class':'smokeddl'})[0]:
            for tagres in cont1.find_all('strong'):
                reso = tagres.get_text()
                print(C+" ["+W+" Resolusi "+C+"]"+R+" >"+W+"",reso)                
                dlo1 = [dlx1['href'] for dlx1 in cont1.find_all('a',href=True)]
                for x1 in dlo1:
                    print(G+" ["+W+"" ,x1,""+G+"]"+W+"")
        print('')
        for cont2 in psoup.find_all('div',{'class':'smokettl'})[1]:
            jdl = cont2
            print(B+" [ ",jdl,"]"""+W+"") 
        for cont1 in psoup.find_all('div',{'class':'smokeddl'})[1]:
            for tagres in cont1.find_all('strong'):
                reso = tagres.get_text()
                print(C+" ["+W+" Resolusi "+C+"]"+R+" >"+W+"",reso)                
                dlo1 = [dlx1['href'] for dlx1 in cont1.find_all('a',href=True)]
                for x1 in dlo1:
                    print(G+" ["+W+"" ,x1,""+G+"]"+W+"")
        print('')
        for cont2 in psoup.find_all('div',{'class':'smokettl'})[2]:
            jdl = cont2
            print(B+" [ ",jdl,"]"""+W+"") 
        for cont1 in psoup.find_all('div',{'class':'smokeddl'})[2]:
            for tagres in cont1.find_all('strong'):
                reso = tagres.get_text()
                print(C+" ["+W+" Resolusi "+C+"]"+R+" >"+W+"",reso)                
            dlo1 = [dlx1['href'] for dlx1 in cont1.find_all('a',href=True)]
            for x1 in dlo1:
                print(G+" ["+W+"" ,x1,""+G+"]"+W+"")
        print('')
        for cont2 in psoup.find_all('div',{'class':'smokettl'})[3]:
            jdl = cont2
            print(B+" [ ",jdl,"]"""+W+"") 
        for cont1 in psoup.find_all('div',{'class':'smokeddl'})[3]:
            for tagres in cont1.find_all('strong'):
                reso = tagres.get_text()
                print(C+" ["+W+" Resolusi "+C+"]"+R+" >"+W+"",reso)                
                dlo1 = [dlx1['href'] for dlx1 in cont1.find_all('a',href=True)]
                for x1 in dlo1:
                    print(G+" ["+W+"" ,x1,""+G+"]"+W+"")
        print('')
        for cont2 in psoup.find_all('div',{'class':'smokettl'})[4]:
            jdl = cont2
            print(B+" [ ",jdl,"]"""+W+"") 
        for cont1 in psoup.find_all('div',{'class':'smokeddl'})[4]:
            for tagres in cont1.find_all('strong'):
                reso = tagres.get_text()
                print(C+" ["+W+" Resolusi "+C+"]"+R+" >"+W+"",reso)                
                dlo1 = [dlx1['href'] for dlx1 in cont1.find_all('a',href=True)]
                for x1 in dlo1:
                    print(G+" ["+W+"" ,x1,""+G+"]"+W+"")
        print('')
        for cont2 in psoup.find_all('div',{'class':'smokettl'})[5]:
            jdl = cont2
            print(B+" [ ",jdl,"]"""+W+"") 
        for cont1 in psoup.find_all('div',{'class':'smokeddl'})[5]:
            for tagres in cont1.find_all('strong'):
                reso = tagres.get_text()
                print(C+" ["+W+" Resolusi "+C+"]"+R+" >"+W+"",reso)                
                dlo1 = [dlx1['href'] for dlx1 in cont1.find_all('a',href=True)]
                for x1 in dlo1:
                    print(G+" ["+W+"" ,x1,""+G+"]"+W+"")
        print('')
        for cont2 in psoup.find_all('div',{'class':'smokettl'})[6]:
            jdl = cont2
            print(B+" [ ",jdl,"]"""+W+"") 
        for cont1 in psoup.find_all('div',{'class':'smokeddl'})[6]:
            for tagres in cont1.find_all('strong'):
                reso = tagres.get_text()
                print(C+" ["+W+" Resolusi "+C+"]"+R+" >"+W+"",reso)                
                dlo1 = [dlx1['href'] for dlx1 in cont1.find_all('a',href=True)]
                for x1 in dlo1:
                    print(G+" ["+W+"" ,x1,""+G+"]"+W+"")
        print('')
        for cont2 in psoup.find_all('div',{'class':'smokettl'})[7]:
            jdl = cont2
            print(B+" [ ",jdl,"]"""+W+"")
        for cont1 in psoup.find_all('div',{'class':'smokeddl'})[7]:
            for tagres in cont1.find_all('strong'):
                reso = tagres.get_text()
                print(C+" ["+W+" Resolusi "+C+"]"+R+" >"+W+"",reso)                
                dlo1 = [dlx1['href'] for dlx1 in cont1.find_all('a',href=True)]
                for x1 in dlo1:
                    print(G+" ["+W+"" ,x1,""+G+"]"+W+"")
        print('')
        for cont2 in psoup.find_all('div',{'class':'smokettl'})[8]:
            jdl = cont2
            print(B+" [ ",jdl,"]"""+W+"")
        for cont1 in psoup.find_all('div',{'class':'smokeddl'})[8]:
            for tagres in cont1.find_all('strong'):
                reso = tagres.get_text()
                print(C+" ["+W+" Resolusi "+C+"]"+R+" >"+W+"",reso)                
                dlo1 = [dlx1['href'] for dlx1 in cont1.find_all('a',href=True)]
                for x1 in dlo1:
                    print(G+" ["+W+"" ,x1,""+G+"]"+W+"")
        print('')
        for cont2 in psoup.find_all('div',{'class':'smokettl'})[9]:
            jdl = cont2
            print(B+" [ ",jdl,"]"""+W+"")
        for cont1 in psoup.find_all('div',{'class':'smokeddl'})[9]:
            for tagres in cont1.find_all('strong'):
                reso = tagres.get_text()
                print(C+" ["+W+" Resolusi "+C+"]"+R+" >"+W+"",reso)                
                dlo1 = [dlx1['href'] for dlx1 in cont1.find_all('a',href=True)]
                for x1 in dlo1:
                    print(G+" ["+W+"" ,x1,""+G+"]"+W+"")
        print('')
        for cont2 in psoup.find_all('div',{'class':'smokettl'})[10]:
            jdl = cont2
            print(B+" [ ",jdl,"]"""+W+"")
        for cont1 in psoup.find_all('div',{'class':'smokeddl'})[10]:
            for tagres in cont1.find_all('strong'):
                reso = tagres.get_text()
                print(C+" ["+W+" Resolusi "+C+"]"+R+" >"+W+"",reso)                
                dlo1 = [dlx1['href'] for dlx1 in cont1.find_all('a',href=True)]
                for x1 in dlo1:
                    print(G+" ["+W+"" ,x1,""+G+"]"+W+"")
                    wait()
    
    except r.ConnectionError as e:
        print(O+" Koneksi Error! "+W)
        wait()
    except r.Timeout as e:
        print(O+" Timeout! "+W)
        wait()
    except IndexError:
        wait()
    except AttributeError:
        print(R+" Tidak Ditemukan! "+W )
        wait()
