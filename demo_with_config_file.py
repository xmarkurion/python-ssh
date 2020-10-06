from ezssh import *
import configparser
import os

#Read config file
config = configparser.ConfigParser()
config.read('config.ini')

host = config['SSH']['host']
port = config['SSH']['port']
username = config['SSH']['username']
password = config['SSH']['password']
#--------------------------------------

ssh = ezssh(host,port,username,password)
ssh.command("ls;")

os.system('pause')



