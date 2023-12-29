#!/bin/bash
USER='user'
PASS='password'
PORT=3306
HOST='hostname'
DBASE='databasename'
query='SELECT * FROM tablename'
mysql -u$USER -p$PASS -P$PORT -h$HOST -D$DBASE <<EOF
$query
EOF
