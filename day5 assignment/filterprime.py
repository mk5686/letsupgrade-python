
def checkprime(num):
		#continue
	if num==2:
			return True
	for i in range(2,num):

		if num==i or num%i==0:
			return False
		else:
			return True

prime_num_lst=filter(checkprime,range(1,2500))
print(list(prime_num_lst))