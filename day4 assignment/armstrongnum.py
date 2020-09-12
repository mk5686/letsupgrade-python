
i=0
for i in range(1042000,702648265):
	ip=str(i)
	l=int(len(ip))
	num=int(ip)
	m=0
	while num!=0:
		r=num%10
		m=m+r**l
		num=int(num/10)


	if m==i:
		print("first armstrong num in given range is \n",m)
		break

	else:
		continue
