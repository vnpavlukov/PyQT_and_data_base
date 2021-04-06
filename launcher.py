import subprocess

process = []

while True:
    action = input(
        'Выберите действие: (q) - выход , (s) - запустить сервер и клиенты, (x) - закрыть все окна:')

    if action in ['q', 'й']:
        break
    elif action in ['s', 'ы', 'l', 'д']:
        num_clients = int(input('Введите количество клиентов: '))
        process.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))
        for client in range(num_clients):
            process.append(subprocess.Popen(
                f'python client.py -n test{client}', creationflags=subprocess.CREATE_NEW_CONSOLE))

    elif action in ['x', 'ч']:
        while process:
            victim = process.pop()
            victim.kill()