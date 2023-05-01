"""to maintain student details

roll

name

m1

m2

m3

total

per

"""

"""

modules imported



"""



import pickle

import os



"""

class used

"""



print("\n\t\t\t*** Welcome to Radhika Bal Vidya Mandir ***\n")









class student(object):

    def __int__(s):

        s.roll=0

        s.name=""

        s.m1=0

        s.m2=0

        s.m3=0

        s.total=0

        s.per=0



    def add_rec(s):

        s.roll=int(input("Enter roll no "))

        s.name=input("Enter full name of student: ")

        s.name=s.name.upper()

        s.m1=float(input("Enter marks of first subject: "))

        s.m2=float(input("Enter marks of second subject: "))

        s.m3=float(input("Enter marks of third subject: "))

        s.total=s.m1+s.m2+s.m3

        s.per=(s.total/300)*100

        

    def disp_rec(s):

        print("Roll No. ",s.roll)

        print("Name ",s.name)

        print("First subject marks ",s.m1)

        print("Second subject marks ",s.m2)

        print("Third subject marks ",s.m3)

        print("Total marks ",s.total)

        print("Percentage ",s.per)



    def display_rec(s):

        print("%-10s"%s.roll,"%0s"%s.name,"%10s"%s.m1,"%20s"%s.m2,"%15s"%s.m3,"%16s"%s.total,"%10s"%s.per)

        #print("in display_rec")

        

    def modify_rec(s):

        s.roll=int(input("Enter new roll no : "))

        s.name=input("Enter new name : ")

        s.name=s.name.upper()

        s.m1=float(input("Enter marks of first subject : "))

        s.m2=float(input("Enter marks of second subject : "))

        s.m3=float(input("Enter marks of third subject : "))

        s.total=s.m1+s.m2+s.m3

        s.per=(s.total/300)*100

    





def write_record():

    try:

        rec=student()

        file=open("stud.dat","ab")

        rec.add_rec()

        pickle.dump(rec,file)

        file.close()

        print("Thank you !!!")

        print("Record added in file")

        input("Press any key to continue ....")

    except:

        pass





def display_all():

    os.system("cls")

    print(105*"=")

    print("\n             Student Records\n")

    print(105*"=")

    print("\n");

    print("Roll No.   Name          1st subject marks 2nd subject marks 3rd subject marks     Total       Percentage");

    print(105*"=")

    try:

        file=open("stud.dat","rb")

        while True:

            rec=pickle.load(file)

            rec.display_rec()

            

            

    except EOFError:

        file.close()

        print(105*"=")

        input("Press any key to continue ....")

    except IOError:

        print("Sorry file could not be opened !!!")

        

def search_roll():

    os.system("cls")

    try:

        z=0

        print(40*"=")

        print("Record Searching By Roll No")

        print(40*"=")

        n=int(input("Enter roll no. search : "))

        file=open("stud.dat","rb")

        while True:

            rec=pickle.load(file)

            #print(rec.roll)

            if(rec.roll==n):

                z=1

                print("\nRecord Found and details are :-\n")

                rec.disp_rec()

                break

    except EOFError:

        file.close()

        if(z==0):

            print(" Sorry record is not present !!!")

        

    except IOError:

        print("Sorry file could not be opened !!!")

    input("Press any key to continue ....")

        

def search_name():

    os.system("cls")

    try:

        z=0

        n=input("Enter name to search : ")

        file=open("stud.dat","rb")

        while True:

            rec=pickle.load(file)

            #print(rec.roll)

            if(rec.name==n.upper()):

                z=1

                rec.disp_rec()

                break

    except EOFError:

        file.close()

        if(z==0):

            print("Sorry record is not present !!!")

        

    except IOError:

        print("Sorry file could not be opened")   

    input("Press any key to continue ....")    



def modify_roll():

    os.system("cls")

    z=0

    try:

        n=int(input("Enter roll no to modify : "))

        file=open("stud.dat","rb")

        temp=open("temp.dat","wb")

        while True:

            rec=pickle.load(file)

            if(rec.roll==n):

                z=1

                print("Record found and details are : ")

                rec.disp_rec()

                print("Enter new data : ")

                rec.modify_rec()

                pickle.dump(rec,temp)

                print("Thank you !")

                print("Record updated!")

            else:

                pickle.dump(rec,temp)



    except EOFError:

        file.close()

        temp.close()

        if(z==0):

            print("Sorry! record not found !!!")

    except IOError:

        print("Sorry! file could not be opened !!!")



    os.remove("stud.dat")

    os.rename("temp.dat","stud.dat")

    input("Press any key to continue ....")



def delete_roll():

    os.system("cls")

    z=0

    try:

        n=int(input("Enter roll no to delete: "))

        file=open("stud.dat","rb")

        temp=open("temp.dat","wb")

        while True:

            rec=pickle.load(file)

            if(rec.roll==n):

                z=1

                print("Record to delete found and details are : ")

                rec.disp_rec()

                #pickle.dump(rec,temp)

                #print("Record updated")

            else:

                pickle.dump(rec,temp)



    except EOFError:

        file.close()

        temp.close()

        if(z==0):

            print("Sorry! record not found !!!")

    except IOError:

        print("File could not be opened !!!")



    os.remove("stud.dat")

    os.rename("temp.dat","stud.dat")

    input("Press any key to continue ....")







while True:

    os.system("cls")

    print(40*"=")

    print("""            Main Menu

            --------- 



           1. Add recod

           2. Display all your saved records

           3. Search record by Roll No.

           4. Search record by name

           5. Modify record by rollno

           6. Delete record by rollno

           7. Exit

    """)

    print(50*"=")

    ch=int(input("Enter your choice: "))

    print(50*"=")

    if(ch==1):

        write_record()

    elif(ch==2):

        display_all()

    elif(ch==3):

        search_roll()

    elif(ch==4):

        search_name()

    elif(ch==5):

        modify_roll()

    elif(ch==6):

        delete_roll()

    elif(ch==7):

        print("Thank you !!!")

        break

    else:

        print("Sorry invalid choice !!!")
