from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Button as ButtonT
import requests

class AvatarHB:
    def __init__(self):
        super().__init__()
        ##CONFIG##
        self.root = Tk()
        self.root.title("Get Avatar 1.0")
        self.root.geometry("333x400+300+100")
        self.root.resizable(False,False)
        ##IMG##
        from PIL import Image, ImageTk
        
        load_img_bg = Image.open("img/bg.png"); ibg = ImageTk.PhotoImage(load_img_bg)
        load_img_iget = Image.open("img/get.png"); iget = ImageTk.PhotoImage(load_img_iget)
        load_img_iseu = Image.open("img/seu.png"); iseu = ImageTk.PhotoImage(load_img_iseu)
        load_img_isdu = Image.open("img/sdu.png"); isdu = ImageTk.PhotoImage(load_img_isdu)
        load_img_ised = Image.open("img/sed.png"); ised = ImageTk.PhotoImage(load_img_ised)
        load_img_isdd = Image.open("img/sdd.png"); isdd = ImageTk.PhotoImage(load_img_isdd)
        load_img_ihead = Image.open("img/avatar/4h.png"); ihead = ImageTk.PhotoImage(load_img_ihead)
        load_img_ibody = Image.open("img/avatar/4b.png"); ibody = ImageTk.PhotoImage(load_img_ibody)

        ##INST##
        self.posh = 4
        self.posb = 4
        self.background = Label(self.root,image=ibg).pack()
        self.btget = Button(image=iget, relief=FLAT, width=270,height=50,command=self.geti)
        self.sdu = Button(image=iseu, relief=FLAT,width=43,height=33,command=lambda: self.alpos(po="r",p="head"))
        self.seu = Button(image=isdu, relief=FLAT,width=43,height=33,command=lambda: self.alpos(po="l",p="head"))
        self.sdd = Button(image=ised, relief=FLAT,width=43,height=33,command=lambda: self.alpos(po="r",p="body"))
        self.sed = Button(image=isdd, relief=FLAT,width=43,height=33,command=lambda: self.alpos(po="l",p="body"))
        self.lhead = Button(image=ihead)
        self.lbody = Button(image=ibody)
        self.enick = Entry(width=10,font="Terminal 27")
        ##PLACE##
        self.sdd.focus_set()
        self.sdu.focus_set()
        self.sed.focus_set()
        self.seu.focus_set() 

        self.btget.place(x=32,y=18)
        self.sdu.place(x=230,y=120)
        self.sdd.place(x=230,y=240)
        self.seu.place(x=50,y=120)
        self.sed.place(x=50,y=240)
        self.lhead.place(x=132,y=95)
        self.lbody.place(x=132,y=195)
        self.enick.place(x=110,y=353)

        self.root.mainloop()

    def geti(self,gesture="sml",size="l"):
        pathl = False
        ptht = [('PNG.', '.png'),
        ('JPG.', '.jpg'),
        ('All files', '*')]
        if (self.enick.get() != ""):
            try:
                pth = asksaveasfilename(filetypes=ptht, defaultextension = '.png',title="Save avatar") 
                url = "https://www.habbo.com.br/habbo-imaging/avatarimage?img_format=gif&user={}&action=std&direction={}&head_direction={}&gesture={}&size={}".format(self.enick.get(),self.posb,self.posh,gesture,size)
                link = requests.get(url)    
                path = pth + ".png"
                with open(path,"wb") as f:
                    f.write(link.content)    
            except:
                messagebox.showerror("Nick Not Found!","The nickname don't exists")
        elif self.enick.get() == "":
            messagebox.showerror("Nickname is invalid","The nickname don't exists")
        else:
            messagebox.showerror("Path Don't Found","Please, select a path to continue")


            
    def alpos(self,po,p):   
        self.sdd.focus_set()
        self.sdu.focus_set()
        self.sed.focus_set()
        self.seu.focus_set() 
        from PIL import Image, ImageTk

        if po=="l"and p=="head": self.posh = self.posh + 1
        elif po=="r" and p=="head":self.posh = self.posh - 1
        elif po=="l"and p=="body": self.posb = self.posb + 1
        elif po=="r"and p=="body": self.posb = self.posb - 1
        if self.posh>8:self.posh = 1
        if self.posb>8:self.posb = 1
        elif self.posh==0: self.posh=8
        elif self.posb==0: self.posb=8

        pathh = "img/avatar/{}h.png".format(self.posh)
        pathb = "img/avatar/{}b.png".format(self.posb)

        img1 = ImageTk.PhotoImage(Image.open(pathh))
        self.lhead.configure(image=img1)
        self.lhead.image = img1

        img = ImageTk.PhotoImage(Image.open(pathb))
        self.lbody.configure(image=img)
        self.lbody.image = img         
        
AH = AvatarHB
AH()