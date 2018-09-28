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
