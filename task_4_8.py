# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = '192.168.3.1'
new_ip = ip.split('.')
new_ip_1 =[]
new_ip_1.append(int(new_ip[0]))
new_ip_1.append(int(new_ip[1]))
new_ip_1.append(int(new_ip[2]))
new_ip_1.append(int(new_ip[3]))
template_1 = '{:010b} {:010b} {:010b} {:010b}'
template_2 = '{:<10} {:<10} {:<10} {:<10}'

print(template_1.format(new_ip_1[0], new_ip_1[1], new_ip_1[2], new_ip_1[3]))
print(template_2.format(new_ip_1[0], new_ip_1[1], new_ip_1[2], new_ip_1[3]))


