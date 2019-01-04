CREATE TABLE books (
    id     INTEGER   PRIMARY KEY AUTOINCREMENT,
    title  TEXT (50) NOT NULL,
    price  INTEGER   CHECK (price >= 0),
    author TEXT (50)
);

insert into books (title,price,author) values('Java Complete Reference',750,'Herbert Schildt')
insert into books (title,price,author) values('Hibernate in Action',650,'Gavin King')

