# AWS Case Study

## To prepare the database use below steps:
1. Create a AWS MySQL RDS in private subnet.
2. Login to that RDS using below command
   ```
   mysql -h your-rds-endpoint.rds.amazonaws.com -u your-username -p
   ```
3. Once connected to the RDS instance, run the following SQL command to create a new database:
   ```
   CREATE DATABASE myappdb;
   USE myappdb;

   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100),
       email VARCHAR(100)
   );

   INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
   INSERT INTO users (name, email) VALUES ('Jane Smith', 'jane@example.com');
   ```



   


   
