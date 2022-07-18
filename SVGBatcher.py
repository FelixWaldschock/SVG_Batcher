
import numpy as np
import os
from pathlib import Path

# Pfade
print("Input toplevel directory")
topdir = os.path.dirname(os.getcwd())
# Topdir must inlcude Input and Output folder

# Folder
topdir = Path(topdir)
topdir = topdir / "Deckel"
input = topdir / "Input"
output = topdir / "Output"
temppath = topdir / "Template"

# Files
csv = input / "list.CSV"
template1 = temppath / "1_Template_single.svg"
template2 = temppath / "2_Template_double.svg"

def readCSV(f):
    return np.genfromtxt(f, delimiter=',',dtype=None,encoding='utf-8')

def checkCreateFolder(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return

def adjustTextFile(replaceString, replacement, filestring):
    if (not(type(replaceString)==list)):
        replaceString = [replaceString]
        print("Umwandlung des Repalcementstrings")
    if (not(type(replacement)==list)):
        replacement = [replacement]
        print("Umwandlung der Replacements")
    
    if(not(len(replacement) == len(replaceString))):
        print("Dimensions of replacements and to be reaplaced parts does not macht")
    
    for i in range(len(replaceString)):
        filestring = filestring.replace(replaceString[i], replacement[i])
        print("Datei umgeschrieben")

    return filestring

def createNewFile(content, path):
    file = open(path, 'w', encoding='utf8')
    file.write(content)
    file.close()
    return True

# Main cycle
data = readCSV(csv)
replacementStrings = ["Vorname", "Nachname"]
for i in range(len(data)):
    V = data[i][1]
    N = data[i][0]
    numOfNames = len(V.split())+len(N.split())
    if (numOfNames>2):
        template = template2
    else:
        template = template1
    # Einlesen der Vorlagedatei
    templateString = open(template, 'r')
    templateString = templateString.read()

    # Erstellen des neuen Dateinamens
    path = N + "_" + V + ".svg"
    path = path.replace(" ", "_")
    path = output / path
    newFileContent = adjustTextFile(replacementStrings, [N,V], templateString)
    createNewFile(newFileContent, path)




