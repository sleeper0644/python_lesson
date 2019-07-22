# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
new_command1 = command1.replace(command1[0:command1.index('1')],'')
new_command1.split(',')
print(new_command1)

new_command2 = command2.replace(command2[0:command2.index('1')],'')
new_command2.split(',')
print(new_command2)




