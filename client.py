import socket
import random
import time

# Configurações do cliente
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5000
BUFFER_SIZE = 1024
TIMEOUT = 5  # Tempo em segundos para timeout

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(TIMEOUT)
    
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print(f"[CONECTADO] Cliente conectado ao servidor em {SERVER_IP}:{SERVER_PORT}")
        
        # Etapa 1: Enviar SYN
        client_seq = random.randint(1000, 5000)
        syn_packet = f"SYN:{client_seq}"
        client_socket.send(syn_packet.encode())
        print(f"[ENVIADO] SYN com seq = {client_seq}")
        
        # Etapa 2: Receber SYN-ACK
        syn_ack_packet = client_socket.recv(BUFFER_SIZE).decode()
        if syn_ack_packet.startswith("SYN-ACK"):
            parts = syn_ack_packet.split(":")
            server_seq = int(parts[1])
            server_ack = int(parts[3])
            if server_ack == client_seq + 1:
                print(f"[RECEBIDO] SYN-ACK com seq = {server_seq} e ack = {server_ack}")
                
                # Etapa 3: Enviar ACK
                ack_packet = f"ACK:{server_seq + 1}"
                client_socket.send(ack_packet.encode())
                print(f"[ENVIADO] ACK com ack = {server_seq + 1}")
                print("[HANDSHAKE COMPLETO] Conexão TCP estabelecida com sucesso!\n")
                
                # Aqui poderia ocorrer a transferência de dados
                
                # Encerramento da conexão
                # Etapa 1: Receber FIN do servidor
                fin_packet = client_socket.recv(BUFFER_SIZE).decode()
                if fin_packet.startswith("FIN"):
                    server_fin_seq = int(fin_packet.split(":")[1])
                    print(f"[RECEBIDO] FIN do servidor com seq = {server_fin_seq}")
                    
                    # Etapa 2: Enviar ACK para o FIN
                    fin_ack_packet = f"ACK:{server_fin_seq + 1}"
                    client_socket.send(fin_ack_packet.encode())
                    print(f"[ENVIADO] ACK confirmando FIN com ack = {server_fin_seq + 1}")
                    
                    # Etapa 3: Enviar FIN para o servidor
                    client_fin_seq = server_ack  # Poderia ser outro número
                    client_fin_packet = f"FIN:{client_fin_seq}"
                    client_socket.send(client_fin_packet.encode())
                    print(f"[ENVIADO] FIN com seq = {client_fin_seq}")
                    
                    # Etapa 4: Receber ACK final do servidor
                    final_ack_packet = client_socket.recv(BUFFER_SIZE).decode()
                    if final_ack_packet.startswith("ACK"):
                        ack_number = int(final_ack_packet.split(":")[1])
                        if ack_number == client_fin_seq + 1:
                            print(f"[RECEBIDO] ACK final confirmando FIN com ack = {ack_number}")
                            print("[CONEXÃO ENCERRADA] Conexão TCP finalizada com sucesso!\n")
            else:
                print("[ERRO] Número de ACK inesperado do servidor.")
        else:
            print("[ERRO] Pacote inesperado recebido do servidor.")
    except socket.timeout:
        print("[TIMEOUT] Ocorreu um timeout durante a comunicação.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
