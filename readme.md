## PREREQUISITES
1. Create project directory</br>
    ```mkdir service_center```
2. Create virtual environment inside project directory</br>
    ```cd service center```
    ```python -m venv venv```
3. Activate virtual environment</br>
    ```venv\Scripts\activate```

## BASIC APPLICATION
1. Install Flask</br>
    ```pip install flask```
2. Create directory 'app' (application package</br>
    ```mkdir app```
3. Create file '__init__.py' - to treat contained files as packages</br>
    ```type nul > app/__init__.py```
4. Create module for the application handlers called 'view functions'</br>
    ```type nul > app/routes.py```
5. Create main application module</br>
    ```type nul > service_center.py```
6. Set-up environment variables</br>
    ```pip install python-dotenv```
    ```type nul > .flaskenv```

## TEMPLATES
1. Create a directory for the layout/presentation of web pages</br>
    ```mkdir app/templates```
2. Create HTML pages</br>
    ```type nul > app/templates/index.html```
    ```type nul > app/templates/base.html```
3. Write view functions in 'routes.py'</br>

## WEB FORMS
1. Install Flask-WTF extension</br>
    ```pip install flask-wtf```
2. Set-up configuration options</br>
    ```type nul > config.py```
    - Define 'Config' class - store configuration variables
    - ADD 'SECRET_KEY' config variable
    - Import class 'Config' at '__init__.py'
3. Define web form classes in 'forms.py'</br>
    ```type nul > app/forms.py```
4. Add the necessary 'form tags' in HTML Templates</br>
    ```type nul > app/templates/login.html```
5. Define 'form' view functions in 'routes.py'</br>

## DATABASES
1. Install Flask-SQLAlchemy extension</br>
    ```pip install flask-sqlalchemy```
    - Add 'SQLALCHEMY_DATABASE_URI' config variable
    - Add 'SQLALCHEMY_TRACK_MODIFICATIONS' config variable
2. Install Flask-Migrate extension</br>
    ```pip install flask-migrate```
3. Create 'database instance' & 'database migration engine instance' in application</br>
4. Define Database Models in 'models.py'</br>
5. Create Migration Repository</br>
    ```flask db init```
6. (First) Database Migration creates database / thereafter, generates migration scripts</br>
    ```flask db migrate```
7. Apply the generated migration scripts</br>
    ```flask db upgrade```

## USER LOGINS
1. Implement password hashing logic in the User Model (2 methods)</br>
2. Install Flask-Login extension</br>
    ```pip install flask-login```
3. Create 'login instance' in application</br>
4. Inherit 'UserMixin' class for 'User' model </br>
5. Configure a user loader function in 'User' class</br>
6. Define the 'Login' & 'Logout' view functions</br>
7. Install Email-Validator dependency</br>
    ```pip install email-validator```
8. Define 'RegistrationForm' and create registration template, and registration view function







