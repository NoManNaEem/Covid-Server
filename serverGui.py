

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



# def vp_start_gui():
#     '''Starting point when module is the main routine.'''
    # global val, w, root
import socket, threading
from covid import Covid
from pandas import Series
from pandas import DataFrame

class ClientThread(threading.Thread):
    


    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        print ("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        while(True):
            msg = ''
            print(msg)
            
            
            covid = Covid()      
            data = self.csocket.recv(2048)

            msg = data.decode()
            top.Text1.insert('1.0',("\nFrom Server :: "+msg))
            if msg=="Active":
                print ("from client", msg)
                msg=str(covid.get_total_active_cases())
                
            
                top.Text1.insert('1.0',("\nsent :: "+msg))
                    
                # msg=covid.get_total_active_cases()
                self.csocket.send(bytes(msg,'UTF-8'))
            elif msg=="Conferm":
                print ("from client", msg)
                msg=str(covid.get_total_confirmed_cases())
                
                # print("sent = ",msg)
                top.Text1.insert('1.0',("\nsent :: "+msg))
                    
                # msg=covid.get_total_active_cases()
                self.csocket.send(bytes(msg,'UTF-8'))
            elif msg=='Deaths':
                print ("from client", msg)
                msg=str(covid.get_total_deaths())
                
                # print("sent = ",msg)
                top.Text1.insert('1.0',("\nsent :: "+msg))
                    
                # msg=covid.get_total_active_cases()
                self.csocket.send(bytes(msg,'UTF-8'))
            elif msg=='Recover':
                print ("from client", msg)
                msg=str(covid.get_total_recovered())
                
                # print("sent = ",msg)
                top.Text1.insert('1.0',("\nsent :: "+msg))
                    
                # msg=covid.get_total_active_cases()
                self.csocket.send(bytes(msg,'UTF-8'))
            else:
                try:
                    print ("from client", msg)
                    Series1=Series(covid.get_status_by_country_name(msg))
                    x=Series1.to_string()
                    
                    print("sent = ",Series1)
                        
                    # msg=covid.get_total_active_cases()
                    self.csocket.send(bytes(x,'UTF-8'))        
                except Exception:
                    x="Invalid"  
                    self.csocket.send(bytes(x,'UTF-8'))                                   
              
            
        print ("Client at ", clientAddress , " disconnected...")


top = tk.Tk()
    # top = Toplevel1 (root)
    # unknown_support.init(root, top)
    

# w = None
# def create_Toplevel1(rt, *args, **kwargs):
#     '''Starting point when module is imported by another module.
#        Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
#     global w, w_win, root
#     #rt = root
#     root = rt
#     w = tk.Toplevel (root)
#     top = Toplevel1 (w)
#     unknown_support.init(w, top, *args, **kwargs)
#     return (w, top)

        
        # _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        # _fgcolor = '#000000'  # X11 color: 'black'
        # _compcolor = '#d9d9d9' # X11 color: 'gray85'
        # _ana1color = '#d9d9d9' # X11 color: 'gray85'
        # _ana2color = '#ececec' # Closest X11 color: 'gray92'

top.geometry("773x526+550+210")
top.title("SERVER")
top.minsize(176, 1)
top.maxsize(1924, 1050)
top.resizable(1,  1)


top.configure(background="#ffffff")
top.configure(highlightbackground="#d9d9d9")
top.configure(highlightcolor="black")

top.Label1 = tk.Label(top)
top.Label1.place(relx=0.272, rely=0.038, height=121, width=316)
top.Label1.configure(activebackground="#000000")
top.Label1.configure(activeforeground="white")
top.Label1.configure(activeforeground="black")
top.Label1.configure(background="#000000")
top.Label1.configure(disabledforeground="#a3a3a3")
top.Label1.configure(font="-family {Verdana} -size 19 -weight bold")
top.Label1.configure(foreground="#f8f8f8")
top.Label1.configure(highlightbackground="#d9d9d9")
top.Label1.configure(highlightcolor="black")
top.Label1.configure(text='''SERVER''')

top.Text1 = tk.Text(top)
top.Text1.place(relx=0.116, rely=0.361, relheight=0.464, relwidth=0.73)
top.Text1.configure(background="#1f1f1f")
top.Text1.configure(font="TkTextFont")
top.Text1.configure(foreground="#f7f7f7")
top.Text1.configure(highlightbackground="#d9d9d9")
top.Text1.configure(highlightcolor="black")
top.Text1.configure(insertbackground="black")
top.Text1.configure(selectbackground="blue")
top.Text1.configure(selectforeground="white")
top.Text1.configure(wrap="word")

LOCALHOST = "localhost"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
top.Text1.insert('1.0',"\nServer started")
# print("Server started")
print("Waiting for client request..")
server.listen(1)
clientsock, clientAddress = server.accept()
newthread = ClientThread(clientAddress, clientsock)
newthread.start()
top.Text1.insert('1.0',"\nConnection Successfull")



top.mainloop()





