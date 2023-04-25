#Cria o banco de dados e as tabelas.
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

host=os.getenv("DB_HOST")
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")

script = 'create_db.sql'

cmd = f"mysql -h {host} -u {user} -p{password} < {script}"

subprocess.run(cmd, shell=True)