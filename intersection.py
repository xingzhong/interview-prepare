## Given two lists, print out the intersection of the lists. If an element is 
## in both lists more than once, print it more than once.

l1 = ["cat", "dog", "table", "horse", "house", "cat"]
l2 = ["cat", "cat", "horse", "dog", "dog", "chair", "cabin"]

def intersection (l1, l2):
    d1 = {}
    d2 = {}
    d3 = {}
    for ele in l1:
        if d1.has_key(ele):
            d1[ele] = d1[ele] + 1
        else:
            d1[ele] = 1
        d3[ele] = 1
    for ele in l2:
        if d2.has_key(ele):
            d2[ele] = d2[ele] + 1
        else:
            d2[ele] = 1
        if d3.has_key(ele):
            d3[ele] = d3[ele] + 1
        else:
            d3[ele] = 1
    for key, item in d3.iteritems():
        if item > 1:
            for i in range(min(d1[key], d2[key])):
                yield key
