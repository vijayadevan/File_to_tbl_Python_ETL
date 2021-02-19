import getpass
import csv

from DBConn import DBConn

if __name__ == '__main__':
    print('Enter the Password for SYSTEM Schema: ')
    pwd = getpass.getpass('')
    # pwd = input()
    CONN_INFO = {
        'host': 'localhost',
        'port': 1521,
        'user': 'SYSTEM',
        'psw': pwd,
        'service': 'orcl'
    }

    db = DBConn(CONN_INFO)

    # Read the Customers data from the Source File
    with open('C:\\Users\\Admin\\Desktop\\assessment\\Source_file\\CUSTOMERS_DATA_20210219.172652.txt', 'r') as file:
        reader = csv.reader(file, delimiter='|')
        line_count = 0
        data = []
        for line in reader:
            line_count += 1
            if line_count != 1:
                data.append((line[2], line[3], line[4], line[5], line[6], line[7],
                                  line[8], line[9], line[10], line[11]))

    # Pre-delete condition for CUSTOMER_STG table
    db.exec_query('truncate table SYSTEM.customer_stg')
    stg_load_sql = f'insert into SYSTEM.customer_stg (CUST_NM, CUST_ID, CUST_OPEN_DT, LAST_CONSUL_DT, VAC_TYP, ' \
                   f'DOC_CONSULTD, STATE, COUNTRY, DT_OF_BIRTH, ACTIVE_CUST_FLAG) ' \
                   f'values (:1, :2, to_date(:3, \'YYYYMMDD\'), to_date(:4, \'YYYYMMDD\'), :5, :6, :7, :8, ' \
                   f'to_date(:9, \'DDMMYYYY\'), :10)'
    db.exec_many_query(stg_load_sql, data)
    print(f'{line_count - 1} rows were inserted into the table from the file')

    # Declaring region specific tables and Country associated with it for splitting the data into respective countries
    dict_region_specific = {
        'CUSTOMER_USA': 'USA',
        'CUSTOMER_AU': 'AU',
        'CUSTOMER_IND': 'IND',
        'CUSTOMER_NYC': 'NYC',
        'CUSTOMER_PHIL': 'PHIL'
    }
    for region in dict_region_specific.keys():
        #Pre-delete condition for Region specific table
        db.exec_query(f'truncate table SYSTEM.{region}')
        rgn_tbl_load_sql = f'insert into SYSTEM.{region} (CUST_NM, CUST_ID, CUST_OPEN_DT, LAST_CONSUL_DT, VAC_TYP, ' \
                   f'DOC_CONSULTD, STATE, COUNTRY, DT_OF_BIRTH, ACTIVE_CUST_FLAG) select CUST_NM, CUST_ID, ' \
                   f'CUST_OPEN_DT, LAST_CONSUL_DT, VAC_TYP, DOC_CONSULTD, STATE, COUNTRY, DT_OF_BIRTH, ' \
                   f'ACTIVE_CUST_FLAG from SYSTEM.customer_stg where trim(country) = \'{dict_region_specific[region]}\''
        db.exec_query(rgn_tbl_load_sql)
        print(f'SYSTEM.{region} is loaded with {dict_region_specific[region]} country records')
