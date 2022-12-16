import datetime
import time
import re
total_amount = 0
amount_1 = 0
amount_2 = 0
amount_3 = 0

print ("😍 WELCOME TO CAFE COFFEE DAY 😍")


def isValid(a):
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return Pattern.match(a)


a = input("Enter Your mobile number:")
print ("***********************************")
if(isValid(a)):
    print ("Thanks for Choosing Cafe Coffee Day ☕☕")

    print ("***********************************")

    while(1):
    

                print ("Cafe Coffee Day Special Deals")
                print ("***********************************")

                print (" 🛒 Our Products ☕")
                print ("*******************")
                print ("☕ COFFEE & 🍵 TEA")
                print ("📻 COFFEE MAKER")
                print ("🍺 MUGS & 🎁 GIFTS")

                print ("***********************************")


                print ("Enter 1 for COFFEE")                
                print ("Enter 2 for TEA")                
                print ("Enter 3 for COFFEE MAKER")                
                print ("Enter 4 for MUGS")                
                print ("Enter 5 for GIFTS")
                a = int(input("Enter your choice :")) 

                print ("***********************************") 

                
                if(a == 1):
                    print ("COFFEE")
                    print ("Enter 1 for Small")
                    print ("Enter 2 for Medium")
                    print ("Enter 3 for Large")
                    print ("Enter 4 for exit")
                    a = int(input("Enter your choice :"))


                    print ("***********************************")  



                    if(a == 1):
                        b = int(input("How many coffee :"))
                        a = 10
                        amount_1 = a * b
                        print ("yes - continue\nno - exit")
                        x = input("do you want one more coffee :")
                            
                        if(x == "yes"):
                            continue
                        elif(x == "no"):
                            total_amount=amount_1+amount_2+amount_3
                            print ("your total amount is:")
                            print (total_amount)
                            print ( "Thank you for visiting \nYour Order will be Placed Soon..🤗")
                            break
                            
                            
                
                        #*****************************************#

                    elif(a == 2):
                        b = int(input("How many coffee :"))
                        a = 20
                        amount_2 = a * b
                        print ("yes - continue\nno - exit")
                        x = input("do you want one more coffee :")
                            
                        if(x == "yes"):
                            continue
                        elif(x == "no"):
                            total_amount=amount_1+amount_2+amount_3
                            print ("your total amount is:")
                            print (total_amount)
                            print ("Thank you for visiting \nYour Order will be Placed Soon..🤗")
                            break


                                            
                        #*****************************************#

                    elif(a == 3):
                        b = int(input("How many coffee :"))
                        a = 30
                        amount_3 = a * b
                        print ("yes - continue\nno - exit")
                        x = input("do you want one more coffee :")
                            
                        if(x == "yes"):
                            continue
                        elif(x == "no"):
                            total_amount=amount_1+amount_2+amount_3
                            print ("your total amount is:")
                            print (total_amount)
                            print ("Thank you for visiting \nYour Order will be Placed Soon..🤗")
                            break
                            
                            
                        #*****************************************#

                    else:
                        (a == 4)
                        print ("Thank you, visit again")

# *********************************************************************************

                elif(a == 2):
                    print ("TEA")
                    print ("Enter 1 for Small")
                    print ("Enter 2 for Medium")
                    print ("Enter 3 for Large")
                    print ("Enter 4 for exit")
                    a = int(input("Enter your choice :"))


                    print ("***********************************")  



                    if(a == 1):
                        b = int(input("How many Tea :"))
                        a = 10
                        amount_1 = a * b
                        print ("yes - continue\nno - exit")
                        x = input("do you want one more Tea :")
                    
                        if(x == "yes"):
                            continue
                        elif(x == "no"):
                            total_amount=amount_1+amount_2+amount_3
                            print ("your total amount is:")
                            print (total_amount)
                            print ( "Thank you for visiting \nYour Order will be Placed Soon..🤗")
                            break
                    
                    
         
                #*****************************************#

                    elif(a == 2):
                        b = int(input("How many Tea :"))
                        a = 20
                        amount_2 = a * b
                        print ("yes - continue\nno - exit")
                        x = input("do you want one more Tea :")
                    
                        if(x == "yes"):
                            continue
                        elif(x == "no"):
                            total_amount=amount_1+amount_2+amount_3
                            print ("your total amount is:")
                            print (total_amount)
                            print ("Thank you for visiting \nYour Order will be Placed Soon..🤗")
                            break


                                       
                 #*****************************************#

                    elif(a == 3):
                        b = int(input("How many Tea :"))
                        a = 30
                        amount_3 = a * b
                        print ("yes - continue\nno - exit")
                        x = input("do you want one more Tea :")
                    
                        if(x == "yes"):
                            continue
                        elif(x == "no"):
                            total_amount=amount_1+amount_2+amount_3
                            print ("your total amount is:")
                            print (total_amount)
                            print ("Thank you for visiting \nYour Order will be Placed Soon..🤗")
                            break
                    
                    
                 #*****************************************#

                    else:
                        (a == 4)
                        print ("Thank you, visit again")

