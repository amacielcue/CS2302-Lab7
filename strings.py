#CS2302 Lab7-A
#By: Alejandra Maciel
#Last Modified: Dic-15-2018
#Instructor: Diego Aguirre
#TA: Manoj  Pravaka  Saha
#The purpose of this lab is to learn how to use dynamic programming but solving the edit distance problem.

from Lab7 import edit_distance

#Main Method
def main():
    #Hard Coded strings
    str1 = "miners"
    str2 = "monkey"

    #Call the edit distance method and print the answer.
    print("###########################################################################################################")
    print("The number of operations needed to convert the word " + str1 + " into the word " + str2 + " is : " + str(edit_distance(str1, str2)))
    print("###########################################################################################################")


#Main Method Caller
main()