### Note: I have removed my SQL credentials

## Project Setup
1. Clone repository:
    ```bash
    git clone https://github.com/Babban33/eactive-test.git
    ```
2. ```bash
    cd eactive-test
    ```

3. Setup Virtual Environment:
    ```bash
    pip install virtualenv
    virtualenv <env_name>
    <env_name>/Scripts/activate
    ```

4. Install libraries:
    ```bash
    pip install flask flask-sqlalchemy pymysql
    ```

## Run Application
1. ```bash
    python run.py
    ```

2. Access **http://127.0.0.1:5000** and the **/hello**, **/users** endpoints.