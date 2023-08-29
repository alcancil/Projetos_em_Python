#Projetos em Python

![image](https://github.com/alcancil/Projetos_em_Python/blob/main/automacao/netmiko/01/imagens/imagem01.png)

Repositório Criado em 29/08/2023 por Alexandre Lavorenti Cancilieri
Código originalmente criado por [Jardel D'Oliveira](https://www.linkedin.com/in/jardeldoliveira/) e alterado por [Alexandre Lavorenti Cancilieri](https://www.linkedin.com/in/alexandre-lavorenti-cancilieri/)

Esse é um exemplo de uso da bilbioteca netmiko desenvolvida em python para automação. Aqui temos o seguinte cenário: Temos 3 switches interligados a uma núvem. Essa núvem representa a máquina real. Então queremos que o script leia os endereços constados nos arquivo device_list.txt e logo em seguida receba os comandos que vão estar no outro arquivo chamado cli.txt. Basicamente temos aqui 3 roteadores com o usuário: admin password: password configurados com acesso ssh. Então aqui vamos alterar o nome dos switches para SWXXX e criarar as vlans 100 e 200 e depois nomea-las como vlan_100 e vlan_200.

Depois de executado o scripte, é para ter uma saida semelhante a da imagem02

![image](https://github.com/alcancil/Projetos_em_Python/blob/main/automacao/netmiko/01/imagens/imagem02.png)
