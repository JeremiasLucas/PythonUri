td = int(input())

a = td // 365
td = td - a * 365

m = td // 30
td = td - m * 30

d = td

print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))