# **********************************************************************************
                elif(a == 3):
                    print ("COFFEE MAKER MACHINE")
                    print ("Enter 1 for Small Size")
                    print ("Enter 2 for Large Size")
                    print ("Enter 3 for exit")
                    a = int(input("Enter your choice :"))


                    print ("***********************************")  



                    if(a == 1):
                        b = int(input("How many Small Size Coffee Maker Machine you want to Buy :"))
                        a = 250
                        amount_1 = a * b
                        print ("yes - continue\nno - exit")
                        x = input("Do you want one more Coffee Maker Machine :")
                    
                        if(x == "yes"):
                            continue
                        elif(x == "no"):
                            total_amount=amount_1+amount_2+amount_3
                            print ("your total amount is:")
                            print (total_amount)
                            print ( "Thank you for visiting \nYour Order will be Placed Soon..🤗")
                            break
                    
                    
         
                #*****************************************#

                    elif(a == 2):
                        b = int(input("How many Large Size Coffee Maker Machine you want to Buy :"))
                        a = 510
                        amount_2 = a * b
                        print ("yes - continue\nno - exit")
                        x = input("Do you want one more Coffee Maker Machine :")
                    
                        if(x == "yes"):
                            continue
                        elif(x == "no"):
                            total_amount=amount_1+amount_2+amount_3
                            print ("your total amount is:")
                            print (total_amount)
                            print ("Thank you for visiting \nYour Order will be Placed Soon..🤗")
                            break


                                       
                 #*****************************************#


                    else:
                        (a == 3)
                        print ("Thank you, visit again")


# **********************************************************************************

                elif(a == 4):
                    print ("MUGS")
                    print ("Enter 1 for Small Mugs")
                    print ("Enter 2 for Medium Mugs")
                    print ("Enter 3 for Large Mugs")
                    print ("Enter 4 for exit")
                    a = int(input("Enter your choice :"))


                    print ("***********************************")  



                    if(a == 1):
                        b = int(input("How many Small Mugs you want to Buy :"))
                        a = 150
                        amount_1 = a * b
                        print ("yes - continue\nno - exit")
                        x = input("Do you want one more Mug :")
                    
                        if(x == "yes"):
                            continue
                        elif(x == "no"):
                            total_amount=amount_1+amount_2+amount_3
                            print ("your total amount is:")
                            print (total_amount)
                            print ( "Thank you for visiting \nYour Order will be Placed Soon..🤗")
                            break

# *********************************************************************************
                    if(a == 2):
                        b = int(input("How many Medium Size Mugs you want to Buy :"))
                        a = 300
                        amount_1 = a * b
                        print ("yes - continue\nno - exit")
                        x = input("Do you want one more Mug :")
                    
                        if(x == "yes"):
                            continue
                        elif(x == "no"):
                            total_amount=amount_1+amount_2+amount_3
                            print ("your total amount is:")
                            print (total_amount)
                            print ( "Thank you for visiting \nYour Order will be Placed Soon..🤗")
                            break
                    
                    
         
                #*****************************************#

                    elif(a == 3):
                        b = int(input("How many Large Size Mugs you want to Buy :"))
                        a = 450
                        amount_2 = a * b
                        print ("yes - continue\nno - exit")
                        x = input("Do you want one more Mug :")
                        
                        if(x == "yes"):
                            continue
                        elif(x == "no"):
                            total_amount=amount_1+amount_2+amount_3
                            print ("your total amount is:")
                            print (total_amount)
                            print ("Thank you for visiting \nYour Order will be Placed Soon..🤗")
                            break


                                       
                 #*****************************************#


                    else:
                        (a == 4)
                        print ("Thank you, visit again")



        # ***************************************************************************************

                elif(a == 5):
                    print(" 🎁 Gifts are coming soon in cafe coffee day....🎁")
                    break
                        
           
else:
    print("Undefined, Please Enter 10 Digit Phone Number")



                    
                       
             
            
                    
                   
                          


