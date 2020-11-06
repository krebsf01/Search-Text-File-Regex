#Regex

import re, os

Found = []
while Found == []:
    # User will enter info to be searched for
    print("Enter the info(it can be a Regex pattern) you want to search for:")
    searchInput = re.compile(input())
        

    #Open file to be searched
    print('Enter the file path:')
    filePath = input()
    os.chdir(f'{filePath}')
    print('Enter the file name with the file extension:')
    fileName = input()
    cvFile = open(f'{fileName}').read()


    #Search user-input pattern
    Found = re.findall(searchInput, cvFile)

    if len(Found) >= 1:
        if isinstance(Found[0], tuple):
            for i in range(len(Found)):
                print(Found[i][0])
        else:
            for i in range(len(Found)):
                print(Found[i])




