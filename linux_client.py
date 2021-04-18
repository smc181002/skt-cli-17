import socket, threading, os, sys

skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip, port = "", 69

skt.bind((ip, port))

msgs = []

def print_msgs():
    os.system("clear")
    for msg in msgs:
        print(f"{msg['name']}  |> {msg['msg']}")
    print()

def send_msg():
    try:
        ip = sys.argv[1]
    except:
        pass

    while True:
        msg = input("Enter your message: ")
        msgs.append({"name": "you", "msg": msg})

        if msg == "/exit":
            os._exit(1)

        skt.sendto(msg.encode(),(ip, port))
        print_msgs()

def recv_msg():
    while True:
        data = skt.recvfrom(2048)

        msgs.append({"name": data[1][0], "msg": data[0].decode()})
        print_msgs()

thread_send = threading.Thread(target=send_msg)
thread_send.start()

thread_recv = threading.Thread(target=recv_msg)
thread_recv.start()