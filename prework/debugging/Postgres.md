0


Try using psql's \copy command, as the hint in the error message you quoted suggests. COPY FROM tells the server to open the file and process it, while \copy reads the file client side and then passes the output to the server, see https://stackoverflow.com/a/19466558/12760895

Open the psql console with 
`psql -U postgres -d [yourdb]` then run

```
\copy [target_table] from '/tmp/test.csv' DELIMITER ',' CSV;
```