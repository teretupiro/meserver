from socket import*
from tkinter import*

class Client(Tk):
    def __init__(self):
        super().__init__()
        self.config(bg='lightgrey')

        self.geometry('500x500')

        self.dialog_win=Text(self,width=40,height=25,bg='grey')
        self.dialog_win.place(x=5,y=5)



        self.msg_entry=Entry(self,width=35)
        self.msg_entry.place(x=5,y=450)

        self.send_btn=Button(self,text='Send',command=self.put_msg)
        self.send_btn.place(y=450,x=400)

        self.socket_settings()

    def put_msg(self):
        text=self.msg_entry.get()
        self.send_msg(text)

    def socket_settings(self):
        self.server_address=('localhost',5401)

    def send_msg(self,msg):
        bin_msg=bytes(msg,'utf-8')

        client=socket(AF_INET,SOCK_STREAM)
        try:
            client.connect(self.server_address)
            client.sendall(bin_msg)
            data=client.recv(1024)
            self.print_text(data.decode('utf-8'))
        except:
            self.print_text('not connected')
        finally:
            client.close()

    def print_text(self,text):
        self.dialog_win.insert(END,text+'\n\n')

c=Client()
c.mainloop()




