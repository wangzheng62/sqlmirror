'创建端点'
CREATE ENDPOINT endpoint_mirror
STATE = STARTED
AS TCP(LISTENER_PORT=10086)
FOR DATABASE_MIRRORING
  (ROLE = ALL );
GO
'创建数据库主密钥'

CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Ibm123456.';
GO
'创建出站证书'
USE MASTER;
CREATE CERTIFICATE host_a_cert
  WITH SUBJECT = 'HOST_A certificate for database mirroring',
  EXPIRY_DATE = '12/31/2099';
GO
'备份证书到文件'
BACKUP CERTIFICATE host_a_cert TO FILE = 'C:\USER\Administrator\host_a_cert.cer';

'入站'
'创建登录名'
USE master;
CREATE LOGIN host_b_login
   WITH PASSWORD = 'Ibm123456.';
GO
'创建用户'
USE master;
CREATE USER host_b_user FOR LOGIN host_b_login;
GO
'证书用户关联'
USE master;
CREATE CERTIFICATE host_b_cert
   AUTHORIZATION host_b_user
   FROM FILE = 'C:\host_b_cert.cer'
GO
''
USE master;
GRANT CONNECT ON ENDPOINT::endpoint_mirror TO host_b_login;
GO