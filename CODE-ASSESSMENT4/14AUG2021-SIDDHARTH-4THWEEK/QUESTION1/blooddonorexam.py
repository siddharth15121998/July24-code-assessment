'''Below is the menu driven program for blood donation bank'''
# importing modules
from enum import EnumMeta
import validatedonor
from os import name
import logging,smtplib,pymongo,collections
from pymongo import collection
import smtplib

#creating log file
logging.basicConfig(filename='bloodlog.log',level=logging.INFO)

#creating connection to MongoDB
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=client["BloodbankDb"]
blood1=mydb["BloodbankDonations"]

listemail=[]

#Applying OOPS concept
class BloodBank:
    def adddonors(self,name,address,bloodgroup,pincode,mobile,lastdonatedate,place,email):
        listemail.append(email)
        infodict={"name":name,"address":address,"bloodgroup":bloodgroup,"pincode":pincode,"mobile":mobile,"lastdateofdonation":lastdonatedate,"place":place,"email":email,"status":0}
        ordereddict=collections.OrderedDict(infodict)
        return ordereddict
print("--------------Welcome To Blood Donor Bank-------------")
print("\n")
print("*******Every Drop Of Blood Can give a Life*******")
print("\n")
while(True):
    print("1. Add Donor:")
    print("2. Search donor based on bloodgroup: ")
    print("3. Search Donors based on blood group and place: ")
    print("4. Update all the donor details with their mobile number: ")
    print("5. Delete the donor using mobile number: ")
    print("6. Display the total number of donors on each blood group: ")
    print("7. Immediate notification to all via email: ")
    print("8.-----EXIT-----")
    try:
        choice=int(input("enter your choice: "))
    except:
        logging.error("User entered wrong choice")
        break
    if choice==1:
        #while(True):
            name=input("Enter your name: ")
            address=(input("enter your address: "))
            bloodgroup=(input("enter your bloodgroup: ")).upper()
            pincode=(input("enter your pincode: "))
            mobile=(input("enter your mobile: "))
            last=(input("enter your lastdonate date: "))
            place=(input("enter your place: "))
            email=(input("enter your email: "))
            if validatedonor.validation_of_Donor(name,pincode,mobile,email):
                bloodobj=BloodBank()
                detailss=bloodobj.adddonors(name,address,bloodgroup,pincode,mobile,last,place,email)
                blood1.insert_one(detailss) 
                       
            else:
                print("Please Try again by entering valid details")
                continue
            break
    
    if choice==2:
        bloodgroup=input("Enter your blood group: ")
        res=blood1.find({"$and":[{"bloodgroup":bloodgroup},{"status":0}]})
        for i in res:
            print(i)
         
    
    if choice==3:
        bg=input("Enter your bloodgroup: ")
        place=input("Enter your place: ")
        res=blood1.find({"$and":[{"bloodgroup":bg},{"place":place},{"status":0}]})
        for i in res:
            print(i)

    if choice==4:
        print("Enter mobile number of donor whose data has to be updated :")
        mobile=input("Enter your mobile number:")
        print("Enter updated details of donor :")
        name=input("Enter your name: ")
        address=(input("enter your address: "))
        bloodgroup=(input("enter your bloodgroup: ")).upper()
        pincode=(input("enter your pincode: "))
        last=(input("enter your lastdonate date: "))
        place=(input("enter your place: "))
        
        res=blood1.update_one({"$and":[{"mobile":mobile},{"status":0}]},{"$set":{"name":name,"address":address,"bloodgroup":bloodgroup,"pincode":pincode,"lastdateofdonation":last,"place":place,"email":email}})

    if choice==5:
        print("Enter mobile number of donor whose data has to be deleted :")
        mobile=input("Enter your mobile number:")
        res=blood1.update_one({"$and":[{"mobile":mobile}]},{"$set":{"status":1}})

    if choice==6:
        res=blood1.aggregate([{"$group":{"_id":"$bloodgroup","totaldonor":{"$sum":1}}}])
        for i in res:
            print(i)
    
    if choice==7:
        message=input("Enter a message to all donors: ")
        connection=smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login("hariompateldada@gmail.com","Sparsh@01")
        connection.sendmail("hariompateldada@gmail.com",listemail,message)
        print("!!! Email Sent !!!")
        connection.quit()

    if choice==8:
        break