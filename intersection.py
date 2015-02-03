## Given two lists, print out the intersection of the lists. If an element is 
## in both lists more than once, print it more than once.

l1 = ["cat", "dog", "table", "horse", "house", "cat"]
l2 = ["cat", "cat", "horse", "dog", "dog", "chair", "cabin"]

def intersect(l1, l2):
	d1, d2 = {}, {}
	for l in l1:
		try: d1[l]+=1
		except KeyError: d1[l] = 1

	for l in l2:
		if l in d1:
			try: d2[l]+=1
			except KeyError: d2[l] = 1
			
	return [[k]*min(d1[k], d2[k]) for k in d2.keys()]
