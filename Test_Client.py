import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            # 서버로부터 메시지 수신
            message = client_socket.recv(1024).decode()
            if message == 'NICK':
                client_socket.send(nickname.encode())  # 닉네임 전송
            else:
                print(message)
        except:
            # 오류 발생 시 연결 종료
            print("연결이 종료되었습니다.")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        message = input('')
        client_socket.send(message.encode())  # 서버로 메시지 전송

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = input("호스트 IP 주소를 입력하세요: ")
    client_socket.connect((host_ip, 12345))

    global nickname
    nickname = input("사용할 닉네임을 입력하세요: ")

    # 메시지 수신 스레드 생성
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # 메시지 전송 스레드 생성
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

if __name__ == "__main__":
    start_client()