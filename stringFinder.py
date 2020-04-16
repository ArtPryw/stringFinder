import os
from tkinter import filedialog

def choice_path():
    choice= input('Do u want pick a network drive?  y/n')
    if choice == 'n' or choice == 'N':
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
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

def findAllOutDirs(path=path):
    finalPathList = []
    for root, subdirs, files in os.walk(path):
            for d in subdirs:
                    if d == "out" or d == "OUT":
                        outPath = root+r"\{}".format(d)
                        if ("DANE" in outPath) and ("2018" in outPath or "2019" in outPath or "2020" in outPath):
                            print(outPath)
                       # finalPathList.append(outPath)
                
                
path = choice_path()                
findAllOutDirs()