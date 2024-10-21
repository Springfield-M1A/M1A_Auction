import socket


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = input("호스트 IP 주소를 입력하세요: ")
    client_socket.connect((host_ip, 12345))

    # 서버로부터 경매 정보 수신
    auction_info = client_socket.recv(1024).decode()
    print(f"서버로부터 수신된 경매 정보: {auction_info}")

    client_socket.close()


if __name__ == "__main__":
    start_client()