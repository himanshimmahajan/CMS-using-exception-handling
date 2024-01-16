""
"""CMS using OOPS with Exception handling
few operations say:
1.Add Customer
2.Search For Customer
3.Delete Customer
4.Modify Customer
5.Display All
6.Exit 
"""
import pickle
class Customer:
    cuslist=[]      #Static Variable
    def __init__(self): #self=1000
        self.id=0
        self.name = 0
        self.age=0
        self.mob = 0
    def addCustomer(self):  #self=1000, self=2000
        for cus in Customer.cuslist:
            if(cus.id==self.id):
                raise ValueError("Duplicate ID")
        Customer.cuslist.append(self)       #cuslist=[1000,2000,3000....
    def searchCustomer(self):   #self=9000, self.id=20, self.name=0....
        for e in Customer.cuslist:  #e=1000
            if(e.id==self.id):
                self.name=e.name    #self.name="Anil"
                self.age=e.age      #self.age=41
                self.mob=e.mob
                break       #return
        else:
            raise ValueError("ID not Found")
    def deleteCustomer(self):   #self=10000, self.id=30
        # for e in Customer.cuslist:
        #     if(e.id==self.id):
        #         Customer.cuslist.remove(e)
        #Another Way
        for i in range(len(Customer.cuslist)):      #i=0,1,2
            if(self.id==Customer.cuslist[i].id):
                Customer.cuslist.pop(i)
                return
    @staticmethod
    def deleteCustomerStatic(id):
        for i in range(len(Customer.cuslist)):      #i=0,1,2
            if(id==Customer.cuslist[i].id):
                Customer.cuslist.pop(i)
                return  #break
        else:
            raise ValueError("ID not Found")

    def modifyCustomer(self):       #self=11000, self.id=20,self.name="Banti"...
        for e in Customer.cuslist:  #e=1000
            if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
    @staticmethod
    def dumptoPickle():
        f=open("D:/vikas/cmsdata.txt","wb")
        pickle.dump(Customer.cuslist,f)
        f.close()

    @staticmethod
    def loadfromPickle():
        f = open("D:/vikas/cmsdata.txt", "rb")
        Customer.cuslist=pickle.load(f)
        f.close()
print("Welcome to Himanshi's CMS")

def getAge():
    while(1):
        age=input("Enter Cust Age:")
        if(age.isdecimal()):
            age=int(age)
            if(age>=10 and age<=110):
                return age
            else:
                print("Incorrect Age, Enter age between 10 to 110 only")
        else:
            print("Enter Age in Numbers Only")

def getMob():
    while(1):
        mob=input("Enter Mobile No:")
        if(len(mob)==10 and mob.isdecimal()):
            return mob
        else:
            print("Enter Mob No in Correct Format Only")


def showCustomer(e):        #e=1000
    print("Cust ID:",e.id,"Cust Name:",e.name,"Cust Age:",e.age,"Cust Mob:",e.mob)
while(1):
    cus=Customer() #cus=1000, 4 instance variables will be created, cus=9000
    choice=input("""Enter Choice: 1 Add Cust, 2 Search, 3 Delete, 4 Modify, 5 Display All, 
    6 Exit:, 7 Write In Pickle, 8 Load from Pickle: """)
    if(choice=="1"):    #Add Customer
        try:
            cus.id=input("Enter Customer Id:")          #cus.id=10
            cus.name=input("Enter Customer Name:")      #cus.name="vikas"
            cus.age=getAge()
            cus.mob=getMob()        #cus.mob=123
            cus.addCustomer()
            print("Customer Added Successfully")
        except Exception as err:
            print("Error!",err)
    elif(choice=="5"):  #Display All
        for e in Customer.cuslist:  #e=1000
            showCustomer(e)
    elif(choice=="2"):   #Search Cust, cus address 9000, cus.id=0,cus.name=0,cus.age=0,cus.mob=0
        try:
            cus.id=input("Enter Cust ID:")  #cus.id=20, 9000.id=20
            cus.searchCustomer()
            showCustomer(cus)
        except Exception as err:
            print("Error!",err)
    elif(choice=="3"):   #Delete Cust, cus=10000
        try:
            # cus.id=input("Enter Cust ID:")  #cus.id=30, 10000.id=30, 10000.name=0.....
            # cus.deleteCustomer()    #cus=10000
            id=input("Enter Customer ID:")
            Customer.deleteCustomerStatic(id)
            print("Customer Deleted Successfully")
        except Exception as err:
            print("Error",err)
    elif(choice=="4"):  #Modify Cust, cus=11000, cus.id=0,cus.name=0....
        try:
            cus.id=input("Enter Cust Id to Modify Cust:")   #cus.id=20
            cus.name=input("Enter Cust Updated Name:")      #cus.name="Banti"
            cus.age = input("Enter Cust Updated Age:")      #cus.age=42
            cus.mob = input("Enter Cust Updated Mob:")      #cus.mob=9212468020
            cus.modifyCustomer()
            print("Customer Modified Successfully")
        except Exception as err:
            print("Error!",err)
    elif(choice=="6"):
        print("Thanks for using Rahul's CMS")
        break
    elif(choice=="7"):  #Save data in Pickle Format
        Customer.dumptoPickle()
        print("Data Saved to Pickle Format Successfully")
    elif (choice == "8"):  # Load Data from Pickle Format
        Customer.loadfromPickle()
        print("Data Retrieved from Pickle Format Successfully")
    else:
        print("Incorrect Choice")


