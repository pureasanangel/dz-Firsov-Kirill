th = {'огниво': 2, 'аптечка': 20, 'компас': 10, 'бутеллизированная вода': 50, 'рубашка': 30,
      	'термос': 100,  'дождевик': 35, 'бинокль': 40, 'удочка': 120,
          'салфетки': 4, 'сух.пай': 82, 'палатка': 600, 'спальный мешок': 225, 'жвачка': 1}
ves = int(input())
sorted_th = dict(sorted(th.items(), key=lambda x: -x[1]))
for k, v in sorted_th.items():
	if v <=  ves:
		print(k, v)
	ves = ves - v

