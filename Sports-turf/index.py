#BOOK MY TURF

################################################################################
#IMPORTS and GLOBAL DECLARATIONS
################################################################################
import random    
import tabulate      
import datetime 
from datetime import date
                
users = {'afsal':'passd1', 'uma':'passd2', 'aswathy':'passd3'}
 
userkey = list(users.keys())
uservalue = list(users.values())

managers = {'manager1':'passw1', 'manager2':'passw2'}
managerkey = list(managers.keys())
managervalue = list(managers.values()) 

b=(1,2,3,4,5)
f = ["Nice parking area,Nice turf,Nice shuttle court ",
     "\n One of the best turf in Thrissur. High quality grass and well maintaned. Very good customer service and the quality of the turf. A must go to turf in Thrissur ",
     "\n I think its a good turf in the city. Its very affordable and gives us a good kick in football. Very clean place and more interactive enviornment. The only thing that pull me over is, it is very hot and you cannot even play for one hour. I think night time is more comfortable than day time here."]

shopping = [{"id":1001, "Name":"Football Cosco", "Available":100, "price":349, "Original price":560},
            {"id":1002, "Name":"Football Nivia", "Available":100, "price":489, "Original price":525},
            {"id":1003, "Name":"Nivia Football pump", "Available":100, "price":235, "Original price":265},
            {"id":1004, "Name":"LDR Football pump", "Available":100, "price":169, "Original price":299},
            {"id":1005, "Name":"Addidas Football Spikes", "Available":100, "price":3200, "Original price":4200}]

pid = [1001, 1002, 1003, 1004, 1005]
shopping1 = shopping
temp=[]
order=""
################################################################################
# FUNCTIONS
################################################################################
#Display Menu
def shoppingtable():      
  header = shopping[0].keys()
  rows = [x.values() for x in shopping ]
  print(tabulate.tabulate(rows,header,tablefmt='grid'))

#Register
def register():        
  fullname = input("Enter your fullname: ")
  email = input("Enter your valid email: ")
  username = input("Enter Username: ")
  password = input("Enter Password: ")
  password1 = input("Confirm Password: ")
  if password==password1:
    print("REGISTER SUCCESSFUL!")
    users.update({username:password})
    userkey.append(username)
    uservalue.append(password)
  else:
    print("Please Recheck Your Password.")
    register()

#Add Manager
def addmanager():      
  name = input("Name of the Manager: ")
  username = input("Enter Username: ")
  password = input("Enter  Password: ")
  mobile = input("Enter  Mobile number: ")
  if(len(mobile)==10):
    location=input("Enter the Location: ")
    print("Add Manager?")
    print("1.Yes")
    print("2.No")
    s=int(input("Enter Your Choice: "))
    if s==1:        
      print("Added Manager Successfully!")
      managers.update({username:password})
      managerkey.append(username)
      managervalue.append(password)
      print(managers)
    else:
      print("Manager not added")
  else:
    print("Invalid Mobile Number, Try Again!!") 
    addmanager()

#Remove Manager
def removemanager():  
  username = input("Enter Username: ")
  password = input("Enter Password: ")
  if username in managerkey:
    if password in managervalue:
      print("Do You Want to Remove?")
      print("1.Yes")
      print("2.No")
      s=int(input("Enter Your Choice: "))
      if s==1:
        print("Removed Manager.")
        managers.pop(username)
        managerkey.remove(username)
        managervalue.remove(password)
        print(managers)
      else:
        print("Manager not removed.")
    else:          
      print("Manager Not found. (Password not matching).")
  else:
    print("Manager Not found. Please retry username and password.")
    removemanager()
#Add Products
def addproducts():      
  n = int(input("Enter the no of items need to be added: "))
  for i in range(n):
    new_id = int(input("Enter id: "))
    new_name = input("Enter name: ")
    new_Available = int(input("Enter Available: "))
    new_price = int(input("Enter price: "))
    new_original = int(input("Enter the original price: "))
    d=[{"id": new_id, "Name": new_name, "Available": new_Available, "price": new_price, "original price": new_original}]
    shopping.extend(d) 
    pid.append(new_id)

#Remove products
def removeitem():   
  shoppingtable()
  shoppingid = int(input("Enter the product id that needs to be deleted: "))
  found = False
  for d in shopping1:
    found = d["id"]==shoppingid
    if found!=True:
      temp.append(d)
      continue                      
    else :
      d["Available"]-=1
  print("Deleting item......")  
  if shoppingid in pid:
    print(f"{shoppingid}'s one available is removed from the list")
  else :
    print(f"{shoppingid} not found!")

#Available products
def availableproducts(): 
  Total=0
  for d in shopping :
    print(f'{d["Name"]}={["Available"]}')
    Total = Total + d["Available"]
    print("\n Total available goods is: ",Total)

