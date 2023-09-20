def protocal():
    lists=['HTTP','SMTP','HTTPS','TCP','UDP','FTP']

    search_protocal='HTTPS'
    found=False
    for i in range(len(lists)):
        found=lists[i]==search_protocal
        if found:
            print('found at index',i)
            break
        else:
            print('')


protocal()

network_protocals=('HTTP','SMTP','HTTPS','TCP','UDP','FTP')

print(network_protocals[1])

users={
    "user1":{'username':'james',
    "password":'james123',
    "email":"james@gmail.com",
    "department":"Applied Statistics"},
    "user2":{
    'username':'james',
    "password":'james123',
    "email":"jamedf@gmail.com",
    "department":"Applied Statistics"
    }
}
users['user1'].update({'title':'DRs'})
print(users['user1'].pop('title'))
print(users['user1'].items())

for i in users['user1'].items():
    print(i)