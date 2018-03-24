from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel


url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

html_content = urlopen(url).read().decode("utf8")

soup = BeautifulSoup(html_content, "html.parser")


ul = soup.find("table",id="tableContent")

tr_list = ul.find_all("tr")

datas=[]
fields = ['Nội dung','Quý 4/2016','Quý 1/2017','Quý 2/2017','Quý 3/2017']
for tr in tr_list:
    td_list = tr.find_all("td")
    td_list = td_list[:-1]
    if len(td_list) == 0:
        continue
    data={}
    for i in range(len(fields)):
        data[fields[i]] = td_list[i].string
    datas.append(data)

pyexcel.save_as(records=datas,dest_file_name="vinamilk.xlsx")
