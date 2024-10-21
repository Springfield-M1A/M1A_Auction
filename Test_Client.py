import socket


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = input("호스트 IP 주소를 입력하세요: ")
    client_socket.connect((host_ip, 12345))  # 호스트 IP와 포트로 연결 시도

    client_socket.send("클라이언트가 접속하였습니다.".encode())  # 서버로 메시지 전송
    response = client_socket.recv(1024).decode()  # 서버로부터 응답 수신
    print(f"서버 메시지: {response}")

    client_socket.close()


if __name__ == "__main__":
    start_client()