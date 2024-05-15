//COMANDOS PARA LA CREACION DE USUARIO EN BASE DE DATOS ORACLE

ALTER SESSION SET "_ORACLE_SCRIPT" = TRUE;

CREATE USER ferremas IDENTIFED BY ferremas;

GRANT CONNECT, RESOURCE TO ferremas;

ALTER USER ferremas DEFAULT TABLESPACE USERS QUOTA UNLIMITED ON USERS;

//COMANDOS PIP PARA PYTHON

pip install djangorestframework
pip install requests
pip install oracledb

//COMANDOS EN CASO DE MODIFICAR LISTENER

LISTENER:

#BORRAR GUIONES DEL LISTENER
"
-# listener.ora Network Configuration File: c:\Oracle\Product\OraDB19c\NETWORK\ADMIN\listener.ora
-# Generated by Oracle configuration tools.

SID_LIST_LISTENER =
  (SID_LIST =
    (SID_DESC =
      (GLOBAL_DBNAME = orcl)
      (ORACLE_HOME = c:\Oracle\Product\OraDB19c)
      (SID_NAME = orcl)
    )
  )
LISTENER =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = localhost)(PORT = 1521))
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
    )
  )
"
//COMANDOS

lsnrctl stop //PARA PARAR LISTENER

lsnrctl status //PARA REVISAR ESTADO DEL LISTENER

lsnrctl start //PARA INICIAR LISTENER

