
from covid import Covid

from pandas import Series
import pyttsx3
# from subprocess import call as say
import winsound
import time
import speech_recognition as sr
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import socket

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

SERVER = "localhost"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
# client.sendall(bytes("This is from Client", 'UTF-8'))


    # if out_data == 'bye':
    #     break

# Data = 0
engine = pyttsx3.init()
def say(x):
    engine.say(x)
    # time.sleep(3.0)
    engine.runAndWait()
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)

    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    # unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def server(s):
    
    
    out_data = s
    client.sendall(bytes(out_data, 'UTF-8'))
    in_data = client.recv(1024)
    print("From Server :", in_data.decode())
    return in_data.decode()

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def exit():
        # out_data = "exit"
        # client.sendall(bytes(out_data, 'UTF-8'))

        root.destroy()

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("998x753+365+107")
        top.minsize(176, 1)
        top.maxsize(1924, 1050)
        top.resizable(1,  1)
        top.title("COVID INFO TRACKER")
        top.configure(background="#61649e")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.04, rely=0.04, relheight=0.117, relwidth=0.514)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Message1 = tk.Message(self.Frame1)
        self.Message1.place(relx=-0.019, rely=0.0, relheight=0.989
                , relwidth=1.037)
        self.Message1.configure(background="#400040")
        self.Message1.configure(font="-family {@Malgun Gothic} -size 12 -weight bold")
        self.Message1.configure(foreground="#fff7f7")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''COVID INFO SYSTEM BY LEADERS''')
        self.Message1.configure(width=532)

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.04, rely=0.186, relheight=0.367, relwidth=0.516)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#1b1b1b")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.TEntry1 = ttk.Entry(self.Frame2)
        self.TEntry1.place(relx=0.272, rely=0.761, relheight=0.112
                , relwidth=0.633)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")
 
        top.bind("<Escape>", exit)
        # entry=self.TEntry1.get()
        

        def plot(): 
                plotwin=tk.Tk()
                plotwin.geometry("400x400")
                plotwin.title("Graph")

            
  
                # the figure that will contain the plot 
                fig = Figure(figsize = (5, 5), 
                             dpi = 100) 
              
                # list of squares 
                # y = [i**2 for i in range(101)] 
              
                # adding the subplot 
                # plot1 = fig.add_subplot(111) 
              
                # plotting the graph 
                # covid = Covid()
                # DeathData=(covid.get_total_deaths())
               
                 # list of squares 
                covid = Covid()
                Data=(covid.get_total_confirmed_cases())
                y = [i**2 for i in range(111)] 
              
                # adding the subplot 
                plot1 = fig.add_subplot(111) 
                plot1.plot(y) 
  
                # creating the Tkinter canvas 
                # containing the Matplotlib figure 
                canvas = FigureCanvasTkAgg(fig, 
                                           master = plotwin)   
                canvas.draw() 
              
                # placing the canvas on the Tkinter window 
                canvas.get_tk_widget().pack() 
              
                # creating the Matplotlib toolbar 
                toolbar = NavigationToolbar2Tk(canvas, 
                                               plotwin) 
                toolbar.update() 
  
              # placing the toolbar on the Tkinter window 
                canvas.get_tk_widget().pack()     
                plotwin.mainloop    


        

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.05, rely=0.584, relheight=0.377, relwidth=0.495)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")
        # self.Text1.insert('1.0')
        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.581, rely=0.053, relheight=0.402
                , relwidth=0.379)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.M = tk.Message(self.Canvas1)
        self.M.pack(fill="both")   

        
        listener=sr.Recognizer()
        
        def Speach():          
            try :
                with sr.Microphone() as source:
                    # self.M.insert('1.0',"Listening.......")
                    # say('espeak '+"Say,,your,,command,,after,,the,,beep", shell=True)
                    winsound.Beep(1000,500)
                    print("listening...")
                    voice = listener.listen(source)
                    command=listener.recognize_google(voice)
                    command=command.lower()
                    if "active" in command:
                        active()
                        # print(command)
                    if "confirm" in command:    
                        Conferm()
                        
                    if "death"in command:
                        Deaths()
                    if "recover" or "recovered" in command:  
                        Recoverd()

                    else:
                        engine.say("INVALID SPEACH")
                        # Country()   

    
            except Exception :
                print("ex")
        self.B=tk.Button(self.Canvas1)
        self.B.configure(text=" VOICE SEARCH ")
        self.B.pack()
        self.B.configure(command=Speach)

             

        Data=0

        def active():
            self.Text1.delete('1.0' , tk.END)
            # print("hello")
            # covid = Covid()
            # ActiveData=(covid.get_total_active_cases())
            # Data=int(ActiveData)
     
            # x=str(ActiveData)
            out_data = "Active"
            client.sendall(bytes(out_data, 'UTF-8'))
            in_data = client.recv(1024)
            print("From Server :", in_data.decode())
     
            
            ActiveData="Active Cases= "+in_data.decode()

            self.Text1.insert('1.0',ActiveData)
            engine.say(ActiveData)
            engine.runAndWait()
        def Recoverd():
            self.Text1.delete('1.0' , tk.END)
            # print("hello")
            # covid = Covid()
            # RecoverdData=(covid.get_total_recovered())
            # Data=RecoverdData
            # x=str(RecoverdData)
            out_data = "Recover"
            client.sendall(bytes(out_data, 'UTF-8'))
            in_data = client.recv(1024)
            # print("From Server :", in_data.decode())
     
        
            RecoverdData="Recoverd Cases = "+in_data.decode()  
            self.Text1.insert('1.0',RecoverdData)
            engine.say(RecoverdData)
            engine.runAndWait()  
        def Deaths():
            self.Text1.delete('1.0' , tk.END)
            # print("hello")
            # covid = Covid()
            # DeathData=(covid.get_total_deaths())
            
            # Data=DeathData
            # x=str(DeathData)
            out_data = "Deaths"
            client.sendall(bytes(out_data, 'UTF-8'))
            in_data = client.recv(1024)
            # print("From Server :", in_data.decode())
     
            DeathData="Deaths Cases = "+in_data.decode()

            self.Text1.insert('1.0',DeathData)
            engine.say(DeathData)
            engine.runAndWait()  
        def Conferm():
            self.Text1.delete('1.0' , tk.END)
            # print("hello")
            # covid = Covid()
            # ConfermData=(covid.get_total_confirmed_cases())
            # Data=ConfermData
            # x=str(ConfermData)
            out_data = "Conferm"
            client.sendall(bytes(out_data, 'UTF-8'))
            in_data = client.recv(1024)
            # print("From Server :", in_data.decode())
            ConfermData="Conferm Cases = "+in_data.decode()
            self.Text1.insert('1.0',ConfermData)  
            engine.say(ConfermData)
            engine.runAndWait()            
        def Country():
            self.Text1.delete('1.0' , tk.END)
            try:
                # covid = Covid()
                # Series1=Series(covid.get_status_by_country_name(self.TEntry1.get()))
                x=self.TEntry1.get()
                out_data = x
                client.sendall(bytes(out_data, 'UTF-8'))
                in_data = client.recv(1024)
                # print("From Server :", in_data.decode())
                Series1=in_data.decode()   
                self.Text1.insert('1.0',Series1) 
                # time.sleep(10)

                say(Series1)
                  
                # engine.say(Series1)
                # engine.runAndWait()                
            except Exception : 
                self.Text1.insert('1.0',"INVALID COUNTRY")    
                

            
        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.913, rely=0.761, height=32, width=38)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#fbfbfb")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''^''')   
        self.Button1.configure(command=Country) 

        self.active = ttk.Button(self.Frame2)
        self.active.place(relx=0.019, rely=0.072, height=35, width=160)
        self.active.configure(takefocus="")
        self.active.configure(text='''Active Cases''')
        self.active.configure(command=active)

        self.conferm = ttk.Button(self.Frame2)
        self.conferm.place(relx=0.35, rely=0.326, height=35, width=210)
        self.conferm.configure(takefocus="")
        self.conferm.configure(text='''Total Confirm Cases''')
        self.conferm.configure(command=Conferm)

        self.recover = ttk.Button(self.Frame2)
        self.recover.place(relx=0.369, rely=0.072, height=35, width=170)
        self.recover.configure(takefocus="")
        self.recover.configure(text='''Total Recovered''')
        self.recover.configure(command=Recoverd)

        self.deaths = ttk.Button(self.Frame2)
        self.deaths.place(relx=0.019, rely=0.326, height=35, width=140)
        self.deaths.configure(takefocus="")
        self.deaths.configure(text='''Total Deaths''')
        self.deaths.configure(command=Deaths)

        

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.019, rely=0.58, height=28, width=167)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#404040")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {@Arial Unicode MS} -size 9")
        self.Label1.configure(foreground="#fefffb")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Country wise Data''')

        self.Label2 = tk.Label(self.Frame2)
        self.Label2.place(relx=0.019, rely=0.761, height=28, width=117)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="#f4f4f4")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Country Name''')

        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.601, rely=0.584, relheight=0.377
                , relwidth=0.366)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")

        self.Label3 = tk.Label(self.Frame3)
        self.Label3.place(relx=0.082, rely=0.06, height=26, width=297)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {@Arial Unicode MS} -size 11 -weight bold")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''TEAM MEMBERS''')

        self.Label4 = tk.Label(self.Frame3)
        self.Label4.place(relx=0.055, rely=0.239, height=35, width=207)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''     ->MALIK NOMAN NAEEM''')

        self.Label4_1 = tk.Label(self.Frame3)
        self.Label4_1.place(relx=0.055, rely=0.479, height=34, width=257)
        self.Label4_1.configure(activebackground="#f9f9f9")
        self.Label4_1.configure(activeforeground="black")
        self.Label4_1.configure(background="#d9d9d9")
        self.Label4_1.configure(disabledforeground="#a3a3a3")
        self.Label4_1.configure(foreground="#000000")
        self.Label4_1.configure(highlightbackground="#d9d9d9")
        self.Label4_1.configure(highlightcolor="black")
        self.Label4_1.configure(text='''->MUHAMMAD HASHIM KHAN''')

        self.Label4_2 = tk.Label(self.Frame3)
        self.Label4_2.place(relx=0.055, rely=0.715, height=35, width=157)
        self.Label4_2.configure(activebackground="#f9f9f9")
        self.Label4_2.configure(activeforeground="black")
        self.Label4_2.configure(background="#d9d9d9")
        self.Label4_2.configure(disabledforeground="#a3a3a3")
        self.Label4_2.configure(foreground="#000000")
        self.Label4_2.configure(highlightbackground="#d9d9d9")
        self.Label4_2.configure(highlightcolor="black")
        self.Label4_2.configure(text='''        ->HASEEB AHMED''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.671, rely=0.505, height=31, width=216)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#000000")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#fdfdfd")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="#ffffff")
        self.Label5.configure(text='''Developed by team LEADERS''')
        
        self.g=tk.Button(self.Canvas1)
        self.g.configure(text="Graph")
        self.g.pack()
        self.g.configure(command=plot)

        # top.bind("<F1>", plot())
        


    
        


if __name__ == '__main__':
    vp_start_gui()






