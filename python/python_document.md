文档与报告
=========

## 收/发邮件
``` py
# poplib
import poplib
username = 'ixkungfu'
password = 'xxxxxxxx'
mail_server = 'pop.gmail.com'

p = poplib.POP3_SSL(mail_server)

for msg_id in p.list()[1]:
    print msg_id
    outf = open('%s.eml' % msg_id, 'w')
    outf.write('\n'.join(p.retr(msg_id)[1]))
    outf.close()

p.quit()



# imaplib
import imaplib
username = 'ixkungfu'
password = 'xxxxxxxx'
mail_server = 'pop.gmail.com'

i = imaplib.IMAP4_SSL(mail_server)
print i.login(username, password)
print i.select('INBOX')

for msg_id in i.search(None, 'ALL')[1][0].split():
    print msg_id
    outf = open('%s.eml' % msg_id, 'w')
    outf.write(i.fetch(msg_id), '(RFC822)').[1][0][1])
    outf.close()

i.quit()



# smtp
import smtplib
mail_server = 'localhost'
mail_server_port = 25
from_addr = 'sender@example.com'
to_addr = 'receiver@example.com'

from_header = 'From: %s\r\n' % from_addr
to_header = 'To: %s\r\n' % to_addr
subject_header = 'Subject: nothing intersting'

body = 'This is a not-very-interestring email'

email_message = '%s\n%s\n%s\n\n%s' % (from_header, to_header, subject_header, body)

s.smtplib.SMTP(mail_server, mail_server_port)
s.quit()



# 发送附件 email

```

## 文档格式模块
* ReST
* docutils
* texttile

## 信息格式化模块
* gdchart
* shelve
* itertools

## PDF模块
reportlab.pdfgen
``` py
from reportla.pdfgen import canvas

def hello():
    c = canvas.Canvas('helloworld.pdf')
    c.drawString(100, 100, 'Hello World')
    c.showPage()
    c.save()

if __name__ == '__main__':
    hello()
```
# Trac Wiki和问题追踪系统
