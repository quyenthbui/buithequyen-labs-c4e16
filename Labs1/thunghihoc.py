from gmail import GMail
from gmail import Message
from random import choice
from datetime import datetime, time

gmail = GMail('thequyentechkid@gmail.com','123!@#qweQWE')
html_content = """<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC&nbsp;</strong></p>
<p style="text-align: left;">Em ch&agrave;o thầy&nbsp;<br /><br /></p>
<p style="text-align: left;">T&ecirc;n em l&agrave;<span style="color: #ff0000;"> Nguyễn Văn A&nbsp;</span></p>
<p style="text-align: left;">H&ocirc;m nay {{sickness}} em th&iacute;ch th&igrave; em nghỉ thầy l&agrave;m thầy em hơi l&acirc;u rồi đấy</p>
<p style="text-align: left;">Văn A</p>"""
reasons =['trời đẹp mây cao','trời mù mưa giông','trời quang mây tạnh','mây giông vần vũ']
reason = choice(reasons)
html_content = html_content.replace("{{sickness}}",reason)
msg = Message('Test Message',to='techkidsc4e16@gmail.com',html=html_content)
while True:
    time_now = datetime.now().time().hour
    if time_now == 7:
        gmail.send(msg)
