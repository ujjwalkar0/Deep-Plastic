This is the source code of https://oceanplastic.herokuapp.com/

Various problem occurs when It runs on heroku cloud, but it works fine in local machine

Run following command to install it on local machine. ( In Linux)

#### Install python and pip in local machine

```bash
sudo apt install python3 python3-pip  
```
#### Install virtualenv

```bash
python3 -m pip install virtualenv 
```

#### Change Directory to website
```
cd /path\ of\ Website\
```

#### Setup a virtualenv
```
python3 -m virtualenv venv 
```

#### Active vitualenv
```
source venv/bin/activate
```

#### Install Require packages
```
pip install -r requirement.txt
```

#### Migrate database
```
python manage.py migrate
```

#### Run on localhost
```bash
python manage.py runserver
```
