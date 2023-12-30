from sshtunnel import SSHTunnelForwarder

def ConnectDBTunnels(param:object):
    print('Connecting to the PostgreSQL Database...')
    try:
        server = SSHTunnelForwarder(
            param.db_ssh_server,
            ssh_username=param.db_ssh_user,
            ssh_password=param.db_ssh_pass,
            remote_bind_address=('localhost', int(param.db_port))
        )
        server.start()
        print("server succesfully connected")
        database_url = f"postgresql://{param.db_user}:{param.db_password}@{param.db_server}:{server.local_bind_port}/{param.db_name}" #PostgreSQL TUNNEL
        return database_url
    except:
        print("failed to connect ...")