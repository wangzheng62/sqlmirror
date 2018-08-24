USE master;
CREATE CERTIFICATE host_b_cert
	AUTHORIZATION host_b_user
	FROM FILE = 'E:\test\host_b_cert.cer'
GO

USE master;
GRANT CONNECT ON ENDPOINT::endpoint_mirror TO host_b_login;
GO