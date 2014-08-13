def main():
    # Choosing username
    username = str(raw_input("Enter your name :\n"))
    # Choosing user designation
    userdesignation =int(raw_input(" 1. Mr\n 2. Mrs \n 3. Ms\n"))
   
    # Choosing designation

    if userdesignation == 1:
        print "Welcome to Shopla Mr.",username  
    elif userdesignation == 2:
        print "Welcome to Shopla Mrs.",username  
    elif userdesignation == 3:
        print "Welcome to Shopla Ms.",username
    else:
        print "Wrong Choice, Please try again"
    print "Enter the following options, as per as your requirements \n"
    userchoice = int(raw_input(" 1. To Shop \n 2. To not Shop"))
    if userchoice == 1:
      print "You selected to Shop , Shop well Spend well"
      usersection = int(raw_input(" 1. Kid Section \n 2. Men Section \n 3. Women Section"))
      if usersection == 1:
	print "Welcome to Kid Section\n"
	kidsection()  # kid section 
      elif usersection == 2:
	print "Welcome to Men Section\n"    # Under Construction
	mensection()  # men section
      elif usersection == 3:
        print "Welcome to Kid Section\n"    # Under Construction
       	womensection() # women section
      else:
        print "Wrong choice"
    else:
      print "You opted not to shop "
	
	

def kidsection():
  print "Welcome to Kid Section\n"
  kidchoice = int(raw_input(" 1. Shirts \n 2. Pants \n"))
  if kidchoice == 1:   # Under Construction
    kidshirts()
  elif kidchoice == 2:  # Under Construction
    kidpants()

def kidshirts():
  kidshirtcost = 250
  kidshirttax = 0.5
  print "Cost of one shirt is %d " %kidshirtcost
  kidshirtsize = int(raw_input("Enter the Kid shirt size \n 1. Small (S) 2. Medium (M) 3. Large (L) 4. Extra Large (XL) \n"))
  kidshirtquantity = int(raw_input("Enter the number of shirts that you would like to purchase : "))
  kidshirttotal = kidshirtcost * kidshirtquantity
  print "Total cost of shirts, excluding tax is %d " %kidshirttotal
  kidshirttaxamount = float(kidshirttax * kidshirttotal)
  kidshirttotalcost = float(kidshirttaxamount + kidshirttotal)
  print "Total cost = Basic Cost + Tax = %d " %kidshirttotalcost
  print "Thanks for shoping" 

if __name__ == "__main__":
    main()


