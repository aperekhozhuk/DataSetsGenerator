# DataSetsGenerator
Web application that allows logged-in users to create dataset schemas and generate respective datasets in CSV format


## Running locally:
```
git clone https://github.com/aperekhozhuk/DataSetsGenerator
cd DataSetsGenerator
```
Next if you have docker:
```
docker build -t datasets_generator_demo .
docker run -p 8000:8000 datasets_generator_demo
```
Else:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 project/manage.py migrate
mkdir project/documents
```
Create superuser:
```
python3 project/manage.py createsuperuser
```
or run this command, it creates superuser without prompt ('admin', '1111'), only for linux
```
sh create_superuser.sh
```
Run server:
```
python3 project/manage.py runserver
```
Open in browser:
```
0.0.0.0:8000
```
Admin credentials:
```
username : admin
password : 1111
```