#Place order         
def placeorder():        
  order_number = 10
  shoppingtable()
  p_id = int(input("\n Enter the id: "))
  found_id = 0
  for d in shopping:
    if d["id"]==p_id:
      found_id+=1
      print("\nId\tName\tAvailable\tprice")
      print("*****")
      print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["price"]}')
      order=f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["price"]}'
      confirm = input("\nDo you want to place an order on the above shown product (Y/N): ")            
      if confirm=='Y' or confirm=='y':
        print("\nSuccessfully placed the order on the product {} {}".format(d["id"],d["Name"]))
        order_number+=1
        print("Your order number is : ",order_number)
        d["Available"]-=1
        break               
      elif confirm=='N' or confirm=='n':
        print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
        break
      else:
        print("\nYou have entered wrong option. Please enter again.\n")
        placeorder()

  if found_id==0:
    print("\nYou have entered invalid id. Please enter valid id.\n")
    placeorder()

  print("\nAvailable products: \n")    
  shoppingtable()       

#Cancel Order    
def cancelorder():   
  found = False
  temp=[]
  order_id=input("Enter the order id: ")
  for d in shopping:
    found = d["id"]==order_id
    if found!=True:
      temp.append(d)
  if len(temp)==d:
    print(f'{order_id} is not found.')
  else:
    print(f'{order_id} is removed from the placed order.')

#Login Menu
def loginMenu():
  print("============================ ")
  print("       LOGIN MAIN MENU")
  print("============================")
  print(" 1. Admin.")
  print(" 2. Manager.")
  print(" 3. User.")
  print(" 4. Exit.")
  print("****")
  choice = int(input("ENTER Login CHOICE: "))
  return choice

#Admin Menu
def adminMenu():
  print("============================")
  print("         ADMIN MENU")
  print("============================")
  print(" 1. Add or Remove Manager")
  print(" 2. Add pricelist")
  print(" 3. View booking")
  print(" 4. View feedbacks")
  print(" 5. Exit")
  print("****") 
  menu1 = int(input("Enter Admin Choice:"))
  return menu1

#Manager Menu
def managerMenu():
  print("============================")
  print("      MANAGER MENU")
  print("============================")
  print(" 1. View, Confirm or Cancel Request")
  print(" 2. Shopping Management")  
  print(" 3. Booking History")
  print(" 4. Exit")
  print("****")     
  menu2 = int(input("Enter Manager choice: "))
  return menu2
#User Menu
def userMenu():
  print("============================")
  print("      USER MENU")
  print("============================")
  print(" 1. Book Turf")
  print(" 2. Check Turf & Availability")
  print(" 3. Shopping")
  print(" 4. Booking History")
  print(" 5. Feedback")
  print(" 6. Exit")
  print("****")     
  menu3 = int(input("Enter User Choice: "))
  return menu3
