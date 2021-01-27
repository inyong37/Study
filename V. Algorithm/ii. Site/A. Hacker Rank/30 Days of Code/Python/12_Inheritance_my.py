# Author      : inyong1020@gmail.com
# Date        : 2020-06-17-Wed.
# Description : Hacker Rank; 30 Days of code; Day 12: Inheritance.
# State       : Passed.
# Environment : -
# Input       : -
# Output      : -

"""
Objective
Today, we're delving into Inheritance. Check out the attached tutorial for learning materials and an instructional video!

Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has  parameters:
A string, .
A string, .
An integer, .
An integer array (or vector) of test scores, .
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
Grading.png

Input Format

The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

You are not responsible for reading the following input from stdin:
The first line contains , , and , respectively. The second line contains the number of test scores. The third line of space-separated integers describes .

Constraints

Output Format

This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

Sample Input

Heraldo Memelli 8135627
2
100 80
Sample Output

 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
Explanation

This student had  scores to average:  and . The student's average grade is . An average grade of  corresponds to the letter grade , so our calculate() method should return the character'O'.
"""


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def printgrade(self):
        grade = sum(scores)/len(scores)
        print('Grade: ', end='')
        if 90 <= grade <= 100:
            print('O')
        elif 80 <= grade <= 90:
            print('A')
        elif 70 <= grade <= 80:
            print('A')
        elif 55 <= grade <= 70:
            print('P')
        elif 40 <= grade <= 55:
            print('D')
        else:
            print('T')

# Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here


#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here

# line = input().split()
# firstname = line[0]
# lastname = line[1]
# idnumber = line[2]
[firstname, lastname, idnumber] = input().split()
total = int(input())
scores = list(map(int, input().split()))
stu = Student(firstname, lastname, idnumber, scores)
stu.printPerson()
stu.printgrade()
