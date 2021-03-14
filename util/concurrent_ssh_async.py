#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
import asyncssh
import asyncssh.client as client
import asyncio
import sys


def close_connections():
    sys.exit()


def define_clients():
    with open('addresses.txt', 'r') as addrs:
        machines = addrs.read().split('\n')
        return machines


async def run_client(host, command):
    async with asyncssh.connect(host, username='root', password='iutchalons') as conn:
        return await conn.run(command)


hosts = define_clients()

commands = {
    'quit_loop': close_connections,
    'connect': define_clients
}


async def execute_command(command: str):
    tasks = (run_client(host, command) for host in hosts)
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for i, result in enumerate(results, 1):
        print(f'{i}>{result.stderr}{result.stdout}')


def mainloop():
    command = ''
    while True:
        command = input('concurrent_ssh<')
        if command in commands:
            commands[command]()
        else:
            asyncio.get_event_loop().run_until_complete(execute_command(command))


def main():
    define_clients()
    mainloop()


if __name__ == '__main__':
    main()
