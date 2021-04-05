import subprocess

process = []

while True:
    action = input(
        'Выберите действие: (q, й) - выход , (s, ы, д, l) - запустить сервер и клиенты, (x, ч) - закрыть все окна:')

    if action in ['q', 'й']:
        break
    elif action in ['s', 'ы', 'l', 'д']:
        process.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))
        process.append(subprocess.Popen('python client.py -n test1', creationflags=subprocess.CREATE_NEW_CONSOLE))
        process.append(subprocess.Popen('python client.py -n test2', creationflags=subprocess.CREATE_NEW_CONSOLE))
        process.append(subprocess.Popen('python client.py -n test3', creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif action in ['x', 'ч']:
        while process:
            victim = process.pop()
            victim.kill()