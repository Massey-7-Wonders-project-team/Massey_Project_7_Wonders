# Massey_Project_7_Wonders
7 Wonders implementation for Massey capstone project

## Getting Started

#### Installs
* Ensure you have python 2.7 running `python --version` to check
* Ensure you have pip installed `pip --version` to check
* Install the following python modules
```
pip install flask flask_script flask_migrate flask_bcrypt pytest flask_testing
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
`python manage.py create_db`

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
Note there are currently no tests
```sh
cd static
npm run test
```

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
