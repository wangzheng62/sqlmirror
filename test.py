import os,telnetlib,pymssql,time
#数据库
HOST_A_DB={
    'host':'192.168.0.180',
    'user':'sa',
    'password':'Ibm123456.'
}
HOST_B_DB={
    'host':'192.168.0.181',
    'user':'sa',
    'password':'Ibm123456.'
}
#服务器
HOST_A={'ip':'192.168.0.180',
        'username':'administrator',
        'password':'Ibm123'}
HOST_B={'ip':'192.168.0.181',
        'username':'administrator',
        'password':'Ibm123'}
#ftp服务器
FTP={
    'ip':'192.168.0.111',
    'username':'ftpuser',
    'password':'123456'
}
#
FILENAME='TEST.TXT'
HOME='c:\\Users\\Administrator'
#测试
def dotest():
    #数据库测试
    try:
        conn = pymssql.connect(**HOST_A_DB)
        conn.close()
        print('数据库A测试连接成功')
    except Exception:
        print('数据库A测试连接失败')
    try:
        conn=pymssql.connect(**HOST_B_DB)
        conn.close()
        print('数据库B测试连接成功')
    except Exception:
        print('数据库B测试连接失败')
    #telnet测试
    tn = telnetlib.Telnet()
    try:
        tn.open(host=HOST_A['ip'],port=23,timeout=20)
        tn.read_until(b'login: ')
        tn.write(HOST_A['username'].encode('ascii') + b'\r')
        tn.read_until(b'password:', timeout=3)
        tn.write(HOST_A['password'].encode('ascii') + b'\r')
        tn.close()
        print('服务器A测试连接成功')
    except Exception:
        print('服务器A测试连接失败')
    try:
        tn.open(host=HOST_B['ip'],port=23,timeout=20)
        tn.read_until(b'login: ')
        tn.write(HOST_B['username'].encode('ascii') + b'\r')
        tn.read_until(b'password:', timeout=3)
        tn.write(HOST_B['password'].encode('ascii') + b'\r')
        tn.close()
        print('服务器B测试连接成功')
    except Exception:
        print('服务器B测试连接失败')
    #FTP服务器测试
    tn.open(host=HOST_A['ip'], port=23, timeout=5)
    msg = tn.read_until(b'login: ')
    print(msg.decode('gbk'))
    tn.write(HOST_A['username'].encode('ascii') + b'\r')
    msg = tn.read_until(b'password:')
    print(msg.decode('gbk'))
    tn.write(HOST_A['password'].encode('ascii') + b'\r')
    msg = tn.read_until(b'>')
    print(msg.decode('gbk'))
    print('ftp {}'.format(FTP['ip']))
    tn.write('ftp {}'.format(FTP['ip']).encode('ascii') + b'\r')
    time.sleep(3)

    print(2)
    tn.write(FTP['username'].encode('ascii') + b'\r')
    msg = tn.read_until(b':')
    print(msg.decode('gbk'))
    tn.write(FTP['password'].encode('ascii') + b'\r')
    msg = tn.read_until(b'>')
    print(msg.decode('gbk'))
#
if __name__=='__main__':
    dotest()
    tn = telnetlib.Telnet()
    tn.open(host=HOST_A['ip'], port=23, timeout=10)
    tn.interact()
    tn.read_until(b'login: ')
    tn.write(HOST_A['username'].encode('ascii') + b'\r')
    tn.read_until(b'password:')
    tn.write(HOST_A['password'].encode('ascii') + b'\r')
    #
    tn.read_until(b'>')
    tn.write('dir c:'.encode('ascii')+b'\r')
    msg=tn.read_until(b'or>')
    tn.write('mkdir test'.encode('ascii')+b'\r')
    msg = tn.read_until(b'or>')
    print(type(msg))
    print(msg.decode('gbk'))
    if '已经存在'in msg.decode('gbk'):
        print('文件夹失败')
    else:
        print('成功')

