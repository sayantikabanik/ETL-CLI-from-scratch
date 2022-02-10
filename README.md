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
### Creating user
Setting the user credentials using flask fab
```shell
FLASK_APP=airflow.www.app flask fab create-admin
```