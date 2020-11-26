#!/usr/bin/env python
import re
# 4.1, шаг 7

# Регулярные выражения
# regex101.com

r = re.compile('(ab(c|d)+ef)')
print(r.match('abcef'))
print(r.match('abdef'))
print(r.match('abde'))

print(r.findall('XXXX abcddcdef abdef abde abef'))
r = re.compile('(ab(c|d)*ef)')
print(r.findall('XXXX abcddcdef abdef abde abef'))
r = re.compile('(ab(c|d)?ef)')
print(r.findall('XXXX abcddcdef abdef abde abef'))

r = re.compile('([A-Za-z-]+)')
print(r.findall('hello wo000rl-d WoW'))
