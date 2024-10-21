import socket


def start_host():
    # 소켓 생성 및 바인딩
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # 모든 IP로부터의 연결 허용, 포트 12345 사용
    server_socket.listen(5)  # 최대 5명까지 대기 가능

    print("호스트 서버가 시작되었습니다. 연결을 기다립니다...")

    print(socket.gethostbyname(socket.gethostname()))
    client_socket, address = server_socket.accept()  # 클라이언트 연결 수락
    print(f"클라이언트가 연결되었습니다: {address}")

    # 클라이언트로부터 메시지 수신
    message = client_socket.recv(1024).decode()
    print(f"클라이언트 메시지: {message}")

    # 클라이언트에게 응답 전송
    client_socket.send("경매 서버에 오신 것을 환영합니다!".encode())

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_host()
