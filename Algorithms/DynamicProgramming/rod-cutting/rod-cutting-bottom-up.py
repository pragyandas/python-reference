_NEG_INFINITY=-99999

def bottom_up_cut_rod(p,n):
	r=[None]*(n+1)

	r[0]=0

	for x in range(1,n+1):
		q=_NEG_INFINITY
		for y in range(1,x+1):
			q=find_max(q,p[y]+r[x-y])

		r[x]=q

	return q	

def find_max(a,b):
	if a>b:
		return a
	else:
		return b


# prices={1:1,2:5,3:8,4:9,5:10,6:17,7:17,8:20,9:24,10:30}

# print(bottom_up_cut_rod(prices,5));
