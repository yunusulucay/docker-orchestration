#!/bin/bash
psql --username=root -c "CREATE DATABASE test_db2;"
psql --username=root -c "CREATE USER test_user2 WITH ENCRYPTED PASSWORD 'test_password2';"
psql --username=root -c "GRANT ALL PRIVILEGES ON DATABASE test_db2 TO test_user2;"
psql --username=root -c "CREATE TABLE IF NOT EXISTS test_table2(id SERIAL PRIMARY KEY NOT NULL, title TEXT);"
