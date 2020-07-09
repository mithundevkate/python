'''Write pseudo-SQL statements to create database tables to store the products of a basic webshop.
'''Each product has a name, a price, a creation date and may belong to several categories. Categories have a name and a flag to indicate whether the category is private or public.
'''Write a SQL query to find the list of products that belong to more than 5 public categories.'''

1. create table products (name varchar2(50) NOT NULL,price number(20) NOT NULL,creation_date DATE NOT NULL , categories varchar2(20) NOT NULL,flag varchar(10) DEFAULT 'private' or 'public');
2. Select TOP 5 * from products where flag ='public';
