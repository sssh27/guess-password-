password = 'a123456'
sum = 0
while True:
	guess = input('請輸入密碼:\n')
	sum = sum + 1
	if guess == password:
		print('密碼正確')
		break
	if guess != password:
		print('密碼錯誤，還有', 3-sum, '次機會')
		if sum == 3:
			print('已鎖定')
			break
		