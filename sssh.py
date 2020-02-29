import paramiko


try:
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.200.111',
                   username='developer',
                   password='4linux',
                   port='22')
except Exception as e:
    print('Erro conexão: {}'.format(e))
    exit()

stdin, stdout, stderr = client.exec_command('sudo init 0')
if stdout.channel.recv_exit_status() == 0:
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))