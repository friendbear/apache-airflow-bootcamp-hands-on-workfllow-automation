# Instalation

1. Launch Linux distribution from the Start menu 
2. Add custom APT repository : sudo add-apt-repository ppa:deadsnakes/ppa
3. Update package lists : sudo apt update -y
4. Install Python version 3.10 and  Pip : sudo apt install python3.10 python3-pip -y
5. Install Python Virtual Environment library : sudo apt install python3.10-venv
6. Create a virtual environment : python3.10 -m venv airflow-env
7. Activate the virtual environment: source airflow-env/bin/activate
8. Open bashrc file and set $AIRFLOW_HOME Parameter : AIRFLOW_HOME=/c/Users/sriw/airflow
9. Install Apache Airflow : pip install apache-airflow
10. Initialize database : airflow db init
11. Create a user : airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin@example.com
12. Start the web server : airflow webserver --port 8080 -D
13. Start the scheduler : airflow scheduler
14. Access the Airflow UI : http://localhost:8080
15. Login with above created user with username as admin and password as admin
