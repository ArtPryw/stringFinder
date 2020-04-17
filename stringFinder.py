import os
from tkinter import filedialog
from tkinter import Tk
from datetime import datetime


def choice_path():
    choice= input('Do u want pick a network drive?  y/n')
    if choice == 'n' or choice == 'N':
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        path = folder_selected
        return path
    elif choice == 'y' or choice =='Y':
        path = input('Enter a path to network drive. Example: //10.64.67.69/gs/GP/')
        return r'{}'.format(path)
    else:
        print("Error. Choice y or n")
        end = input('if exit, press x and click enter')
        if end == 'x':
            return
        else:
            choice_path()

def findAllOutDirs(path):
    finalPathList = []
    for root, subdirs, files in os.walk(path):
            for d in subdirs:
                    if d == "out" or d == "OUT":
                        outPath = root+r"\{}".format(d)
                        if ("DANE" in outPath) and ("2018" in outPath or "2019" in outPath or "2020" in outPath):
                            finalPathList.append(outPath)
    return finalPathList

def writeListToTxt(listOfPaths):
    initializerCommunicate = "writing file in progress..."
    finishCommunicate = "File saved succesfull. "
    errorCommunicate = 'Something is wrong with file. Error.'
    listOfPaths = listOfPaths
    def writeFile(listOfPaths, fileName):
        print(initializerCommunicate)
        try:
            with open(fileName, 'w') as f:
                for i in listOfPaths:
                    f.write("%s\n" % i)
            print(finishCommunicate)
        except:
            print(errorCommunicate)
    try:
        fileName = input('enter file output name...')
        if len(fileName) < 40:
            fileName = fileName + ".txt"
            writeFile(listOfPaths, fileName = fileName)
        else:
            print('Maximum file name == 40 + extension. Your file will be cut to that size.')
            fileName = filename[:41] + ".txt"
            writeFile(listOfPaths, fileName = fileName)
    except:
        print("something wrong with your input! File will be named: OutGenerate with timestamp in format: DDMMYYY_HH_MM_SS")
        now = datetime.now()
        today = now.strftime("%d%m%Y_%H%M%S")
        fileName = 'OutGenerate_' + today + '.txt'
        writeFile(listOfPaths, fileName)

        
        
    
w_path = choice_path() 
dirsList = findAllOutDirs(w_path)
writeListToTxt(dirsList)




#testowanko nowej funckji
files = []
# r=root, d=directories, f = files
for i in dirsList:
    for r, d, f in os.walk(i):
        for file in f:
            pathToCsv = os.path.join(r, file)
            if '.2col' or '.2COL' or '.csv' or '.CSV' in pathToCsv:
                #print(pathToCsv)
                files.append(pathToCsv)
#writeListToTxt(files)
for i in files:
    print(i)
