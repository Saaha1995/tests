#find max count of wordr in line
from time import time
start = time

with open ('/home/alexandr/Downloads/dataset_3363_3.txt') as inf:
    line = ''
    rows = []
    for line in inf:
        rows.append(line.strip())

new_line = ''
for i in rows:
    new_line = new_line + ' ' + i

a = sorted(new_line.upper().split())

list_a_unrep = set()
for i in a:
    list_a_unrep.add(i)

qaz = sorted(list(list_a_unrep))

q=0
d = []
for j in qaz:
    q = a.count(j)
    d.append([q, j])

m = [0, 0]
for i in d:
    if i[0] > m[0]:
        m = i
    elif i[0] == m[0]:
        if i[1] > m[1]:
            m = i

qwer = str(m[1]) + ' ' + str(m[0])
print (qwer)

with open ('/home/alexandr/Downloads/answer1.txt', 'w') as ouf:
    ouf.write (qwer)
print (start-time)




