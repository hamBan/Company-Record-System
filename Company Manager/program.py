"""
Created on Sun Jan 13 15:28:23 2019

@author: SOHAM
"""
# Basic Company Record System
import pickle
import re
import os
# Employee Record Class
class employee:
    def __init__(self,empcode,name,salary,email,dept):
        self.empcode = empcode
        self.name = name
        self.salary = salary
        self.email = email
        self.dept = dept
        self.l = [empcode,name,salary,email,dept]
# to add an employee
    def add(self):
        open("C:\\Users\\SOHAM\\Desktop\\Python Programs\\Company Manager\
\\Company Records\\emplist.file","ab+").close()
        with open("C:\\Users\\SOHAM\\Desktop\\Python Programs\\Company Manager\
\\Company Records\\emplist.file","rb+") as f:
            if os.path.getsize("C:\\Users\\SOHAM\\Desktop\\Python Programs\
\\Company Manager\\Company Records\\emplist.file"):
                l = pickle.load(f)
            else:
                l = []
            l.append(self.l)
            print(l)
            f.seek(0)
            pickle.dump(l,f)
# to add an employee
# check employee code
    def codecheck(self):
        if re.fullmatch("E\d\d\d",self.empcode):
            return 1
        else:
            print("Invalid Employee Code")
            return 0
# check employee code
# check email
    def emailcheck(self):
        if re.search("\w+@\w+.[\w\.]+\w+$",self.email):
            return 1
        else:
            print("Invalid Email ID")
            return 0
# check email
# check department
    def deptcheck(self):
        with open("C:\\Users\\SOHAM\\Desktop\\Python Programs\\Company Manager\
\\Company Records\\deptlist.file","rb") as f:
            d = pickle.load(f)
            if self.dept not in d:
                print("Invalid Department")
                return 0
            else:
                return 1
# check department
# check and add
    def checkadd(self):
        if self.codecheck() and self.emailcheck() and self.deptcheck():
            self.add()
            return 1
        else:
            return 0
# check and add
# search department
    def search(self):
        with open("C:\\Users\\SOHAM\\Desktop\\Python Programs\\Company Manager\
\\Company Records\\emplist.file","rb") as f:
            r = pickle.load(f)
            c = 0
            for l in r:
                if self.name in l[1]:
                    print(l[0],l[1],l[2],l[3],l[4])
                    c+=1
            if c==0:
                print("Name not found")
# search department
# show employees
    def show(self):
        with open("C:\\Users\\SOHAM\\Desktop\\Python Programs\\Company Manager\
\\Company Records\\emplist.file","rb") as f:
            r = pickle.load(f)
            for l in r:
                for i in l:
                    print(i,end = " ")
                print()
# show employees
# Department Record Class
class department:
    def __init__(self,depcode,dept):
        self.depcode = depcode
        self.dept = dept
# to add a department    
    def add(self):
        open("C:\\Users\\SOHAM\\Desktop\\Python Programs\\Company Manager\
\\Company Records\\deptlist.file","ab+").close()
        with open("C:\\Users\\SOHAM\\Desktop\\Python Programs\\Company Manager\
\\Company Records\\deptlist.file","rb+") as f:
            if os.path.getsize("C:\\Users\\SOHAM\\Desktop\\Python Programs\
\\Company Manager\\Company Records\\deptlist.file"):
                deptlist = pickle.load(f)
            else:
                deptlist = {}
            depcode = self.depcode
            dept = self.dept
            deptlist.update({dept:depcode})
            f.seek(0)
            pickle.dump(deptlist,f)
# to add a department
# check
    def check(self):
        open("C:\\Users\\SOHAM\\Desktop\\Python Programs\\Company Manager\
\\Company Records\\deptlist.file","ab+").close()
        with open("C:\\Users\\SOHAM\\Desktop\\Python Programs\\Company Manager\
\\Company Records\\deptlist.file","rb+") as f:
            if os.path.getsize("C:\\Users\\SOHAM\\Desktop\\Python Programs\
\\Company Manager\\Company Records\\deptlist.file"):
                deptlist = pickle.load(f)
                for i in deptlist:
                    if self.dept == i or self.depcode == deptlist[i]:
                        print("Department already exists")
                        return 0
        return 1
# check
# check code
    def checkcode(self):
        if re.fullmatch("D\d\d\d",self.depcode):
            return 1
        else:
            print("Invalid Department Code")
            return 0
# check code
# check and add
    def checkadd(self):
        if self.check() and self.checkcode():
            self.add()
            return 1
        else:
            return 0
# check and add
# to search a department
    def search(self):
        with open("C:\\Users\\SOHAM\\Desktop\\Python Programs\\Company Manager\
\\Company Records\\deptlist.file","rb+") as f:
            deptlist = pickle.load(f)
            if self.dept in deptlist:
                print("Department Name = ",self.dept)
                print("ID = ",deptlist[self.dept])
            else:
                print("Department not found")
# to search a department
# show departments
    def show(self):
        with open("C:\\Users\\SOHAM\\Desktop\\Python Programs\\Company Manager\
\\Company Records\\deptlist.file","rb+") as f:
            deptlist = pickle.load(f)
            for i in deptlist:
                print(deptlist[i],i)
# show departments
# Start    
# main menu
while True:
    c1 = int(input("Main Menu:\n1. Employee\n2. Department\n3. Exit\n Enter \
your choice: "))
# employee menu
    if c1==1:
        while True:    
            c2 = int(input("Employee Menu:\n1. Add\n2. Show\n3. Search\n\
4. Back to Main Menu\nEnter your choice: "))
# add
            if c2==1:
                while True:
                    while True: 
                        ecode = input("Enter your \"employee code\": ")
                        name = input("Enter your name: ")
                        salary = int(input("Enter your salary: "))
                        email = input("Enter your email address: ")
                        dept = input("Enter your department: ")
                        yn = input("Submit(Y/N) ? \n")
                        if yn=="Y":
                            break
                    e = employee(ecode,name,salary,email,dept)
                    r = e.checkadd()
                    if r==1:
                        yn = input("Do you want to add more(Y/N) ? \n")
                        if yn == "N":
                            break
# add
# show
            elif c2==2:
                em = employee("","",0,"","")
                em.show()
# show
# search
            elif c2==3:
                while True:
                    name = input("Enter name to be searched: ")
                    ob = employee("",name,0,"","")
                    ob.search()
                    yn = input("Do you want to search more(Y/N) ? ")
                    if yn == "N":
                        break
# search
# back
            else :
                break
# back
# employee menu
# department menu
    elif c1==2:
        while True:
            c2 = int(input("Department Menu:\n1. Add\n2. Show\n3. Search\n\
4. Back to Main Menu\nEnter your choice: "))
# add
            if c2==1:
                while True:
                    while True:
                        depcode = input("Enter the department code: ")
                        dept = input("Enter the department name: ")
                        yn = input("Submit(Y/N) ? \n")
                        if yn=="Y":
                            break
                    d = department(depcode,dept)
                    r = d.checkadd()
                    if r==1:
                        yn = input("Do you want to add more(Y/N) ? \n")
                        if yn == "N":
                            break
# add
# show
            elif c2==2:
                dp = department("","")
                dp.show()
# show
# search
            elif c2==3:
                dept = input("Enter Department Name: ")
                ob = department("",dept)
                ob.search()
# search
# back
            else:
                break
# back
# department menu
# exit
    else:
        break
# exit
# stop