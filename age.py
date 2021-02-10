driver = input('請問你有開過車嗎?')
age = input('請問你的年齡?')
age=int(age)

if driver == '有':
	if age >= 18:
		print('擬通過測驗了')
	else:
		print('奇怪')
		