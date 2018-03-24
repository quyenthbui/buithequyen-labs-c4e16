from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL


url = 'https://www.apple.com/itunes/charts/songs/'

html_content = urlopen('https://www.apple.com/itunes/charts/songs/').read().decode('utf8')

soup = BeautifulSoup(html_content,'html.parser')

ul = soup.find('section','section chart-grid')

li_list = ul.find_all('li')

#datas = []

#for li in li_list:
    #data = {}
    #data['song name'] = li.h3.a.string
    #data['artist'] = li.h4.a.string
    #datas.append(data)
    #print(datas)

#pyexcel.save_as(records=datas, dest_file_name='itunestest.xlsx')

options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}

dl = YoutubeDL(options)

#options = {
    #'default_search': 'ytsearch',
    #'max_downloads': 1,
    #'format': 'bestaudio/audio'
#}


for li in li_list:
    songname = li.h3.a.string
    artist = li.h4.a.string
    #print(songname+artist)
    dl.download([songname + ' ' + artist])
