from ezssh import *

host="192.168.3.254"
port=22
username="admin"
password="password"

ssh = ezssh(host,port,username,password)
ssh.command("ls; cd folder; sudo git pull origin master")





