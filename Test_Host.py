import socket
import threading

# 클라이언트 목록을 저장할 리스트
clients = []

def handle_client(client_socket, address):
    # 클라이언트 접속 처리
    nickname = client_socket.recv(1024).decode()  # 닉네임 수신
    print(f"클라이언트 {nickname} ({address})가 접속했습니다.")
    clients.append(nickname)

    # 계속해서 클라이언트와 통신
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"{nickname}: {message}")
        except:
            print(f"{nickname}가 연결을 끊었습니다.")
            clients.remove(nickname)
            client_socket.close()
            break

def start_host():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)
    print("서버가 시작되었습니다. 클라이언트 연결을 기다립니다...")

    while True:
        client_socket, address = server_socket.accept()
        # 클라이언트가 접속할 때마다 스레드 생성
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

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