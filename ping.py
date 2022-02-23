import os, sys
from bs4 import BeautifulSoup as bs
import requests
import subprocess
from colorama import Fore, Back, Style ,init
from prettytable import PrettyTable

def scrape(url):
  g = requests.get(url)
  soup = bs(g.text, "html.parser")
  table = soup.find('table', {'class':'table_lst table_lst_srs'})
  trs = table.findAll('tr')
  return trs

def main():
  init()
  url = input('Enter the url : ') if len(sys.argv) == 1 else sys.argv[1]
  t = PrettyTable(['ping', 'ip','players','ratio','map','name','index'])
  trs = scrape(url)
  os.system("cls")

  index = 1
  for tr in trs[1:-1]:
    td = tr.findAll('td')
    name = td[2].text.strip()
    players = td[3].text.strip()
    ip = td[6].text.strip()
    map = td[7].text.strip()
    ip_no_port= tr.find('span', attrs={'class':'ip'}).text.strip()
    p=subprocess.Popen(["ping","-n","1","-w","1000",ip_no_port], stdout = subprocess.PIPE)
    comm = str(p.communicate()[0])
    try:
      ratio = round(int(players.split('/')[0])/int(players.split('/')[1]), 2)
    except Exception:
      ratio = 0
    if 'Average' in comm:
      ping = int(comm.split('ms')[-2].split("=")[-1].strip())
      t.add_row([ping,ip,players,ratio,map,name,index])
    else:
      t.add_row([999,ip, players,ratio,map,name,index])		
    os.system("cls")
    print(t)
    index += 1
  
  os.system("cls")
  sort = sys.argv[2] if len(sys.argv) == 3 else 'ping'
  print(t.get_string(sortby=sort)) if sort != "ratio" else print(t.get_string(sortby=sort, sort_key=lambda row:-row[0]))
  print(f'we have {len(trs)-2} servers')

  while True:
    sort = input("enter the key to sort with {ping, ip, players, ratio, map, name, index}: ").lower().strip()
    if sort in t.field_names:
      try:
        os.system("cls")
        print(t.get_string(sortby=sort)) if sort != "ratio" else print(t.get_string(sortby=sort, sort_key=lambda row:-row[0]))
      except Exception as e:
        print(e)
    else:
      print("Not a valid field name!")

if __name__ == "__main__":
  main()

