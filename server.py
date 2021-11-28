from socket import *
from tkinter import *
import threading

class Server(Tk):
    def __init__(self):
        super().__init__()
        self.config(bg='lightgrey')

        self.geometry('500x500')

        self.dialog_win=Text(self,width=40,height=25,bg='grey')
        self.dialog_win.place(x=5,y=5)


        self.sockobj = socket(AF_INET, SOCK_STREAM)
        self.sockobj.bind(('', 5401))
        self.sockobj.listen(5)


        server_tread=threading.Thread(target=self.start)
        server_tread.daemon=True
        server_tread.start()


    def start(self):
        while True:
          connection, address = self.sockobj.accept()  # ждем сообщение от клиента, устонавливаем соединение с клиентом, получаем ip адрес

          bin_data = connection.recv(1024)  # количество байтов
          self.str_data = bin_data.decode('utf-8')



          ip_addr = address[0]
          self.dialog_win.insert(END,'Server get a message',+' '+'from','',ip_addr,': ', self.str_data+'\n\n')

          str_answer = ip_addr +':'+ self.str_data

          connection.send(str_answer.encode('utf-8'))
          connection.close()

s=Server()
s.mainloop()
