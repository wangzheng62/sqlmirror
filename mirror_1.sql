/*'1,�������ݿ�����Կ'*/
use master;
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Ibm123456.';
GO
/*'2,������վ֤��'*/
USE MASTER;
CREATE CERTIFICATE host_a_cert
  WITH SUBJECT = 'HOST_A certificate for database mirroring',
  EXPIRY_DATE = '12/31/2099';
GO
/*'3,�����˵�'*/
CREATE ENDPOINT endpoint_mirror
STATE = STARTED
AS TCP(LISTENER_PORT=10086)
FOR DATABASE_MIRRORING
  (
  authentication=certificate host_a_cert,
  ROLE = ALL );
GO

/*'4,����֤�鵽�ļ�'*/
BACKUP CERTIFICATE host_a_cert TO FILE = 'E:\test\host_a_cert.cer';

/*'��վ'
'������¼��'*/
USE master;
CREATE LOGIN host_b_login
   WITH PASSWORD = 'Ibm123456.';
GO
/*'�����û�'*/
USE master;
CREATE USER host_b_user FOR LOGIN host_b_login;
GO