
def checklist(new_sub,lst):
	sub_lst=new_sub.copy()
	for i in range(len(lst)):
		if sub_lst[0]==lst[i]:
			sub_lst.pop(0)
	if len(sub_lst)==0:
		return "it's a Match"
	else:
		#sub_lst=sub_lst+new_sub
		return "it's Gone"


a=[1,1,5]
b=[1,5,6,4,1,2,3,5]
c=[1,5,6,5,1,2,3,6]
print(b)
print(checklist(a,b))
print("\n")
print(c)
print(checklist(a,c))
