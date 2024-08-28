# Handshake TCP

Este projeto contém uma implementação básica de um handshake TCP em Python, simulando o processo de estabelecimento e encerramento de uma conexão TCP entre um cliente e um servidor. O handshake TCP é uma parte fundamental do protocolo TCP (Transmission Control Protocol), que garante uma comunicação confiável entre dois dispositivos em uma rede.

### Clone o repositório
```bash
git clone https://github.com/JoaoVictorFBarros/HandShake.git
```


### Instalação das Dependências

Todas as bibliotecas usadas são padrão do python

### Executando o Projeto

Para iniciar o programa, execute:

1. **Servidor**:
   - Execute o script `server.py`.
   - O servidor iniciará e ficará aguardando conexões de clientes.

   ```bash
   python3 server.py
   ```

2. **Cliente**:
   - Execute o script `client.py`.
   - O cliente tentará se conectar ao servidor e iniciar o handshake TCP.

   ```bash
   python3 client.py
   ```
 
<div align="center">
<img src=print.png >
</div>


## Estrutura do Projeto

O projeto está dividido em dois scripts principais:

1. **Servidor (`server.py`)**: O script que simula o comportamento do lado do servidor durante o processo de handshake TCP e encerramento da conexão.
2. **Cliente (`client.py`)**: O script que simula o comportamento do lado do cliente durante o processo de handshake TCP e encerramento da conexão.

## O que é um Handshake TCP?

O handshake TCP é um processo de três etapas usado para estabelecer uma conexão confiável entre um cliente e um servidor. Ele garante que ambas as partes estejam prontas para a transmissão de dados e concordem com parâmetros como números de sequência e de reconhecimento.

### Etapas do Handshake TCP

1. **SYN (Synchronize)**: O cliente envia um pacote SYN ao servidor para iniciar a conexão, contendo um número de sequência inicial.
2. **SYN-ACK (Synchronize-Acknowledge)**: O servidor responde com um pacote SYN-ACK, que contém seu próprio número de sequência e um reconhecimento do número de sequência do cliente.
3. **ACK (Acknowledge)**: O cliente envia de volta um pacote ACK ao servidor, reconhecendo o número de sequência do servidor, completando assim o handshake.

### Encerramento da Conexão

O encerramento de uma conexão TCP também envolve um processo de handshake, garantindo que ambas as partes reconheçam o término da comunicação.

1. **FIN (Finish)**: A parte que deseja encerrar a conexão envia um pacote FIN.
2. **ACK do FIN**: A outra parte reconhece o pacote FIN enviando um ACK.
3. **FIN da outra parte**: A outra parte também envia um pacote FIN.
4. **ACK final**: A parte inicial reconhece o FIN da outra parte enviando um ACK final, completando o encerramento da conexão.

## Importância do Handshake TCP

O handshake TCP é crucial porque:

- **Confiabilidade**: Garante que os dados sejam entregues de forma confiável e na ordem correta.
- **Sincronização**: Permite que cliente e servidor sincronizem seus números de sequência e reconhecimento, assegurando que ambos estejam prontos para a troca de dados.
- **Estabelecimento de Parâmetros**: Define parâmetros de conexão essenciais antes que a transmissão de dados comece.
- **Prevenção de Conexões Perdidas**: O processo de três etapas ajuda a prevenir conexões que possam ser iniciadas erroneamente devido a pacotes duplicados ou atrasados na rede.
   ```
