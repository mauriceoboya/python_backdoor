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

net_ports={
    "net1":{'port21':'ftp',
    "port22":'ssh',
    "port80":"http",
    "port153":"tomcat"},
    "net2":{
    'port21':'ftp',
    "port22":'ssh',
    "port80":"http",
    "port153":"tomcat"
    }
}
net_ports['net1'].update({'port443':'https'})
print(net_ports['net1'].pop('port22'))
print(net_ports['net1'].items())

for i in net_ports['net1'].items():
    print(i)


def networks(*networks):
    networks=['HTTP','SMTP','HTTPS','TCP','UDP','FTP']
    for i in networks:
        print(i)


networks()