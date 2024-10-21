import socket
import time


def connect_to_host():
    while True:
        try:
            host_ip = input("호스트 IP 주소를 입력하세요: ")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host_ip, 12345))
            return client_socket
        except socket.error:
            print("잘못된 IP 주소이거나 서버에 연결할 수 없습니다. 다시 시도하세요.")
            time.sleep(1)


def start_client():
    client_socket = connect_to_host()

    # 닉네임 설정
    nickname = input("사용할 닉네임을 입력하세요: ")
    client_socket.send(nickname.encode())  # 닉네임 서버로 전송

    while True:
        message = input("메시지 입력: ")
        client_socket.send(message.encode())


if __name__ == "__main__":
    start_client()