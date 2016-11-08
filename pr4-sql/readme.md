# Práctica 4 - SQL

## Sqlite3 commands

### Basics

Login into the database:

```
# ../pr4-sql
sqlite3 Libreria
```

To turn readable output:

```
sqlite> .mode column
sqlite> .headers on
```

To show all database tables:

```
sqlite> .tables
```

To show all records in a table:

```
sqlite> select * from <table_name>;
```

### CSV Export

```
sqlite> .header on
sqlite> .mode csv
sqlite> .once output_file.csv
```
