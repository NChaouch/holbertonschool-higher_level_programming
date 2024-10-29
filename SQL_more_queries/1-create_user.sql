-- creates the MySQL server user user_0d_1
-- creation script
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- for all databases (*.*) and according all privileges for user.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- for modification is acting 
FLUSH PRIVILEGES;
