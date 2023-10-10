# About
This project is a Q&A platform developed with Flask and Bootstrap.

# Run
- Create a ```config.py``` file and put under the root folder, the template at the end.
- Make sure you have MySQL running on device
- Execute ```flask db init```
- Execute ```flask db migrate```
- Execute ```flask db upgrade```
- Run by ```flask run```
  
# config.py
This is a template of config.py, please create your own and put under the root folder.
```python
HOSTNAME = "localhost"
PORT = 3306
USERNAME = "root"
PASSWORD = ""
DATABASE = "flask_qa"
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}" \
                          f"?charset=utf8"

MAIL_SERVER = "smtp.gmail.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "xxxxxxx@gmail.com"
MAIL_PASSWORD = "xxxxxxxxxxxxxx"
MAIL_DEFAULT_SENDER = "xxxxxxx@gmail.com"

SECRET_KEY = "hvir'vkr;j`niowv,vrwq"
```