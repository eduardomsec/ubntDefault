import socket
import paramiko
import os
from netaddr import IPNetwork

range = raw_input("Digite a Network: ")
user = "ubnt"
passwd = "ubnt"
network = IPNetwork(range)
port = 22
listHots = []

def ubiquit(host, user, passwd):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=passwd)

        print 'UBNT ENCONTRADO - Digite as seguintes informacoes:\n' \
              'mca-cli\nset-inform http://unifi.campogrande.ms.gov.br:8080/inform\n'

        create(host, user, passwd)

    except Exception as err:
        return 0

def create(host, user, passwd):
    os.system('start putty.exe -ssh ' + user + '@' + host + ' -pw ' + passwd)
    listHots.append(host)
    return 0

if __name__ == '__main__':
    for ip in network:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.3)
        code = client.connect_ex((str(ip), port))

        if code == 0:
            ubiquit(str(ip), user, passwd)

    print 'Unifi encontrado:'
    for ip in listHots:
        print ip
    print 'Busca Finalizada'

    raw_input()