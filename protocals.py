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