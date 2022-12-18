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
    print(C+" |  .  \ "+R+" |  |\   |"+C+" github.com/"+R+"rzyware")
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

        smokettl_list = psoup.find_all('div',{'class':'smokettl'})
        smokeddl_list = psoup.find_all('div',{'class':'smokeddl'})
        for cont2, cont1 in zip(smokettl_list, smokeddl_list):
            jdl = cont2.text
            print(B+" [ ",jdl,"]"""+W+"")
            for tagres in cont1.find_all('strong'):
                reso = tagres.get_text()
                print(C+" ["+W+" Resolusi "+C+"]"+R+" >"+W+"",reso)
                dlo1 = [dlx1['href'] for dlx1 in cont1.find_all('a',href=True)]
                for x1 in dlo1:
                    print(G+" ["+W+"" ,x1,""+G+"]"+W+"")
            print('')
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
