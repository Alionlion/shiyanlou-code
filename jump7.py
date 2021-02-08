a = 0
while a < 100:
	a+=1
	if (a+3)%10 == 0 or a%7 == 0 or a//10 == 7:
		continue
	print(a)