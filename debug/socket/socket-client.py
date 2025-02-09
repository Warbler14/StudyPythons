## CLIENT ##

import socket
from _thread import *

import uuid

HOST = '127.0.0.1' ## server에 출력되는 ip를 입력해주세요 ##
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def recv_data(client_socket):
    while True:
        data = client_socket.recv(1024)
        recive_decoded = repr(data.decode())
        print("recive : ", recive_decoded)

start_new_thread(recv_data, (client_socket,))
print('>> Connect Server')

client_uuid = uuid.uuid1()
print('client uuid : ' + str(client_uuid))
client_socket.send('abc'.encode())

#TODO 서버 연결이 끊어지면 자동 종료하는 기능 추가
while True:
    message = input()
    if message == 'quit':
        close_data = message
        break

    client_socket.send(message.encode())

client_socket.close()