def fileList():
    filename = input('Please enter the filename: ')
    file = open(filename, 'r')
    lines = file.readlines()

    lineNum = len(lines)

    return lines, lineNum
        

def filePrint(lines, lineNum):
    repeat = True
    pLines = lines  
    while repeat:
     print("The number of lines in the file are ", lineNum)
     num = int(input("Please enter a line to print or input 0 to quit: "))
     if num >= 1 and num <= lineNum:
        print(pLines[num-1])
     elif num > lineNum:
         print("Line input is greater than lines in text file.")
     else:
        if num == 0:
            repeat = 0
            print("Now exiting...")

def main():
    lines, lineNum = fileList()
    filePrint(lines, lineNum)

main()