class SchoolDay:            
    
    def __init__(self, p,a,r):
        self.present=p
        self.absent=a
        self.released=r


def attendanceAlert(s_days):     #function to make attendance alert
    count_days=0
    for day in s_days:
        if day.present/(day.absent+day.present+day.released)<0.8:       #if present/(total)<0.8, increment the count
            count_days=count_days+1
    print("Min. Attendace Rule is 0.8\n The rule has been brocken "+str(count_days)+" number of times\n")
    
def avgEnroll(s_days):      #function to calculate avg. enrollment
    total=0
    count=0
    for day in s_days:
        total+=day.absent+day.present+day.released      #total students are summed for each day object then avg. is calculated.
        count+=1
    print("Average enrollment "+str(total/count))
    
def releaseDays(s_days):        #function to calculate release days average and count of release days
    total=0
    count=0
    for day in s_days:          #count only when release >0 for the current day object
        if day.released>0:
            total+=day.released
            count+=1
    print("Average released "+str(total/count)+" in "+str(count)+" days")

file=open('attendance.txt','r')        #read files form sample2.txt

lines = file.readlines();           #list containing each line

s_days=[]       #epmty list to add SchoolDay objects.

for line in lines:                  #for each line element in lines list
    line=line.strip("\n")           #removes \n
    par=line.split(' ')             #splits string into par list[present, absent, released]
    sd=SchoolDay(int(par[0]),int(par[1]),int(par[2]))       #saved in sd object
    s_days.append(sd)                   #object sd saved to list s_days
    
while(True):                #menu for calling functions
    print("Attendance Analysis\n============================\n")
    ch=int(input("1-Attendance Alert Days\n2-Avg. Enrollment\n3-Release Days\n0-Exit\n?"))
    if ch==1:
        attendanceAlert(s_days)
    elif ch==2:
        avgEnroll(s_days)
    elif ch==3:
        releaseDays(s_days)
    elif ch==0:
        break