#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
import sys

#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
import paramiko
import paramiko.client as client

connections = []


def close_connections():
    for conn in connections:
        conn.close()
        sys.exit()


def define_clients():
    with open('addresses.txt', 'r') as addrs:
        addresses = addrs.read().split('\n')
        for addr in addresses:
            cli = client.SSHClient()
            cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # cli.load_system_host_keys()
            # print(addr)
            cli.connect(hostname=addr, username='root', password='iutchalons')
            connections.append(cli)


commands = {
    'quit_loop': close_connections,
    'connect': define_clients
}


def execute_command(command: str):
    i = 1
    for conn in connections:
        result = conn.exec_command(command)
        stdin, stdout, stderr = result
        print(f'{i}>{stderr.readlines()}{stdout.readlines()}')
        i += 1


def mainloop():
    command = ''
    while True:
        command = input('concurrent_ssh<')
        if command in commands:
            commands[command]()
        else:
            execute_command(command)


def main():
    paramiko.util.log_to_file('logs')
    define_clients()
    mainloop()


if __name__ == '__main__':
    main()
