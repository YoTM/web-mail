#!/bin/bash

echo "Starting Mysql DataBase"
sudo /etc/init.d/mysql start

echo "Create new user admin"
mysql -uroot -e "CREATE USER 'admin'@'localhost'"

echo "Set password to user admin"
mysql -uroot -e "SET PASSWORD FOR 'admin'@'localhost' = PASSWORD('admin123')"

echo "Create scheme with name askapp"
mysql -uroot -e "CREATE DATABASE askapp"

echo "Give rights on this shceme for admin"
mysql -uroot -e "GRANT ALL ON askapp.* TO 'admin'@'localhost'"




