# Install mongo db for running the application
http://docs.mongodb.org/manual/tutorial/install-mongodb-on-red-hat/

# Install and setup  virtualenvironment

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

# NOTE : do these changes before executing these are the config files

```
cp  helpers/settings.py.prod  helpers/settings.py.local
#make changes in settings local with valid key and password
ln -sf helpers/settings.py.local helpers/settings.py
```

This is making use of an external cloud telephony service for alerting using call and sms named exotel[http://exotel.in/]
So inorder to run the application one need to register and have API key and token from the account.
