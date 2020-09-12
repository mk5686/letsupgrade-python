#assignment 1
print("what is your altitude")
altitude=int(input())

if altitude<=1000:
	print("Safe to land")
elif 1000<altitude<=5000:
	print("Bring down to 1000")
elif altitude>5000:
	print("Turn Around")
	
