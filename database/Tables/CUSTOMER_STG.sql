CREATE TABLE system.customer_stg (
    cust_nm            VARCHAR2(255) NOT NULL,
    cust_id            VARCHAR2(18) NOT NULL,
    cust_open_dt       DATE NOT NULL,
    last_consul_dt     DATE,
    vac_typ            CHAR(5),
    doc_consultd       CHAR(255),
    state              CHAR(5),
    country            CHAR(5),
    dt_of_birth        DATE,
    active_cust_flag   CHAR(1),
    CONSTRAINT cust_nm_pk PRIMARY KEY ( cust_nm )
);