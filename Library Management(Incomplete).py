# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:07:43 2018
@author: G Sriram
"""
import os
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
    The function also writes into a text file the details of the student. 
    Arguments: None
    Return: s of type Student containing all information about a student. 
    '''
    regno=str(input("Enter the registration number of the student: "))
    name=str(input("Enter the name of the student(Without spaces. Use . for multiple words):")) 
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
    The function also writes into a text file the details of the book
    Arguments: None
    Return: b of type Books containing all the information about a book.
    '''
    isbn=str(input("Enter the ISBN of the book: "))
    name=str(input("Enter the Name of the book(Without spaces. Use _ for multiple words): "))
    author=str(input("Enter the Author of the book(Without spaces. Use . for multiple words): "))
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
    The function also writes into a text file the details of the Faculty
    Arguments: None
    Return: f of type faculty containing all the information about a Faculty.
    '''
    name=str(input("Enter the name of the Faculty(Without spaces. Use . for multiple words): "))
    e_no=str(input("Enter the Employee ID of the Faculty: "))
    dept=str(input("Enter the Department of the Faculty: "))

    f=faculty(name,e_no,dept)
    return f

def writeStudent(s):
    '''
    Function which writes into a text file the details of student each time the function is called.
    Arguments: s of type Student.
    Return: None.
    '''
    fw=open('studlist.txt','a')
    writelist=str(s.getname()+'$$'+s.get_rno()+'$$'+s.get_email()+'$$'+s.get_num()+'\n')
    fw.write(writelist)
    fw.close()

def writeBook(b):
    '''
    Function which writes into a text file the details of Book each time the function is called.
    Arguments: b of type Book.
    Return: None.
    '''
    fw=open('booklist.txt','a')
    writelist=str(b.getisbn()+'$$'+b.getname()+'$$'+b.getauthor()+'$$'+b.getstock()+'$$'+b.getdept()+'\n')
    fw.write(writelist)
    fw.close()
def writeFaculty(f):
    '''
    Function which writes into a text file the details of Faculty each time the function is called.
    Arguments: f of type Faculty.
    Return: None.
    '''
    fw=open('facultylist.txt','a')
    writelist=str(f.getname()+'$$'+f.get_eno()+'$$'+f.get_dept()+'\n')
    fw.write(writelist)
    fw.close()
def readStudent():
    '''
    Function to read the student list from text file and return a list of students details.
    Arguments: None. 
    Return: List with elements of type Student
    '''
    fr=open('studlist.txt','r')
    a=[]
    for line in fr:
        x=line.split('$$')
        a.append(Students(x[0],x[1],x[2],x[3]))
    fr.close()
    return a
def readBooks():
    '''
    Function to read the books list from text file and return a list of books details.
    Arguments: None. 
    Return: List with elements of type Books
    '''
    fr=open('bookslist.txt','r')
    a=[]
    for line in fr:
        x=line.split('$$')
        a.append(Books(x[0],x[1],x[2],x[3],x[4]))
    fr.close()
    return a
def readFaculty():
    '''
    Function to read the faculty list from text file and return a list of faculty details.
    Arguments: None. 
    Return: List with elements of type Faculty
    '''
    fr=open('facultylist.txt','r')
    a=[]
    for line in fr:
        x=line.split('$$')
        a.append(faculty(x[0],x[1],x[2]))
    fr.close()
    return a
def searchStudents(reg_no):
    '''
    Function to search for student in the file and return the details of the student.
    Arguments: reg_no of type string.
    Return: s of type Student.
    '''
    studlist=readStudent()
    for i in studlist:
        if(i.get_rno()==reg_no):
            return i
    print("Student not found!")
    
def searchBooks(isbn):
    '''
    Function to search for book in the file and return the details of the book.
    Arguments: isbn of type string.
    Return: b of type Books.
    '''
    booklist=readBooks()
    for i in booklist:
        if(i.getisbn()==isbn):
            return i
    print("Book not found!")  
    
def searchFaculty(eno):
    '''
    Function to search for faculty in the file and return the details of the faculty.
    Arguments: eno of type string.
    Return: f of type faculty.
    '''
    flist=readFaculty()
    for i in flist:
        if(i.get_eno()==eno):
            return i
    print("Faculty not found!") 

def modifyStudent(reg_no):
    '''
    Function to Modify list of students, given the registration number.
    Arguments: reg_no of type string.
    Return: None
    '''
    studlist=readStudent()
    fw=open('studlist1.txt','a')
    for i in studlist:
        if(i.get_rno()==reg_no):
            s=addStudent()
            writelist=str(s.getname()+'$$'+s.get_rno()+'$$'+s.get_email()+'$$'+s.get_num()+'\n')
            fw.write(writelist)
        else:
            writelist=str(i.getname()+'$$'+i.get_rno()+'$$'+i.get_email()+'$$'+i.get_num())
            fw.write(writelist)           
    fw.close()
    os.remove('studlist.txt')
    os.rename('studlist1.txt','studlist.txt')
    
def modifyBook(isbn):
    '''
    Function to Modify list of Book, given the ISBN.
    Arguments: isbn of type string.
    Return: None
    '''
    booklist=readBooks()
    fw=open('booklist1.txt','a')
    for i in booklist:
        if(i.getisbn()==isbn):
            b=addBook()
            writelist=str(b.getisbn()+'$$'+b.getname()+'$$'+b.getauthor()+'$$'+b.getstock()+'$$'+b.getdept()+'\n')
            fw.write(writelist)
        else:
            writelist=str(i.getisbn()+'$$'+i.getname()+'$$'+i.getauthor()+'$$'+i.getstock()+'$$'+i.getdept())
            fw.write(writelist)           
    fw.close()
    os.remove('booklist.txt')
    os.rename('booklist1.txt','booklist.txt')
def modifyFaculty(e_no):
    '''
    Function to Modify list of faculty, given the Employee.
    Arguments: e_no of type string.
    Return: None
    '''
    flist=readFaculty()
    fw=open('facultylist1.txt','a')
    for i in flist:
        if(i.get_eno()==e_no):
            f=addFaculty()
            writelist=str(f.getname()+'$$'+f.get_eno()+'$$'+f.get_dept()+'\n')
            fw.write(writelist)
        else:
            writelist=str(i.getname()+'$$'+i.get_eno()+'$$'+i.get_dept())
            fw.write(writelist)    
    fw.close()
    os.remove('facultylist.txt')
    os.rename('facultylist1.txt','facultylist.txt') 
def deleteStudent(reg_no):
    '''
    Function to delete a student, given the registration number.
    Arguments: reg_no of type string.
    Return: None
    '''
    studlist=readStudent()
    fw=open('studlist1.txt','a')
    for i in studlist:
        if(i.get_rno()==reg_no):
            continue
        else:
            writelist=str(i.getname()+'$$'+i.get_rno()+'$$'+i.get_email()+'$$'+i.get_num())
            fw.write(writelist)           
    fw.close()
    os.remove('studlist.txt')
    os.rename('studlist1.txt','studlist.txt')

def deleteBook(isbn):
    '''
    Function to delete a book, given the ISBN.
    Arguments: isbn of type string.
    Return: None
    '''
    booklist=readBooks()
    fw=open('booklist1.txt','a')
    for i in booklist:
        if(i.getisbn()==isbn):
            continue
        else:
            writelist=str(i.getisbn()+'$$'+i.getname()+'$$'+i.getauthor()+'$$'+i.getstock()+'$$'+i.getdept())
            fw.write(writelist)           
    fw.close()
    os.remove('booklist.txt')
    os.rename('booklist1.txt','booklist.txt')

def deleteFaculty(e_no):
    '''
    Function to delete a faculty, given the employee number.
    Arguments: e_no of type string.
    Return: None
    '''
    flist=readFaculty()
    fw=open('facultylist1.txt','a')
    for i in flist:
        if(i.get_eno()==e_no):
            continue
        else:
            writelist=str(i.getname()+'$$'+i.get_eno()+'$$'+i.get_dept())
            fw.write(writelist)    
    fw.close()
    os.remove('facultylist.txt')
    os.rename('facultylist1.txt','facultylist.txt') 
