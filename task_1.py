from subprocess import Popen, PIPE
from ipaddress import ip_address
import socket


'''1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
'''


check_ip = ['vk.com', '2.2.2.2', '192.168.0.1', '192.168.0.101']


def host_ping(check_ip_list, timeout=100, requests=1, print_data=True):
    reachable_data = {'Reachable': [], 'Unreachable': []}
    for ip in check_ip_list:
        reply = Popen(
            f"ping {ip_address(socket.gethostbyname(ip))} -w {timeout} -n {requests}", stdout=PIPE, stderr=PIPE)
        code = reply.wait()
        if code == 0:
            reachable_data['Reachable'].append(ip)
            if print_data: print(ip, 'Узел доступен', )
        else:
            reachable_data['Unreachable'].append(ip)
            if print_data: print(ip, 'Узел недоступен')
    return reachable_data


host_ping(check_ip)
print()

''' 2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только 
последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.'''


def host_range_ping(start_ip, additional_ip=0):
    """ additional_ip - сколько ещё нужно проверить дополнительных адресов начиная с start_ip"""
    for i in range(additional_ip + 1):
        host_ping([str(ip_address(socket.gethostbyname(start_ip)) + i)])


host_range_ping('192.168.0.253', 4)
print()

'''3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае 
результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate). 
Таблица должна состоять из двух колонок и выглядеть примерно так:
Reachable   Unreachable
10.0.0.1    10.0.0.3
10.0.0.2    10.0.0.4
'''

from tabulate import tabulate


def host_range_ping_tab(start_ip, count_ip=1):
    all_ip = [str(ip_address(socket.gethostbyname(start_ip)) + i) for i in range(count_ip)]
    print(tabulate(host_ping(all_ip, print_data=False), headers='keys', tablefmt="pipe", stralign="center"))


host_range_ping_tab('10.0.0.1', 4)
