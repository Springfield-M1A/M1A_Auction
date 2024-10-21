import socket
import threading

# 클라이언트 목록을 저장할 리스트
clients = []
nicknames = []


# 브로드캐스트 함수 (모든 클라이언트에게 메시지 전송)
def broadcast(message):
    for client in clients:
        client.send(message)


def handle_client(client_socket):
    while True:
        try:
            # 클라이언트로부터 메시지 수신
            message = client_socket.recv(1024)
            broadcast(message)  # 받은 메시지를 다른 클라이언트에게 브로드캐스트
        except:
            # 연결이 끊긴 클라이언트 처리
            index = clients.index(client_socket)
            clients.remove(client_socket)
            client_socket.close()
            nickname = nicknames[index]
            broadcast(f'{nickname}님이 퇴장하셨습니다.'.encode())
            nicknames.remove(nickname)
            break


# 서버 시작 함수
def start_host():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # 모든 IP에서 연결 허용
    server_socket.listen()

    print("서버가 시작되었습니다. 클라이언트 연결을 기다립니다...")

    while True:
        # 클라이언트 연결 수락
        client_socket, address = server_socket.accept()
        print(f"클라이언트가 연결되었습니다: {address}")

        # 닉네임 요청 및 수신
        client_socket.send('NICK'.encode())
        nickname = client_socket.recv(1024).decode()

        # 닉네임과 클라이언트 소켓을 리스트에 저장
        nicknames.append(nickname)
        clients.append(client_socket)

        print(f"닉네임: {nickname}")
        broadcast(f"{nickname}님이 경매에 참여하셨습니다!".encode())
        client_socket.send("경매 서버에 접속되었습니다!".encode())

        # 클라이언트의 메시지를 처리하는 스레드 생성
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


def show_menu():
    while True:
        print("\n===== 경매 메뉴 =====")
        print("1. 아이템 추가")
        print("2. 아이템 추가 (txt 파일로)")
        print("3. 아이템 삭제")
        print("4. 추가 설정")
        print("5. 내 IP 주소 확인")
        print("6. 경매 시작")
        print("0. 종료")

        choice = input("선택: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            add_items_from_file()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            additional_settings()
        elif choice == '5':
            show_ip_address()
        elif choice == '6':
            start_auction()
        elif choice == '0':
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

def add_item():
    item = input("추가할 아이템을 입력하세요: ")
    # 아이템 추가 로직 (예: 리스트에 추가)
    print(f"아이템 '{item}'이(가) 추가되었습니다.")

def add_items_from_file():
    file_path = input("txt 파일 경로를 입력하세요: ")
    try:
        with open(file_path, 'r') as file:
            items = file.readlines()
            # 각 줄을 아이템으로 추가
            for item in items:
                item = item.strip()
                if item:
                    print(f"아이템 '{item}'이(가) 추가되었습니다.")
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

def remove_item():
    item = input("삭제할 아이템을 입력하세요: ")
    # 아이템 삭제 로직 (예: 리스트에서 삭제)
    print(f"아이템 '{item}'이(가) 삭제되었습니다.")

def additional_settings():
    # 나중에 추가할 설정
    print("추가 설정 메뉴입니다.")

def show_ip_address():
    # 호스트의 IP 주소 확인
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"내 IP 주소: {ip_address}")

def start_auction():
    # 경매 시작 로직
    print("경매가 시작되었습니다.")

if __name__ == "__main__":
    # 메뉴 스레드
    menu_thread = threading.Thread(target=show_menu)
    menu_thread.start()

    # 호스트 서버 스레드
    start_host()