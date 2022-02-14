# ETL-from-scratch
Demonstration of various OSS technologies to construct an ETL pipeline

### Dependency management using conda
Steps to create environment 
```shell
conda env create --file environment.yml
```
```shell
conda activate etl
```
```shell
conda list
```
```shell
conda info
```
```shell
conda deactivate
```
### Creating user and running the webserver
1(a). Setting the user credentials using `flask fab`, 
follow the instructions on the command line
```shell
FLASK_APP=airflow.www.app flask fab create-admin
```
1(b). Creating user using airflow's `create users command`
```shell
airflow users create 
--username admin 
--password your_password 
--firstname your_first_name 
--lastname your_last_name 
--role Admin 
--email your_email@some.com
```
2. Run the below command to confirm if the user is created
```shell
airflow users list
```
3. Initialise airflow database
```shell
airflow db init
```
5. Setup mysql database and secure it using password - [macOS setup instructions](https://flaviocopes.com/mysql-how-to-install/)

6. Make changes in the `airflow.cfg`

7. Star the airflow webserver and schedular 
```shell
airflow webserver
airflow schedular
```


### References
- https://insaid.medium.com/setting-up-apache-airflow-in-macos-2b5e86eeaf1
