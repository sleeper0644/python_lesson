# -*- coding: utf-8 -*-
'''
Задание 4.1

Обработать строку nat таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

ok
'''

nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
new_nat = nat.replace('FastEthernet','GigabitEthernet')
print(nat)
print(new_nat)
