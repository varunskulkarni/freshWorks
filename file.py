class File:
    def __init__(self, fileName):
        self.fileName = fileName
    # Bring back pointer to first row first column.
    def closeFile(self, fptr):
        fptr.seek(0, 0)
        fptr.close()
    
    # Read file content.
    def readFile(self):
        try:
            fptr = open(self.fileName, "r")
            lines = fptr.read()
            return lines
        except FileNotFoundError:
            print("File do not exist!")
        finally:
            self.closeFile(fptr)

    # Write back to file.
    def writeFile(self, fString, fileName):
        try:
            fptr = open(fileName, "w")
            fptr.write(fString)           
        except:
            print("Something went wrong...")
        finally:
            self.closeFile(fptr)