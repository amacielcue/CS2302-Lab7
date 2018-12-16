#CS2302 Lab7-A
#By: Alejandra Maciel
#Last Modified: Dic-15-2018
#Instructor: Diego Aguirre
#TA: Manoj  Pravaka  Saha
#The purpose of this lab is to learn how to use dynamic programming but solving the edit distance problem.


#Method to create matrix and fill it out depending on the string's matching characters.
def edit_distance(str1, str2):
    #Create 2D-array or matrix of the length of str1 by length of str2
    matrix = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]

    #Loop to change the horizontal (row/str1) starting values
    for i in range(1, len(str1)+1):
        matrix[i][0] = i

    #Loop to change the vertical (column/str2) starting values
    for j in range(1, len(str2)+1):
        matrix[0][j] = j

    #Nested loop to traverse all the matrix
    for i in range(len(str1)):
        for j in range(len(str2)):
            #If the charcater of the str1 and the character of str2 are the same then pass the diagonal value
            if str1[i] == str2[j]:
                matrix[i+1][j+1] = matrix[i][j]
            #Else, if they differ then pass the smallest adjacent value plus 1
            else:
                matrix[i+1][j+1] = min(matrix[i+1][j], matrix[i][j], matrix[i][j+1]) + 1

    #Return the last value added to the matrix
    return matrix[len(str1)][len(str2)]



