import socket


def start_host():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # 호스트의 IP와 포트 설정
    server_socket.listen(5)

    print("경매 서버가 시작되었습니다. 클라이언트를 기다립니다...")
    print("내 IP 주소 : ", socket.gethostbyname(socket.gethostname()))
    client_socket, address = server_socket.accept()
    print(f"클라이언트가 연결되었습니다: {address}")

    # 경매 상품 설정
    auction_item = input("경매할 상품을 입력하세요: ")
    start_price = input(f"{auction_item}의 시작 가격을 입력하세요: ")

    # 클라이언트에게 경매 정보 전송
    auction_info = f"경매 상품: {auction_item}, 시작 가격: {start_price}"
    client_socket.send(auction_info.encode())

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_host()