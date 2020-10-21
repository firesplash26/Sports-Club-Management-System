import Tkinter             #imported module Tkinter



def Login():               #for logging in (GUI part)
    global entUsername
    window=Tkinter.Tk()
    window.configure(background="#a1dbcd")
    window.title("Welcome")
    lblHead=Tkinter.Label(window,text="WELCOME TO THE SPORTS CLUB!",fg="#383a39",bg="#a1dbcd",font=("Helvetica",16))
    lblHead.pack()
    lblInst=Tkinter.Label(window,text="Please login to continue:",fg="#383a39",bg="#a1dbcd",font=("Helvetica",16))
    lblInst.pack()
    lblUsername=Tkinter.Label(window,text="Username:",fg="#383a39",bg="#a1dbcd")
    entUsername=Tkinter.Entry(window)       #username= your name 
    lblUsername.pack()
    entUsername.pack()
    lblPassword=Tkinter.Label(window,text="Password:",fg="#383a39",bg="#a1dbcd")
    entPassword=Tkinter.Entry(window)       #password:sportclub
    lblPassword.pack()
    entPassword.pack()
    btn=Tkinter.Button(window,text="Login",command=Register,fg="#a1dbcd",bg="#383a39")
    btn.pack()
    window.mainloop()
    
def Register():                             #registering for the upcoming events
    print "\t\t\t\t\t\t\t","""**************************** THE UPCOMING EVENTS THIS MONTH ****************************
(1) Swiming 100m-(Freestyle/Backstroke-stroke/Butterfly)----------------- (on 1st February 2016)REGISTER? (Y/N)
(2) Tri-athon (includes: Swimming,Cycling,Hundred Metre Running Race)----------------- (on 20th February 2016)REGISTER?(Y/N)
(3) Running Race- (100m,200m,400m)----------------------------------------------------(on 28th February 2016)REGISTER?(Y/N)
(4)Exit"""
    chregi=raw_input("Do u want to register for any event(Y/N):")
    
    while chregi=='Y':
        
        ch=input("enter the event u want to participate(1,2,3,4):")
        if ch==1:
            chswim=raw_input("enter the Style (Freestyle/Backstroke-stroke/Butterfly):")
            print entUsername,"u have successfully registered for the swimming event:",chswim
        if ch==2:
            
            print entUsername,"u have successfully registered for the triathon event:"
        if ch==3:
            chrun=raw_input("enter the Style (100m,200m,400m):")
            print entUsername,"u have successfully registered for the running event for",chrun
        if ch==4:
            import Final1             #imported Final1.py
            Final1.Options()
        if ch==5:
            break
        
        
        chregi=raw_input("Enter 'Y' to continue : ")
    
   



Login()



