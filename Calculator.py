
from tkinter import Tk, W, E,StringVar
from tkinter.ttk import Frame, Button, Entry, Style

class Example(Frame):
    def cycle_label_text(self, event):
        global label_text
        label_text.set("")
    def clear(self):
        global label_text
        global expression
        label_text.set("")
        expression = ""
    def press(self,key):
        global label_text
        global expression
        expression = expression+str(key)
        label_text.set(expression)
    def press_equal(self,key):
        global label_text
        global expression
        expression = str(eval(expression))
        label_text.set(expression)
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
        
    def initUI(self):
      
        self.master.title("Calculator",)
        
        Style().configure("TButton", padding=(0, 5, 0, 5), 
            font='serif 10')
        
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3) 
        
        global expression
        expression = ""
        global label_text
        label_text = StringVar()
        label_text.set("Enter Here...")
        entry = Entry(self,textvariable=label_text)
        entry.grid(row=0, columnspan=4, sticky=W+E)
        entry.bind("<Button-1>", self.cycle_label_text)
        #entry.pack()
        cls = Button(self, text="Cls",command = self.clear)
        cls.grid(row=1, column=0)
        bck = Button(self, text="Back")
        bck.grid(row=1, column=1)
        lbl = Button(self)
        lbl.grid(row=1, column=2)    
        clo = Button(self, text="Close",command = self.quit)
        clo.grid(row=1, column=3)        
        sev = Button(self, text="7", command= lambda: self.press(7))
        sev.grid(row=2, column=0)        
        eig = Button(self, text="8", command = lambda: self.press(8))
        eig.grid(row=2, column=1)         
        nin = Button(self, text="9", command = lambda: self.press(9))
        nin.grid(row=2, column=2) 
        div = Button(self, text="/", command = lambda: self.press('/'))
        div.grid(row=2, column=3) 
        
        fou = Button(self, text="4", command = lambda: self.press(4))
        fou.grid(row=3, column=0)        
        fiv = Button(self, text="5", command = lambda: self.press(5))
        fiv.grid(row=3, column=1)         
        six = Button(self, text="6", command = lambda: self.press(6))
        six.grid(row=3, column=2) 
        mul = Button(self, text="*", command = lambda: self.press("*"))
        mul.grid(row=3, column=3)    
        
        one = Button(self, text="1", command = lambda: self.press(1))
        one.grid(row=4, column=0)        
        two = Button(self, text="2", command = lambda: self.press(2))
        two.grid(row=4, column=1)         
        thr = Button(self, text="3", command = lambda: self.press(3))
        thr.grid(row=4, column=2) 
        mns = Button(self, text="-", command = lambda: self.press("-"))
        mns.grid(row=4, column=3)         
        
        zer = Button(self, text="0", command = lambda: self.press(0))
        zer.grid(row=5, column=0)        
        dot = Button(self, text=".", command = lambda: self.press("."))
        dot.grid(row=5, column=1)         
        equ = Button(self, text="=", command = lambda: self.press_equal("="))
        equ.grid(row=5, column=2) 
        pls = Button(self, text="+", command = lambda: self.press("+"))
        pls.grid(row=5, column=3)
        
        self.pack()
        
   
     

def main():
  
    root = Tk()
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()  
