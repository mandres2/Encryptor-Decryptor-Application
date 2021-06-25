create table ACCOUNT (
    ACCOUNT_ID int identity not null,
    AVAIL_BALANCE float,
    CLOSE_DATE datetime,
    LAST_ACTIVITY_DATE datetime,
    OPEN_DATE datetime not null,
    PENDING BALNCE float,
    STATUS varchar(10),
    CUST_ID int,
    OPEN_BRANCH_ID int not null,
    OPEN_EMP_ID int not null,
    PRODUCT_CD varchar(10) not null,
    primary key (ACCOUNT_ID)
);