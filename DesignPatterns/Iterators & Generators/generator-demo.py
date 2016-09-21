def generate_sequence(n):
	i=n
	while i>-1:
		yield i
		i-=1

for x in generate_sequence(10):
	print(x)

c=(i for i in range(10,-1,-1) if i%2==0)
print(next(c))
print(next(c))
