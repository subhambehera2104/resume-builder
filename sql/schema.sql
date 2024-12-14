CREATE USER 'flask_app'@'localhost' IDENTIFIED BY '12345678';
GRANT ALL ON *.* TO 'flask_app'@'localhost' WITH GRANT OPTION;

create database resume_builder;
use flask_db;

CREATE TABLE IF NOT EXISTS users (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL,
password VARCHAR(255) NOT NULL
);
insert into users(name, email, password)
value("subham behera", "subhambehera2104@gmail.com", "12345678");

CREATE TABLE user_information (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name varchar(50) NOT NULL,
  email varchar(50) NOT NULL,
  phone varchar(10) NOT NULL,
  date_of_birth, DATE NOT NULL,
  website varchar(1024),
  address varchar(100) NOT NULL,
  gender varchar(10) NOT NULL,
  user_img varchar(255),
  about varchar(255),
  skill varchar(255),
  work_experience varchar(255),
  hobbies varchar(255)
);