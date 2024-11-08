-- creates the MySQL server user user_0d_1
-- creation script
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
-- privilege for the database according to the user 
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- for modification is acting
FLUSH PRIVILEGES;

