_NEG_INFINITY = -99999

def memoized_cut_rod(p,n):
	r=[None]*(n+1)

	for x in range(0,n+1):
		r[x]=_NEG_INFINITY
	return memoized_cut_rod_aux(p,n,r)


def memoized_cut_rod_aux(p,n,r):
	if r[n]>=0:
		return r[n]

	if n==0:
		q=0
	else:
		q=_NEG_INFINITY

	for x in range(1,n+1):
		q=find_max(q,p[x]+memoized_cut_rod_aux(p,n-x,r))

	r[n]=q
	return q

def find_max(a,b):
	if a>b:
		return a
	else:
		return b


# prices={1:1,2:5,3:8,4:9,5:10,6:17,7:17,8:20,9:24,10:30}

# print(memoized_cut_rod(prices,5))


