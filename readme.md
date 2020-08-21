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

    