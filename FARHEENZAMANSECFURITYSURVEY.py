#DISPLAY OPTIONS FOR THE SURVEY
def survey ():
    print("welcome to China Border Protection")
    print("===SATISFACTION SERVEY==-")
    
    print("PLEASE ENTER A CHOICE FOR THE SURVEY")
    print("1-SUBMIT RATING")
    print("2-VIEW RATING")
    print("3-RESET RATING")
    print("0-EXIT")
    #DECLARING VARIABLE FOR THE USER OPTIONBS
    option = input()
   
    if option == "1":
        #COLLECTING INPUT FROM THE USER
      print(input("Enter a rating from 1-4"))
      survey()
      
    elif option == "2":
        #displaying the input from the user
     print(input)
     print("your recorded rating is below")
     survey() #this loops the prgomme to its beginning options
    
    elif option == "3":
        #indicating the input has been reset
        print("Your rattings has been reset")
        survey()
        
        
    elif option =="0":
        #exiting the progam
        print("Thank you for your time, Goodbye")
        survey()
        
   
    
     
    #looping to the orginal options
survey()
    

        
 

        
     
    
        
 
       
    
       
              
    
    
    

  
        

 