USE master;
GO
ALTER DATABASE test01 
SET RECOVERY FULL;
GO

BACKUP DATABASE test01 
    TO DISK = 'e:\test\test01.bak' 
    WITH FORMAT
GO

BACKUP LOG test01 
    TO DISK = 'E:\test\test01-log.bak' 
GO