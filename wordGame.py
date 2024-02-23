from os import system, name
import csv
import sys
import random
import itertools
from time import sleep


N=10

selections= {'music': ['trumpet', 'tuba', 'trombone', 'euphonium', 'violin', 'viola', 'flute', 'oboe','guitar', 'bass', 'drums', 'celo', 'bassoon', 'triangle', 'timpani', 'piano', 'horn', 'clarinet', 'saxophone', 'snare'],
                'science': ['biology', 'physics', 'chemistry', 'zoology', 'optics', 'psychology', 'ecology', 'microbiology', 'botany', 'astronomy', 'biochemistry', 'agronomy', 'geology', 'psychoanalysis', 'geography', 'meteorology', 'pathology', 'ornithology', 'cosmology', 'entomology'],
                'presidents': ['lenin', 'stalin', 'malenkov', 'khurshchev', 'brezhnev', 'andropov', 'chernenko', 'gorbachev', 'hoover', 'roosevelt', 'nixon', 'carter', 'kennedy', 'truman', 'reagan', 'ford', 'eisenhower', 'johnson', 'De Gaulle', 'tito']}
def clear():
    if name== 'nt':
        _= system('cls')
    else:
        _= system('clear')

def main():
    clear()
    print("==============================================================")
    print("Welcome to Thomas Hu's word game, have fun and guess the words")
    playername= input("Input a name you want to use for this game: ")
    foo=1
    while foo!=0:
        menu(playername)


def rules():
    print("==============================================================")
    print("You can select one of three collections of words,")
    print("from which your answer word will be randomly selected.")
    print("You will have a few shots to guess for letters in the word,")
    print("namely, one less chance than the number of letters in the word")
    print("If you correctly guess one of the letters, the position of the")
    print("letter will be given, and no chances would be subtracted.")
    print("You will also get 1 point for each letter you get right.")
    print("You will get 1 point for each remaininng attempt if you get")
    print("the right word.")
    print("!Vamonos!")
    print("==============================================================")


def menu(playername):
    clear()
    print("Make your choices:")
    print("1. Instructions")
    print("2. Music instruments")
    print("3. Science studies")
    print("4. 20th century presidents")
    print("5. Randomly choose from the selections")
    print("6. Exit")
    print("7. Leaderboard")
    print("==============================================================")
    index=0
    selkey="a"
    while index>7 or index<1:
        indextemp= input("input the number key to the selection you chose: ")
        if indextemp.isdigit():
            index= int(indextemp)
        else:
            index= 0
        print("==============================================================")
        if index==5:
            index= (random.randint(1,3))%3+2
        if index==2:
            selkey= "music"
        if index==3:
            selkey= "science"
        if index==4:
            selkey= "presidents"
        if selkey== 1:
            rules()
        if index== 6:
            exit
        if index== 7:
            leaderboard()
        if index>1 and index<6:
            guess(selkey, playername)

def guess(selkey, playername):

    print(f"Great, your selection is: {selkey}")
    word= selections[selkey][random.randint(0,19)]
    length= len(word)
    print(f"A word with {length} letters is selected")
    attempts= length-1
    score=0

    wordtemp= [0]*(length)
    for i in range(length):
        wordtemp[i]= "#"


    while attempts>0:
        prevscore= score
        print("==============================================================")
        print(f"Attempt {length-attempts}")
        letter= input("Give the letter of your choice: ")
        print("==============================================================")
        print("Answers revealed:", end= " ")
        for i in range(length):
            if letter== word[i]:
                print(letter, end="")
                score+=1
                wordtemp[i]= word[i]
            else:
                print(wordtemp[i], end="")
        scorediff= score-prevscore
        print(" ")
        print(f"You guessed {scorediff} letters right!")
        if scorediff==0:
            attempts-=1
        if wordtemp== word:
            break
    print("==============================================================")
    print("End of round")
    score+= attempts
    if wordtemp==word:
        print(f"Congratulations, the right word is: {word}")
    else:
        print(f"The right word is: {word}")
    print(f"Your score is: {score}")
    print("==============================================================")
    leadingname= []
    leadingscore= []

    with open("leaderboard.txt") as f:
        leaderdict= csv.DictReader(f)
        for user in leaderdict:
            leadingname.append(user["name"])
            leadingscore.append(int(user["score"]))
    for i in range(9):
        if score>= leadingscore[i]:
            leadingscore.insert(i, score)
            leadingname.insert(i, playername)
            leadingscore.pop()
            leadingname.pop()




def leaderboard():
    leadingname=[]
    leadingscore=[]
    with open("leaderboard.txt") as f:
        leaderdict= csv.DictReader(f)
        for user in leaderdict:
            leadingname.append(user["name"])
            leadingscore.append(int(user["score"]))
    print ("Player, Score")
    for i in range(9):
        print(f"{leadingname[i]}, {leadingscore[i]}")







#print out menu with viable options "selection 1", "selection 2", "selection 3", "random selection"
#direct to individual functions
#ask whether user wants to exit or not

#selection individual functions:
#read file into dictionary
#assign keys "word" and "selection" to different blocks of information in the dict array
#randomly pick a word as "answer"
#record length of answer
#use while loop to assess the answer for length-1 times
#if yielded answer, print answer and contratulation
#if did not yield answer, print answer and direct back to menu


if __name__ == "__main__":
    main()


