-----------------------------------------------------------------------------------------------------
-- File name : DB_Runscript.sql
-- Description : To create CUSTOMER Staging and Region specific tables.
-----------------------------------------------------------------------------------------------------

SPOOL DB_Runscript.txt

SET TIME ON
SET DEFINE OFF
SET TIMING ON
SET SQLBLANKLINES ON
SET SERVEROUTPUT ON

prompt 'Creation of Tables in System Schema'
connect SYSTEM@ORCL
@@ ./Tables/CUSTOMER_STG.sql
@@ ./Tables/CUSTOMER_PHIL.sql
@@ ./Tables/CUSTOMER_USA.sql
@@ ./Tables/CUSTOMER_AU.sql
@@ ./Tables/CUSTOMER_IND.sql
@@ ./Tables/CUSTOMER_NYC.sql

SHOW ERRORS
SPOOL OFF