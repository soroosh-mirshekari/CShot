CREATE DATABASE schot;
CREATE USER 'my_user'@'localhost' IDENTIFIED BY 'my_password';
GRANT ALL PRIVILEGES ON my_local_db.* TO 'my_user'@'localhost';
FLUSH PRIVILEGES;