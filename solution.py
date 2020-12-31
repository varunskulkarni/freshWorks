import json
import threading
import time
from file import File

class TimeToLive:
    # Insert key-value pair with time-to-live in seconds.
    def insert(self, key_value, key, value, secs):
        if key in key_value:
            print(f"\nKey: {key} already exists!\n")
        else:
            key_value[key] = value
            print(f"{key}: {value} iserted!\n")
            time.sleep(secs)
            del key_value[key]

class Solution(File):
    # Dictonary variable.
    key_value = dict()

    # Initilize with a given file.
    def initilize(self, fileName = "json.txt"):
        self.fObj = File(fileName)
        self.key_value = json.loads(self.fObj.readFile())
        print("\nInitilized successfully!\n")

    # Insert key-value pair into dictonary.
    def insert(self, key, value):
        if key in self.key_value:
            print(f"\nKey: {key} already exists!\n")
        else:
            self.key_value[key] = value
            print(f"{key}: {value} inserted!\n")

    # Delete a key-value pair from dictonary.
    def delete(self, key):
        if key in self.key_value:
            del self.key_value[key]
            print(f"\nKey: {key} is deleted successfully!\n")
        else:            
            print(f"\nKey: {key} do not exist!\n")

    # Get value from a given key.
    def getValue(self, key):
        if key in self.key_value:
            return self.key_value[key]
        else:
            print(f"\nKey: {key} do not exist!\n")
    
    # Save dictonary to a file.
    def writeToFile(self):
        try:
            fileName = input("\nEnter file name with extension to save json content: ")
            fileStr = json.dumps(self.key_value)
            File.writeFile(self, fString=fileStr, fileName=fileName)
            print(f"\nFile is saved!\n")
        except:
            print("\nSomething went worng!\n")

    # Separator
    def separator(self):
        print("-----*-----")

    # Menu
    def menu(self):
        while True:
            try:
                print("---MENU---")
                print("\n1. Initilize using file.")
                print("2. Insert a key-value pair.")
                print("3. Insert a key-value pair with time-to-live in seconds.")
                print("4. Get value of a key.")
                print("5. Delete a key-value pair.")
                print("6. Save to file.")
                print("7. Exit.\n")    
                choice = int(input("(Enter your choice)--> "))
                if choice == 1:
                    self.separator()
                    fileName = input("\nEnter file name: ")
                    self.initilize(fileName)
                    self.separator()
                elif choice == 2:
                    self.separator()
                    key = input("\nEnter key: ")
                    value = input("Enter value: ")
                    self.insert(key, value)
                    self.separator()
                elif choice == 3:
                    self.separator()
                    key = input("\nEnter key: ")
                    value = input("Enter value: ")
                    secs = int(input("Enter time in seconds: "))
                    tObj = threading.Thread(target = TimeToLive.insert, args=(5, self.key_value, key, value, secs))
                    tObj.start()
                    self.separator()
                elif choice == 4:
                    self.separator()
                    key = input("\nEnter key: ")
                    value = self.getValue(key)
                    if value != None:
                        print(f"\n{key}: {value}\n")
                    self.separator()
                elif choice == 5:
                    self.separator()
                    key = input("\nEnter key: ")
                    self.delete(key)
                    self.separator()
                elif choice == 6:
                    self.separator()                    
                    self.writeToFile()
                    self.separator()
                else:
                    if choice == 7:
                        break
                    else:
                        raise Exception(ValueError)
            except ValueError:
                self.separator()
                print("Invalid choice!")
                print("Re-enter your choice...")
                self.separator()
            finally:
                print("\n")

#MAIN
mainObj = Solution(File)
mainObj.menu()