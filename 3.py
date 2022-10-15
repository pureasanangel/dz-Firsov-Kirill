# Вводятся часы, минуты и секунды. Вывести, сколько секунд прошло с полуночи.
# Вывести, какая часть суток прошла (число от 0 до 1).
h = int(input())
myn = int(input())
sec = int(input())
print(h,":",myn,':',sec)
myn = h*60 + myn
sec = myn*60 + sec
k = 1 - ((86400 - sec)/3600)/24
print('seconds since 00:00',sec, 'day part', k)