
# Website SMPN Satu Atap 1 Pengabuan

The website SMPN Satu Atap 1 Pengabuan is a school website that is used to display various information about SMPN Satu Atap 1 Pengabuan and in it there are also two additional menus, namely quizzes and reading logs. On the quiz menu, students can work on questions and on the reading log menu, students can input the title of the book and the date they finished reading the book.


## Documentation

If you want to see how this website looks, you can see the documentation video on this YouTube link [click here](https://youtu.be/Lo3Di2q5g8A?si=x7JbeSMpHBl_ayZU).


## Installation

Application/Software/Module Requirement

1. Visual Studio Code
    You can download vscode at this link: https://code.visualstudio.com/

2. XAMPP
You can download xampp at this link: https://www.apachefriends.org/download.html

After installing vscode, you need to install some of these modules:

1.1.**Flask**: Flask is a micro web framework for Python.
   - Installation: `pip install Flask`

1.2. **Flask-MySQLdb**: Flask-MySQLdb is an extension for Flask that allows connections to a MySQL database.

   - Installation: `pip install Flask-MySQLdb`

1.3. **bcrypt**: bcrypt is a password hashing library for Python. It's used for securely hashing passwords.
   - Installation: `pip install bcrypt`

1.4. **datetime**: datetime is a module in Python's standard library used for manipulating dates and times.
   - Included in Python's standard library, so no separate installation is required.

## Database Preparation
1. Extract the zip file of this website and save the folder in `c/xampp/htdocs`.
2. Open xampp, then click start on Apache and MySQL.
3. Open Google Chrome and type localhost/phpmyadmin.
4. After logging in, create a new database with the name: reading.
5. In the database (reading), click import menu, then upload reading.sql.
6. If two tables appear in the database (reading), namely books and users, then database preparation is complete.


## Running Tests

1. Open Folder FinalProject with vscode.
2. Open app.py
3. In terminal,

```bash
  python .\app.py
```

## Using the website
1. **Initial View**
If you successfully run this website, the first display you will see is as follows:
![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

4. **Without Login**
Almost all menus on this website can be accessed without needing to log in.
![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

5. **With Login**
The only menu that can only be accessed by registering and logging in first is the Reading Log.
- Registration
![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

- Login
![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)






  
    
