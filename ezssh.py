import paramiko

class ezssh:
    def __init__(self, host, port,username,password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, port=self.port, username=self.username, password=self.password)

    def command(self,comands):
        stdin, stdout, stderr = self.ssh.exec_command(comands)

        for line in stdout.readlines():
            print(line)

    def shutdown(self):
        self.command("shutdown now")

    def reboot(self):
        self.command("reboot")


    def __exit__(self, exc_type, exc_value, traceback):
        self.ssh.close()
        pass