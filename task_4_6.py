# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
template = '''
Protocol:              OSPF
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
'''
nwe_ospf_route = ospf_route.split()
nwe_ospf_route[4] =  nwe_ospf_route[4].replace(',','')
nwe_ospf_route[5] =  nwe_ospf_route[5].replace(',','')
print(template.format(nwe_ospf_route[1], 
                      nwe_ospf_route[2],
                      nwe_ospf_route[4],
                      nwe_ospf_route[5],
                      nwe_ospf_route[6]))
