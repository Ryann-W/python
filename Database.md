Database - contains many tables

Relation(or table) - contains tuples and attributes

Tuple (or row) - a set of fields that generally represents an "object" like a person or a music track

Attribute(also column or field) -  one of possibly many elements of data corresponding to the object represented by the row
(reference form FreeCodeCamp)

A realtion is defined as a set of tuples that have the same attributes. A tuple usually represents an object and information about that object. Objects are typically physical objects or concepts. A relation is usually described as a table, which is organized into rows and columns. All the data referenced by an attribute are in the same domain and conform to the same constraints(Wikipedia)(FreeCodeCamp)

            
---------- ---------- ---------- ---------- ----------
  TITLE   |  RATING  |  LEN     |          |          |
---------- ---------- ---------- ---------- ---------- 
   ABOUT  |     3    |  23      |          |          |
---------- ---------- ---------- ---------- ---------- 
   MAKE   |     4    |  34      |          |          | 
---------- ---------- ---------- ---------- ---------- 
          |          |          |          |          |
---------- ---------- ---------- ---------- ---------- 

Columns / Attributes
Rows / Tuples
Tables / Relations
                        
SQL = Strcutured Query Language is the language we use to issue commands to the databse

Create a table / Retrieve some data / Insert data / Delete data

Common database Systems

Three major Database Management System in wide use

Oracle - Large, commercial, enterprise-scale, very very tweakable

MySql - Simpler but very fast and scalable - commercial open source

SqlServer - Very nice - from Microsoft(also Access)

Many other smaller projects, free and open source 
HSQL, SQLite, Postgres... (From FreeCodeCamp)

For some basic operations in SQLite

SQL : Insert - The insert statement inserts a row into table

INSERT INTO User(name,email)VALUES('Mike','mike@outlook.com')
(multiple lines use semi comma ;)

SQL : Delete - Deletes a row in a table based on a selection criteria

DELETE FROM Users WHERE email='mike@outlook.com'

SQL : Updata - Allows the updating of a field with a where clause

UPDATE Users SET name='Charles'WHERE email='csev@umich.edu'

Retrieving Records: Select

The select statement retrieves a group of records - you can either retrieve all the records or a subset of the records with a WHERE clause

SELECT*FROM Users
SELECT*FROM Users WHERE email='csev@umich.edu'