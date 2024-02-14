import socket
target = input ("Inserisci l'indirizzo IP da scansionare:")
portrange = input ("Inserisci le porte da scansionare:")

lowport= int( portrange.split ('-')[0])
highport= int( portrange.split ('-')[1])

print ('Scanning Hosts', target, 'from port', lowport, 'to port', highport)

for port in range (lowport, highport):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status= s.connect_ex((target, port))
    if (status==0):
        print('*"* PORT TCP', port, '- OPEN  *"*')
    else:
        print( 'PORT TCP', port, '- CLOSED')

for port in range (lowport, highport):
    s2=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    status=s2.connect_ex((target, port))
    if (status==0):
        print ('*"* PORT UDP', port, '- CLOSED')
    else:
        print ('PORT UDP', port, '- OPEN')