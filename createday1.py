from os import system, name
import csv
import sys
import random
import itertools

def main():
    clear() #what is the function I can use to clear the terminal?
    print("==============================================================")
    print("Welcome to History mini assessment")
    studentname= input("Input your full name: ")
    foo=1
    while foo!=0:
        menu()

def menu():
    clear()
    print("Options:")
    print("1. Instructions")
    print("2. Rubrics")
    print("3. Assessment")
    print("4. Exit")
    print("==============================================================")
    index= input("Make your choice:")
    if index==1:
        instructions()
    if index==2:
        rubrics()
    if index==3:
        assessment()
    if index==4:
        exit()
    print("==============================================================")


def instructions():
    clear()
    print("Each question would have only one correct answer among 4.")
    print("The question would be randomly selected from a series of")
    print("numerous questions. The options are also randomized.")
    print("You would be assessed on European history, American history,")
    print("and American history. You will be assessed based on a scale of")
    print("four in each of these standards. Wrong options will not cast")
    print("extra penalties so take your guess at the ones you do not know.")
    print("!VAMOUZ!")
    print("==============================================================")
    temp= "foo"
    while (temp != "y" and temp!= "Y"):
        temp= input("Type y to return to menu:")
    print("==============================================================")
    menu()

def rubric():
    print("There will be three rubric on which you will be assessed:")
    print("American history, European history, Asian history.")
    print("Each rubric would be based on a scale of 4:")
    print("")
    print("1. You have close to no understanding on the geopolitical and")
    print("   historical knowlege on the region.")
    print("")
    print("2. You have a preliminary understanding of the region. Your")
    print("   is very far from the professional level, but is sufficient")
    print("   for basic communications of social events.")
    print("")
    print("3. You know more than the average person about this region.")
    print("   You have clearly been educated on this region's history.")
    print("")
    print("4. You have the ability to handle the history of this region")
    print("   with ease, grace and style. You are equiped with the")
    print("   ability to take college level history courses.")
    print("==============================================================")
        temp= "foo"
    while (temp != "y" and temp!= "Y"):
        temp= input("Type y to return to menu:")
    print("==============================================================")
    menu()

def assessment():

def feedback():

