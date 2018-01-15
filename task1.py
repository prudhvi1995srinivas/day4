def nested_sum(L):
	sum=0
for i in L1:
	if isinstance(i,int):
	sum+=i
	else:
	sum+=nested_sum(i)
	return sum
