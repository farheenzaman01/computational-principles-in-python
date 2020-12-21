# creating user defined data type to store per Student information for the class
class SchoolDay:
  def __init__(self, p,a,r):
        self.present=p
        self.absent=a
        self.released=r


#function to make attendance alert
def attendanceAlert(s_days): 
    count_days=0
    #s_days is a list of each students
    for day in s_days:
        #if present/(total)<0.8, increment the count
        # day is a user defined datatype so we can use '.' operator to get its attribute
        if (day.present/(day.absent+day.present+day.released)) < 0.8:
            count_days=count_days+1
    print("Min. Attendace Rule is 0.8\n attendance rule has been broken "+str(count_days)+" number of times\n")


#function to calculate average enrollment  
def avgEnroll(s_days): 
    total=0
    count=0
    #s_days is a list of each student so we can iterate on it
    for day in s_days:#total students are summed for each day object then average is calculated.
        total+=day.absent+day.present+day.released 
        count+=1
    print("Average enrollment "+str(total/count)+"\n")


#function to calculate release days average and count of release days  
def releaseDays(s_days): 
    total=0
    count=0
    
    for day in s_days: #count only when release >0 for the current day object
        if day.released>0:
            total+=day.released
            count+=1
    print("Average released "+str(total/count)+" in "+str(count)+" days\n")


#read files form given txt file
file=open('attendance.txt','r')

#list containing each line
lines = file.readlines();
s_days=[] #empty list to add SchoolDay objects.

#for each line element in lines list
for line in lines:
    # line is read as "125 5 9\n"
    line=line.strip("\n") #removes \n
    par=line.split(' ') #splits string into list for present, absent, released
    sd=SchoolDay(int(par[0]),int(par[1]),int(par[2])) # storing in sd object
    s_days.append(sd) #object sd saved to list s_days
  
while(True): #menu for calling functions in a while loop
    print("Please choose from below for todays attendance Analysis")
     #menu options written in a shorter print format below
    choice=int(input("1-Attendance Alert Days\n2-Average. Enrollment\n3-Release Days\n0-Exit\n?"))
   
    if choice==1:
        attendanceAlert(s_days)
    elif choice==2:
        avgEnroll(s_days)
    elif choice==3:
        releaseDays(s_days)
    elif choice==0:
        print("Good bye,See you tomorrow")
        break # i just added this to my git