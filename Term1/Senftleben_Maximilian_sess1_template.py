def printHello():
    # Add your code here to print "Hello, World!" to the screen
    print("Hello, World!")

def readAndSaveFile(filename):
    # Add code here to read in your file line by line etc
    
    fil=open(filename,"r").readlines()
    fi_headtail=open(filename+"_headtail","w")
    firstline=fil[0]
    lastline=fil[-1]
    fi_headtail.write(firstline + lastline)

def printTwoStrings(stringA, stringB):
    # Add code here to print the two supplied lines to the screen
        
    print(stringA,stringB)
    
if __name__=="__main__":
    printHello()
    readAndSaveFile("sc.txt")
    printTwoStrings("First: ", "Second: ")
