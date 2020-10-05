import paramiko

class ezssh:
    def __init__(self, host, port,username,password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def command(self,comands):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, port=self.port, username=self.username, password=self.password)
        stdin, stdout, stderr = ssh.exec_command(comands)

        for line in stdout.readlines():
            print(line)
        ssh.close()


    







