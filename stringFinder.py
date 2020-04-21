import os
from tkinter import filedialog
from tkinter import Tk
from datetime import datetime
from timeit import default_timer as timer
import time 
from io import open
import lzma
import gzip


initializerCommunicate = "writing file in progress..."
finishCommunicate = "File saved succesfull. "
errorCommunicate = 'Something is wrong with file. Error.'

    
    
def time_measure(foo):
    start = time.time()
    foo
    stop = time.time()
    print('function takes: ', stop-start)

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
                        outPath = root+r"/{}".format(d)
                        if ("DANE" in outPath) and ("2018" in outPath or "2019" in outPath or "2020" in outPath):
                            finalPathList.append(outPath)
    return finalPathList

def final_list_to_txt(list_to_save):
    fileName = 'result.txt'
    print(initializerCommunicate)
        try:
            with open(fileName, 'w') as f:
                for i in list_to_save:
                    f.write("%s\n" % i)
            print(finishCommunicate)
        except:
            print(errorCommunicate)

def writeListToTxt(listOfPaths):
    
    listOfPaths = listOfPaths
    def writeFile(listOfPaths, fileName):
        print(initializerCommunicate)
        try:
            with open(fileName, 'w') as f:
                for i in listOfPaths:
                    f.write("%s/n" % i)
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
        
def filesList():
    w_path = choice_path()
    dirsList = findAllOutDirs(w_path)
    #print(dirsList)
    files = []
    # r=root, d=directories, f = files
    for i in dirsList:
        for r, d, f in os.walk(i):
            for file in f:
                pathToCsv = os.path.join(r, file)
                if ('.csv' in pathToCsv) or ('.txt' in pathToCsv) or ('.CSV' in pathToCsv) or ('.TXT' in pathToCsv):
                    files.append(pathToCsv)
    return files
        
def create_SNP_list(target_str):
    filesList_g = filesList()
    #print(filesList_g)
    found = []
    target = str(target_str)
    print("Searching for:", target_str)
    print("Supported extends: 'txt, csv, xz, gz'. May works with others for text files but not supported.")
    #Extension block
    ext = []
    for l in filesList_g:
        ext.append(l.rsplit('.', 1)[1])
    ext = list(set(ext))
    print("Found files extends", ext)
    
    counter_current = 0
    counter_stop = len(filesList_g)
    for file_path in filesList_g:
        print('{}/{}'.format(counter_current,counter_stop))
        counter_current+=1
        try:
            if '.xz' in file_path:
                #print("file_path = ", file_path)
                with lzma.open(file_path, mode='rt') as src:
                    for line in src:
                        #if len(line) == 0: break #happens at end of file, then stop loop
                        if target in line:
                            found.append(line)

            elif '.gz' in file_path:
                with gzip.open(file_path,'rt') as src:
                    for line in src:
                        if target in line:
                            found.append(line)
                            
            elif '.txt' in file_path or '.csv' in file_path:
                with open(file_path,'r',encoding='UTF-8') as src:
                    for line in src:
                        if target in line:
                            found.append(line)
            
        except:
            print("Something is wrong with open file:", file_path, +'. File will be omitted.')
            try:
                with open('logs.txt', 'a') as f:
                        f.write("%s/n" % file_path)
            except:
                print(errorCommunicate)
            
    return found



string_looking_for = input("What u pattern U try to find?")                                 
almost_final_list = create_SNP_list(string_looking_for)
final_list_to_txt(almost_final_list)