#!/bin/bash
# declare STRING variable
STRING="utworzenie bazy danych i weryfikacja zaleznosci"
#print variable on a screen
echo $STRING
#exec sqlite3 database.db | echo -e ".exit"
exec sqlite3 database.db < install_db.sql
