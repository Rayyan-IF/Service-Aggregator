import psycopg2
from sshtunnel import SSHTunnelForwarder

try:
    with SSHTunnelForwarder(
         ('10.1.32.26', 22),
         ssh_username="devel",
         ssh_password="qaC2#2512", 
         remote_bind_address=('localhost', 5432)) as server:
         
         server.start()
         print("server connected")

         params = {
             'database': 'dms_microservices_dev',
             'user': 'sa',
             'password': 'P@ssw0rd',
             'host': 'localhost',
             'port': server.local_bind_port
             }

         conn = psycopg2.connect(**params)
         curs = conn.cursor()
         print("database connected")
except:
    print("Connection Failed")