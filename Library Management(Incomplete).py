# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:07:43 2018

@author: G Sriram
"""
class Books(object): 
    def __init__(self, isbn,name,author,stock,dept):
        '''
        Function to initialise the isbn, name, author and stock of any book
        '''
        self.isbn=isbn
        self.name=name
        self.author=author
        self.stock=stock
        self.dept=dept
    def getisbn(self):
        '''
        Function that returns the ISBN of the book
        '''
        return self.isbn
    def getname(self):
        '''
        Function which returns the name of the book
        '''
        return self.name
    def getauthor(self):
        '''
        Function which returns the author of the book
        '''
        return self.author
    def getstock(self):
        '''
        Function which returns the stock
        '''
        return self.stock
    def getdept(self):
        '''
        Function which returns the department which the book is related to.
        '''
        return self.dept

class Students(object):
    def __init__(self,name,reg_no,email,num):
        '''
        Function to assign the student name, registration number, E-Mail ID and Ph.No of the student issuing the book
        '''
        self.name=name
        self.reg_no=reg_no
        self.email=email
        self.num=num
    def getname(self):
        '''
        Returns the name of the student
        '''
        return self.name
    def get_rno(self):
        '''
        Returns the Registration number of the Student
        '''
        return self.reg_no
    def get_email(self):
        '''
        Returns the E-Mail of the student
        '''
        return self.email
    def get_num(self):
        '''
        Returns the Phone number of the student
        '''
        return self.num

class faculty(object):
    def __init__(self,name,e_no,dept):
        '''
        Function to assign the Faculty name, Employee Number and Department of Faculty
        '''
        self.name=name
        self.e_no=e_no
        self.dept=dept
    def getname(self):
        '''
        Returns the name of the Faculty
        '''
        return self.name
    def get_eno(self):
        '''
        Returns the employee number of the faculty
        '''
        return self.e_no
    def get_dept(self):
        '''
        Returns the Department of the Faculty
        '''
        return self.dept
    
def addStudent():
    '''
    A function which prompts a user to enter the details of students and returns an instance containing all info.
    
    Arguments: None
    Return: s of type Student containing all information about a student. 
    '''
    
    name=str(input("Enter the name of the student:"))
    regno=str(input("Enter the registration number of the student: "))
    email=str(input("Enter the E-Mail ID of the student: "))
    while True:    
        number=str(input("Enter Phone Number of student: "))
        if(len(number)==10):
            break
        else:
            print("Please enter a valid Phone Number.")
    s=Students(name,regno,email,number)
    return s

def addBook():
    '''
    Function which prompts the user to enter the details of the book and returns an instance containing all the info.
    
    Arguments: None
    Return: b of type Books containing all the information about a book.
    '''
    isbn=str(input("Enter the ISBN of the book: "))
    name=str(input("Enter the Name of the book: "))
    author=str(input("Enter the Author of the book: "))
    stock=int(input("Enter the number of books available: "))
    while True:
        dept=str(input("Enter the department to which the book is related to(CSE,ECE,ME,IT,Others) :"))
        if(dept in ('CSE','ECE','ME','IT','Others')):
            break
        else:
            print("Please enter a valid department name.")
    b=Books(isbn,name,author,stock,dept)
    return b

def addFaculty():
    '''
    Function which prompts the user to enter the details of faculty and returns an instance containing all the info.
    
    Arguments: None
    Return: f of type faculty containing all the information about a Faculty.
    '''
    name=str(input("Enter the name of the Faculty: "))
    e_no=str(input("Enter the Employee ID of the Faculty: "))
    dept=str(input("Enter the Department of the Faculty: "))
    f=faculty(name,e_no,dept)
    return f
