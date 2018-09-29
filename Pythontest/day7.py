friends = {
    'tom':'666',
    'jerry':'777',
    'bob':'999'
}
print (friends['tom'])
print (friends['bob'])
print (friends)
for key in friends:
    print (key,":",friends[key])


a1={'a':1,'b':2}
a2={'b':2,'a':1}
print(a1==a2)
print (a1 !=a2)


friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': ' 666-33-111'}
print (friends.keys())
print (friends.popitem())
print (friends)

friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': ' 666-33-111'}
print (friends.items())
print (friends.values())
print (friends.get('tom'))
print (friends.get('a','bucunzai'))
print (friends.pop('bob'))
print (friends)



t1=( )
print (t1)
t2=(11,22,33)
t3=tuple([1,2,3,4])
t4=tuple("abc")

t1=(1,2,3,4,5,6,7,8)
t2=(9,10,11,12,13,14,15)
print (min(t1))
print (min(t1,t2))
print (min(t1))
print (max(t1,t2))
print (sum(t1))
print (len(t1))


# if条件判断
today="monday"
if today == "monday":
    print ("this is monday")
else:
    print ("this not monday")

today = "monday1"
if today == "monday":
    print("this is monday")
elif today == "tuesday":
    print("this is tuesday")
elif today == "wednesday":
    print("this is wednesday")
elif today == "thursday":
    print("this is thursday")
elif today == "friday":
    print("this is friday")
elif today == "saturday":
    print("this is saturday")
elif today == "sunday":
    print("this is sunday")
else:
    print("something else")


