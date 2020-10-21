# python-poplib

## 邮箱登录、获取邮件内容、附件写入本地

~~~python
import poplib,email
from email.header import decode_header
from email.parser import Parser


# 邮件地址, 口令和POP3服务器地址:
download_email = 'valuation_bill@mycapital.net'
password = 'GdJaBcjKJuKZfK2Z'
pop3_server = 'pop.qiye.163.com'

server = poplib.POP3_SSL(pop3_server)
server.user(download_email)
server.pass_(password)


def decode_str(aStr):
    """
    字符编码转换
    """
    #decode_header方法会将字符串还原成二进制 并获取该字符串的正确解析方式
    #返回值：[(bytes,charset)]
    bytes, charset = decode_header(aStr)[0]
    if charset:
        value = bytes.decode(charset)
        return value
    else:
        return None
    

#获取所有邮件item
resp, mails, octets = server.list()

# 倒序遍历邮件,取最新的300份
index = len(mails)-300 if len(mails)>300 else 0
for i in range(len(mails),index, -1):
    # resp:响应 lines:每一行的数据组成的列表 octets:邮件大小
    resp, lines, octets = server.retr(i)
    # 换行符拼接二进制文件 并utf-8解码，忽略其中有异常的编码，仅显示有效的编码
    msg_content = b'\r\n'.join(lines).decode('utf-8', 'ignore')
    # 将字符串转化为Message对象
    msg = Parser().parsestr(msg_content)
    # 邮件标题
    subject = decode_str(msg.get('Subject'))
    
    
    # msg.walk()返回一个generator 包含message对象 (邮件、文本、附件)
	for part in msg.walk():
        file_name = part.get_filename()
        if file_name:# 文本没有文件名称 此处过滤掉
            file_name = decode_str(file_name)# 附件名称解码
            data=part.getpayload(decode=True)# 获取附件内容
            with open("hehe.txt","wb")as file:
                file.write(data)
            
~~~