################################################################################
# MAIN CODE
################################################################################
n = True          
while n==True:
  print(" WELCOME TO SPORTS HUB TURF ")
  print("============================ ")
  print("         HOME")  
  print("============================ ")
  print(" 1. Register.")       
  print(" 2. Login.") 
  print(" 3. Exit.")
  print("****")
  home = int(input("ENTER YOUR HOME CHOICE: "))
  if home==1: #Register
    register()
  elif home==2: #Login
    choice = loginMenu()

    while(choice!=4):
      if choice==1:           #Admin Login
        adm=input("Enter Admin Username: ")
        pwd=input("Enter Admin Password: ")
        if adm=='admin' and pwd=='admin@abc':
          print("ADMIN CONNECTED!")
          menu1 = adminMenu()
          while(menu1!=5):
            if menu1==1:       #Add/Remove Manager
              print("1.Add Manager","\n 2.Remove Manager")
              ar = int(input("Enter Your Choice"))
              if ar==2:
                removemanager()
              else:                
                addmanager()
              menu1 = adminMenu()

            elif menu1==2:     #Add Pricelist
              print("Individual player---------------Rs 200.00")
              print("Football 5s (team)--------------Rs 1000.00")
              print("Football 7s(team)---------------Rs 1400.00")
              print("Football 11s(team)--------------Rs 2200.00")
              print("Rugby 7s(team)------------------Rs 1400.00")
              print("Rugby 15s(team)-----------------Rs 3000.00")
              print("Badminton singles---------------Rs 200.00")
              print("Badminton doubles(team)---------Rs 400.00")
              print("Badminton mixed(team)-----------Rs 400.00")
              print("/nDo you want to Add ?")
              print("1.Yes","\n2.No")
              yn= int(input("Enter Your Choice: "))
              if yn==1:
                  g=input("Enter Name of the game :")
                  p=input("Enter price in Rs: ")
                  print("\n",g,"---------------",p)
              else:
                  print("price list not added")
                  
              menu1 = adminMenu()

            elif menu1==3:       #View Booking 
              print("Booking History")
              print("MONTH:March")
              print("15.03.22","\nAswathyBadminton singles_6.00am-7.00am","\nAfsal_Football 5s3.00pm-4.00pm")
              print("16.03.22","\nAswathyBadminton doubles_6.00am-7.00am", "\nUma_Badminton doubles_6.00am-7.00am", "\nAfsal_Football 7s7.00pm-8.00pm")
              print("17.03.22","\nAswathyBadminton mixed_7.00am-8.00am", "\nUma_Badminton singles_6.00am-7.00am", "\nAfsal_Rugby 7s_7.00pm-8.00pm","\nAswathy_Badminted doubles6.00pm-7.00pm")
              menu1 = adminMenu()
              
            elif menu1==4:      #View Feedback
              print("Feedback: ")
              print(*f,sep="\n")
              menu1 = adminMenu()
              
            else:
              print("INVALID CHOICE for admin menu")
              menu1 = adminMenu()
          print("End of Main Code through Admin.")
          # menu1 = 5
          choice = 4          
        else:
          print('Incorrect admin username or password. Retry Login!')
          choice = loginMenu()
          
      elif choice==2:   #Manager Login
        m = input("Enter manager username: ")
        pwd1 = input("Enter manager password: ")
        if m in managerkey and pwd1 == managervalue[managerkey.index(m)]:
          print("LOGIN SUCCESSFUL!")
          menu2 = managerMenu()          
          while(menu2!=4):
            if menu2==1:  #View/Confirm/Cancel  Request
              print("1. User:Aswathy","\nSport: Badminton mixed","\nNo. of players:2","\nTime:6.00am-7.00am","\nLocation:Ayyanthole") 
              print("2. User:Uma","\nSport: Rugby 7s","\nNo. of players:7","\nTime:4.00pm-5.00pm","\nLocation:Ayyanthole") 
              print("3. User:Afsal","\nSport: Football 11s","\nNo. of players:1","\nTime:6.00pm-7.00pm","\nLocation:Thiroor") 
              u=int(input("Enter Your Request No.: "))
              if (u==1) or (u==2) or (u==3) or (u==4):
                print("1. Confirm","\n2. Cancel")
                e = int(input("Enter Your Choice: "))   
                if e==1:
                  print("Request Confirmed.")
                else:
                  print("Request Cancelled.")   
              else:
                print("Invalid Request No.")
              menu2 = managerMenu()

            elif menu2==2:  #Shopping Management
              while(b!=5):
                print("1. Display Menu")
                print("2. Add products")
                print("3. Remove products")
                print("4. Product good available")
                print("5. Exit")
                b = int(input("Enter Your Choice"))
                if b==1:
                  shoppingtable()  
                elif b==2:
                  addproducts()
                elif b==3:
                  removeitem()
                elif b==4:
                  availableproducts()
                else:
                  print("Invalid Choice of Shopping Management.")
                menu2 = managerMenu()

            elif menu2==3:  #Booking History
              print("Booking History")
              print("MONTH:March")
              print("15.03.22","\nAswathyBadminton singles_6.00am-7.00am","\nAfsal_Football 5s3.00pm-4.00pm")
              print("16.03.22","\nAswathyBadminton doubles_6.00am-7.00am", "\nUma_Badminton doubles_6.00am-7.00am", "\nAfsal_Football 7s7.00pm-8.00pm")
              print("17.03.22","\nAswathyBadminton mixed_7.00am-8.00am", "\nUma_Badminton singles_6.00am-7.00am", "\nAfsal_Rugby 7s_7.00pm-8.00pm","\nAswathy_Badminted doubles6.00pm-7.00pm")
              menu2 = managerMenu() 
            else:
              print("INVALID CHOICE")
              menu2 = managerMenu()
          print("End of Main Code through Manager.")
          # menu2 = 4
          choice = 4     
        else:
          print("Incorrect Manager Username or Password. Retry Login!")
          choice = loginMenu()

      elif choice==3:   #User Login
        u = input("Enter your username: ")    
        pwd2 = input("Enter the password: ")
        if u in userkey and pwd2 == uservalue[userkey.index(u)]:
          print("Login Successful!")
          menu3 = userMenu()
          while(menu3!=6):  
            if menu3==1:     #Book Turf
              print("Individual player---------------Rs 200.00")
              print("Football 5s (team)--------------Rs 1000.00")
              print("Football 7s(team)---------------Rs 1400.00")
              print("Football 11s(team)--------------Rs 2200.00")
              print("Rugby 7s(team)------------------Rs 1400.00")
              print("Rugby 15s(team)-----------------Rs 3000.00")
              print("Badminton singles---------------Rs 200.00")
              print("Badminton doubles(team)---------Rs 400.00")
              print("Badminton mixed(team)-----------Rs 400.00") 
              game = input("Enter Name of the sport: ")
              p = int(input("No of players: "))
              inputDate = input("Date(dd/mm/yy): ")
              day, month, year = inputDate.split('/')
              isValidDate = True
              try:
                 datetime.datetime(int(year), int(month), int(day))
              except ValueError:
                 isValidDate = False                 
              if(isValidDate):
                 print("Select Time:")
                 print("1. 6.00am-7.00am","\n2. 7.00am-8.00am","\n3. 8.00am-9.00am","\n4. 9.00am-10.00am" ,"\n5. 11.00am-12.00pm" ,"\n6. 3.00pm-4.00pm" ,"\n7. 4.00pm-5.00pm", "\n8. 5.00pm-6.00pm", "\n9. 6.00pm-7.00pm", "\n10. 7.00pm-8.00pm")
                 ti = int(input("Select Your Time: "))
                 print("Locations:-","\n1. Ayyanthole","\n2. Thiroor")
                 lo = int(input("Enter Location Choice: "))
                 print("Total amount= ",p*200)
                 print("Do You Want to Book?")
                 print("1.Yes","\n2.No")
                 s = int(input("Enter Your Choice: "))
                 if s==1:
                   print("Pay",p*200)
                   print("1.Yes","\n2.No")
                   s=int(input("Enter Your Choice :"))
                   if s==1:
                       print("Payment Successful")                               
                       print("Booking Successful!")
                       print("Thank You!")
                       print("You won a scratch card!")
                       print("/n")
                       
                       l=["Better luck next time!","Rs.5","Rs10","Better luck next time!"]
                       print("✓",random.choice(l))
                   else:
                       print("Payment Cancelled")        
                 else:
                   print("Booking Cancelled.")
              else:
                 print("Input date is not valid..")
              menu3 = userMenu() 
              
            elif menu3==2:  #Check Turf & Availability
              print("1. Ayyanthole")
              print("2. Thiroor")
              today = date.today()
              print("Date : ",today)
              t = int(input("Enter Your Choice"))
              if t==1:
                print("1. Badminton single2_6.00am-7.00am")
                print("2. Badminton double4_7.00am-8.00am")
                print("3. Badminton mixed2_6.00am-7.00am")
              else:
                print("1. Badminton single1_7.00am-8.00am")
                print("2. Badminton double2_6.00am-7.00am")
                print("3. Badminton mixed4_6.00pm-7.00pm")
                print("4. Football 11s10_6.00pm-7.00pm")
              menu3 = userMenu() 
                  
            elif menu3==3 :   #Shopping
              print("DISCLAIMER : OFFLINE PAYMENT ONLY")
              while(b!=4):
                print("1. Display Menu")
                print("2. Place order")
                print("3. Cancel order")
                print("4. Exit")
                b = int(input("Enter Your Choice: "))
                if b==1:
                  shoppingtable()  
                elif b==2:
                  placeorder()
                elif b==3:
                  cancelorder()
                elif b==4:
                  print("Thank You. End of Shopping Menu.")
                else:
                  print("Invalid Choice for Shopping Menu!")
              menu3 = userMenu() 
              
            elif menu3==4:  #Booking History 
              if u==userkey[0]:
                print("15.03.22","\nFootball 5s3.00pm-4.00pm", "16.03.22","\nFootball 7s_7.00pm-8.00pm", "17.03.22","\nRugby 7s7.00pm-8.00pm")
              elif u==userkey[1]:
                print("16.03.22","\nBadminton doubles6.00am-7.00am", "17.03.22","\nBadminton singles6.00am-4.00am")
              elif u==userkey[2]:
                print("15.03.22","\nBadminton singles6.00am-7.00am", "16.03.22","\nBadminton doubles_6.00am-7.00am", "17.03.22","\nBadminton mixed_7.00am-8.00am","17.03.22","\nBadminton doubles6.00pm-7.00pm",  )
              else:
                print("NIL")
              menu3 = userMenu() 

            elif menu3==5:  #Feedback
              print(" Feedbacks :-")
              print(*f,sep="\n")
              print("\n")
              fd = input("Enter Your Feedbacks:-\n")
              f.append(fd)
              menu3 = userMenu() 
            else:
              print("INVALID CHOICE!")
              menu3 = userMenu()
              print("End of Main Code through User.")
          # menu3 = 6
          choice = 4              
        else:
          print("Incorrect User Username or Password. Retry Login!")
          choice = loginMenu()
      else:
          print("INVALID CHOICE for LOGIN! Retry!")
          choice = loginMenu()
          print("End of Main Code through Login.")
    # choice = 4

  else: # home=3 EXIT
    print("End of Main Code through Home.")
    print("THANKYOU! 🙏")
    n = False
################################################################################
#END OF MAIN CODE
################################################################################