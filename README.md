# Massey_Project_7_Wonders
7 Wonders implementation for Massey capstone project

## Getting Started

#### Installs
* Ensure you have python 2.7 running `python --version` to check
* Ensure you have pip installed `pip --version` to check
* Install the following python modules
```
pip install flask flask_script flask_migrate flask_bcrypt pytest flask_testing psycopg2
```
* Ensure you have node installed at least version 7 `node -v` to check
* Ensure you have npm installed at least version 4 `npm -v` to check

#### Create DB
* Set up postgres locally [link](http://postgresguide.com/setup/install.html)
* You may want a postgres interface such as [pgAdmin](https://www.pgadmin.org/)
* Create a database called 7-wonders in your interface or run `CREATE DATABASE 7-wonders` in your postgres shell
* Run the following to set the environment
OSX/Linux:
```
export DATABASE_URL="postgresql://username:password@localhost:port/7-wonders"
```
or on Windows:
```
$env:DATABASE_URL="postgresql://username:password@localhost:port/7-wonders"
```
* Run this script and it will create the tables in your database
```
python manage.py create_db
```

To update database after adding to the database model, use:
```
python manage.py db migrate
python manage.py db upgrade
```


#### Install Front-End Requirements
```sh
cd static
npm install
```

#### Run Back-End

```sh
python manage.py runserver
```
Open localhost:5000 to view

You will need a production frontend build if you are running this way

#### Test Back-End

```sh
python test.py tests/
```

#### Run Front-End

```sh
cd static
npm start
```
Open localhost:3000 to view

#### Build Front-End for production

```sh
npm run build:production
```

#### Test Front-End
```sh
cd static
npm run test
```
Will run the frontend test suite

If you want to run the test in watch mode run:
`npm run test:watch`

#### Browser tests
Step 1:
Setup Selenium.
Download gecko web driver [here]() and ensure you add to your system path variable the folder you download the driver to.
Run selenium ```java -jar selenium.jar``` from inside the static/selenium folder.

Step 2:
``npm run test:browser`` will kick off the nightwatch tests.

Browser tests are located in static/tests/browser 

### Deployment
The app is running on a hobby dyno instance on Heroku
[massey7wonders.herokuapp.com](https://massey7wonders.herokuapp.com)

A new deployment is trigged upon a new merge to the master branch.

This then picks up two Heroku buildpacks, a python build pack, and a nodejs buildpack.

The python buildpack installs the dependencies inside the requirements.txt file

The nodejs buildpack installs the dependencies inside the package.json. Because this has to be at the root level, we direct this to access the package.json inside the static folder.

If the installs are successful it then deploys the code and runs the script inside the Procfile. This runs the app via gunicorn - Not sure if we need gunicorn for our purpose but we will leave it for now.

## Further Documentation
Further documentation can be found [here](https://drive.google.com/drive/folders/0BxaJR_flclorQ3RYaUs4UmREamM?usp=sharing)

## Creators
* [Mitchell Donaldson](https://github.com/mmdonaldson/)
* [Sam Irvine](https://github.com/Sam-Irv/)
* [Jacob Stringer](https://github.com/jacobstringer)
* [Marthijn Batlajeri](https://github.com/Marthijn-B)
* Jade Graham

## Credits
This project was bootstrapped thanks to [React Redux Flask by Daniel Ternyak](https://github.com/dternyak/React-Redux-Flask)
