from subprocess import CalledProcessError, check_output


for ip in range (1, 55, 1):
    ipAddress = '192.168.20. ' + str(ip);
    
    print(ipAddress);
    
    ipConectadas = [];
    
    try:
        check_output(['ping', '-c', '1', ipAddress]);
        print('Ip conectada');
        ipConectadas.append(ipAddress);
            
    except CalledProcessError:
        print('Ip no conectada');
        
print('IPS CONECTADAS: ', ipConectadas);