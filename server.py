import socket
import random
import threading
import time

# Configurações do servidor
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5000
BUFFER_SIZE = 1024
TIMEOUT = 5  # Tempo em segundos para timeout

def handle_client(connection, address):
    print(f"[CONEXÃO ESTABELECIDA] Cliente conectado: {address}")
    
    try:
        # Etapa 1: Receber SYN
        syn_packet = connection.recv(BUFFER_SIZE).decode()
        if syn_packet.startswith("SYN"):
            client_seq = int(syn_packet.split(":")[1])
            server_seq = random.randint(1000, 5000)
            print(f"[RECEBIDO] SYN do cliente com seq = {client_seq}")
            
            # Etapa 2: Enviar SYN-ACK
            syn_ack_packet = f"SYN-ACK:{server_seq}:ACK:{client_seq + 1}"
            connection.send(syn_ack_packet.encode())
            print(f"[ENVIADO] SYN-ACK com seq = {server_seq} e ack = {client_seq + 1}")
            
            # Etapa 3: Receber ACK
            ack_packet = connection.recv(BUFFER_SIZE).decode()
            if ack_packet.startswith("ACK"):
                ack_number = int(ack_packet.split(":")[1])
                if ack_number == server_seq + 1:
                    print(f"[RECEBIDO] ACK do cliente com ack = {ack_number}")
                    print("[HANDSHAKE COMPLETO] Conexão TCP estabelecida com sucesso!\n")
                    
                    # Aqui poderia ocorrer a transferência de dados
                    
                    # Encerramento da conexão
                    # Etapa 1: Enviar FIN
                    fin_packet = f"FIN:{server_seq + 1}"
                    connection.send(fin_packet.encode())
                    print(f"[ENVIADO] FIN com seq = {server_seq + 1}")
                    
                    # Etapa 2: Receber ACK do FIN
                    fin_ack_packet = connection.recv(BUFFER_SIZE).decode()
                    if fin_ack_packet.startswith("ACK"):
                        ack_number = int(fin_ack_packet.split(":")[1])
                        if ack_number == server_seq + 2:
                            print(f"[RECEBIDO] ACK do cliente confirmando FIN com ack = {ack_number}")
                            
                            # Etapa 3: Receber FIN do cliente
                            client_fin_packet = connection.recv(BUFFER_SIZE).decode()
                            if client_fin_packet.startswith("FIN"):
                                client_fin_seq = int(client_fin_packet.split(":")[1])
                                print(f"[RECEBIDO] FIN do cliente com seq = {client_fin_seq}")
                                
                                # Etapa 4: Enviar ACK final
                                final_ack_packet = f"ACK:{client_fin_seq + 1}"
                                connection.send(final_ack_packet.encode())
                                print(f"[ENVIADO] ACK final confirmando FIN do cliente com ack = {client_fin_seq + 1}")
                                print("[CONEXÃO ENCERRADA] Conexão TCP finalizada com sucesso!\n")
                else:
                    print("[ERRO] Número de ACK inesperado do cliente.")
            else:
                print("[ERRO] Pacote inesperado recebido do cliente.")
        else:
            print("[ERRO] Pacote SYN não recebido corretamente.")
    except socket.timeout:
        print("[TIMEOUT] Ocorreu um timeout durante a comunicação.")
    finally:
        connection.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(5)
    print(f"[INICIANDO] Servidor ouvindo em {SERVER_IP}:{SERVER_PORT}")

    while True:
        conn, addr = server_socket.accept()
        conn.settimeout(TIMEOUT)
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
        print(f"[ATIVO] Conexões ativas: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
