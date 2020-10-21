import os
import pickle
import datetime

class sport_club:
    def __init__(self):        # initialising 
        self.MRec=[]
        self.Mno=0
        self.Mname=""
        self.MSport=""
        self.MTransport=""
        self.Area=""
        self.Mfees=0
    print "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t","WELCOME TO THE SPORTS CLUB" 

    def Member_add(self):      #adding members
        print ("Enter Information for Membership")
        self.Mno=input("Enter member no. : ")
        self.Mname=raw_input("Enter member name : ").upper()
        self.MSport = raw_input("Enter sport name [F/B/C] : ").upper()
        if self.MSport=="F":
            self.Mfees=300
        if self.MSport=="B":
            self.Mfees=300
        if self.MSport=="C":
            self.Mfees==300
        if self.MSport=="F"and "C":
            self.Mfees==600
        if self.MSport=="C"and "F":
            self.Mfees==600
        if self.MSport=="F"and "B":
            self.Mfees==600
        if self.MSport=="B"and "F":
            self.Mfees==600
        if self.MSport=="B"and "C":
            self.Mfees==600
        if self.MSport=="C"and "B":
            self.Mfees==600

        
            
 
            
                
            
                
        print ("""Areas for which we provide transport
    1. Karama
    2. Bur Dubai
    3. Satwa
    4. Deira
    5. Qusais
    6. Sharjah
    """)
        self.MTransport=raw_input(" Do you want transport[Y/N]")
        if self.MTransport in ("Yesyes"):
            self.Transport_Info()
        if self.MTransport in ("Nono"):
            pass
    def Transport_Info(self):       #adding Transport
        self.Area=raw_input("Enter area[K/B/S/D/Q/S]").upper()
        if self.Area in ("KB"):
           self.Mfees+=250
        if self.Area in ("SD"):
            self.Mfees+=300
        if self.Area in ("QS"):
            self.Mfees+=350
        
    
        
    

    
    
    def M_output(self):             #displaying details
        X=open("Sports Club.dat","rb")
        """print ("\t\t Sport Club Management Database")        
        print ("\t\t===================================")
        CurDate = datetime.datetime.now()
        print ('\t\t\t\t\t\t\t\tDate: %d-%d-%d' % (CurDate.day, CurDate.month, CurDate.year))
        print ("{0:<20} {1:<30} {2:^15}".format("Member No.", "Member Name", "Sport","Transport","Area","Fees"))
        print ("-" * 100)
        """
        print self.Mno,
        print "\t""\t""\t",self.Mname,
        print "\t""\t""\t""\t",self.MSport,
        print "\t""\t",self.MTransport, 
        print "\t""\t",self.Area,
        print "\t""\t""\t""\t""\t",self.Mfees
       
                
               
def create():                       #creating file sportsclub
    X=open("Sports Club.dat","wb")
    S=sport_club()
    print(""" Different sports which we provide:
    1. Football
    2. Basketball
    3. Cricket""")
    ch=raw_input("Do you want to add members?-")
    while ch in ("Yesyes"):
        S.Member_add()
        pickle.dump(S,X)
        print " THANK YOU"
        ch=raw_input("Do you want to add members?:")
    X.close()


def display():                     #displaying the file
    X=open("Sports Club.dat","rb")
    print ("\t\t Sport Club Management Database")        
    print ("\t\t===================================")
    CurDate = datetime.datetime.now()
    print ('\t\t\t\t\t\t\t\tDate: %d-%d-%d' % (CurDate.day, CurDate.month, CurDate.year))
    print ("{0:<20} {1:<30} {2:^15}{3:<20} {4:<30} {5:^15}".format("Member No.", "Member Name", "Sport","Transport","Area","Fees"))
    print ("-" * 133)
    while True:
        try:
            S=pickle.load(X)
            S.M_output()
        except EOFError:
            pass
    X.close()

def delete():                       #deletion of a record
    print "Enter Information for Deletion"
    X=open("Sports Club.dat","rb")
    Y=open("Temp.dat","wb")
    record=int(input("Enter the Member No. to be Deleted"))
    try:
        while True:
            S=pickle.load(X)
            if S.Mno!=record:
                pickle.dump(S,Y)
    except EOFError:
        pass
    X.close()
    Y.close()
    os.remove("Sports Club.dat")
    os.rename("Temp.dat","Sports Club.dat")
     
def modify():                       #modifying a record
    X=open("Sports Club.dat","rb")
    Y=open("Temp.dat","wb")
    mod=int(input("Enter the Member No. to be Modified"))
    try:
        while True:
            S=pickle.load(X)
            if S.Mno==mod:
                S.Member_add()
                pickle.dump(S,Y)
    except EOFError:
        pass
    X.close()
    Y.close()


def Options():
    ans = "Y"                          #performing various function using the table
    while ans=="Y":
        print """Enter the function which you wish to perform:
    (1)Delete a record from the table
    (2)Modify a record in the table
    (3)Check the entered records
    (4)Check for the different events coming this month
    (5)Exit"""
        ch=input("Enter your choice:")
        if ch==1:
            delete()
        elif ch==2:
            modify()
        elif ch==3:
            display()
        elif ch==4:
            import Final2           #file imported Final2.py
            Final2.Login()
        elif ch==5:
            exit
        else:
            print "Invalid Input"
ans=raw_input("Do you wish to continue?:")
           
    

# main    
create()
S=sport_club()
Options()




        
        
        

  



