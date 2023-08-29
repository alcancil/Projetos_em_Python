#O script está lendo 2 listas, uma com os endereços de IP, e outra com os comandos. E por algum motivo, ele só está lendo o primento switch do arquivo (tenho 3 switches no meu lab). 
 
my_devices = open("device_list.txt")
comandos = open("cli.txt")
devyces = list()
'''data = time.strftime("%Y%m%d")'''
 
for device_ip in my_devices:
    device = {
        "device_type": 'cisco_ios',
        "ip": device_ip,
        "username": 'admin',
        "password": 'password',
}    
    devyces.append(device)      
 
for cada_ip in devyces:
     for comand in comandos:
         net_connect = ConnectHandler(**cada_ip, session_timeout=30)
         #net_connect.enable()
         '''time.sleep(3)'''
         print(f'\n Conectando no Switch:{cada_ip["ip"]}')
         output = net_connect.send_command(comand)
         print (f'\n Enviando o comando: *{comand}*\n')
         #print(output)
         print(f'\n Fechando a conexão de {cada_ip["ip"]}')
         continue    
net_connect.disconnect()