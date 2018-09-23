a1 = {"meng":21, "yan":23}
b1 = {"meng":22, "yan":23}
print (a1==b1)
print (a1!=b1)

friends={'tom':'111-222-333','cat':'222-3333-4444','cindy':'222-3333-4444'}
print (friends.popitem())


print (friends.keys())
print (friends.values())
print (friends.get('tom'))
print (friends.get('meng'))
print (friends.pop('meng','null'))
print (friends)


#元组（Tuple）和列表⾮常相似，与列表不同的是，元组⼀旦创⽴，就不可改变，也就是说，元组是不可变的



t1=(1,2,3)
t2=(22,11,33)
t3=tuple([1,2,3,4])
t4=tuple("abc")
print (min(t4))
print (max(t4))
print (sum(t2))
print (len(t2))

#test
#average
def ave(num):
	nsum = 0
	for i in range(len(num)):
		nsum +=num[i]
		return nsum / len(num)

def mediannum(num):
    listnum = [num[i] for i in range(len(num))]
    listnum.sort()
    lnum = len(num)
    if lnum % 2 == 1:
        i = int((lnum + 1) / 2)-1
        return listnum[i]
    else:
        i = int(lnum / 2)-1
        return (listnum[i] + listnum[i + 1]) / 2



s='string'
print (len(s))
print (s[0])
s[0]= 'anothers'
print(s)