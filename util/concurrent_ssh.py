#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
import logging

import paramiko
import paramiko.client as client
import sys

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
            #cli.load_system_host_keys()
            #print(addr)
            cli.connect(hostname=addr, username='root', password='iutchalons')
            connections.append(cli)


commands = {
    'quit_loop': close_connections,
    'connect': define_clients
}


def execute_command(command: str):
    final_result = ''
    i = 1
    for conn in connections:
        result = conn.exec_command(command)
        final_result += f'{i}>{result[1].read()}\n'
    return final_result


def mainloop():
    command = ''
    while True:
        command = input('concurrent_ssh<')
        if command in commands:
            commands[command]()
        else:
            results = execute_command(command)
            print(results)


def main():
    paramiko.util.log_to_file('logs')
    define_clients()
    mainloop()


if __name__ == '__main__':
    main()
