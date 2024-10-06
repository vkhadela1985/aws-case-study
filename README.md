# AWS Case Study

## Refer below steps:

### Prepare a database:
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
4. For creating aws mysql RDS, Refer: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html#CHAP_GettingStarted.Creating.MySQL   

### Create application stack 
1. Create a ECR Repository
2. Use below commands to build the docker image and push into ECR
   ```
   aws ecr get-login-password --region <aws_region> | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<aws_region>.amazonaws.com
   docker build -t <ecr_repo_name> .
   docker tag app-ecr-repo:latest <account_id>.dkr.ecr.<aws_region>.amazonaws.com/<ecr_repo_name>:<tag>
   docker push <account_id>.dkr.ecr.<aws_region>.amazonaws.com/<ecr_repo_name>:<tag>
   ```
3. Make sure where you are building this docker image should have ECR access. Refer: https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html
4. Created ECS Cluster, ECS Task Definintion, ECS Service. In ECS service, you will get an options for creating security group, target group and application load balancer and listner.
5. To create ECS Cluster, refer https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-cluster-console-v2.html
6. To create ECS task definition, refer https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html
7. In task definition, you also need to pass the env variables for MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
8. To create ECS service, refer https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html
9. You can view the webpage on browser using LoadBalancer endpoint

### Monitoring Setup
1. Create a SNS topic https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html
2. Create SNS subscription https://docs.aws.amazon.com/sns/latest/dg/sns-email-notifications.html
3. Create Cloudwatch Alarms for ECS  
   


   


   
