import json
import sys
import SubQual

#global variables
global jsonFile

#start main program
#print greeting
print()
print("Subjective Quality Evaluation System")
print("--------------------------------------")
print()
while True:
    #print out the menu
    print("===== Main Menu =====")
    print("Please select an option :")
    print("  1  Import Test Data From File")
    print("  2  Print Data Summary Report")
    print("  3  Output Summary Report to File")
    print("  4  View Details of an Individual Test")
    print("  5  View Details of an Individual Video Clip")
    print("  X  Exit")

    #get the users choice
    choice = input(">>> ")
    print()
    #carry out task
    if choice == '1':
        newjson = SubQual.importer()
        jsonFile = newjson
        #jsonFile = json.load(newjson)
        #print(newjson)
    elif choice == '2':
        try:
            SubQual.printReport(jsonFile)
        except NameError:
            print("*NO FILE DEFINED*")
            print("Please Import Test Data From File first")
    elif choice == '3':
        try:
            SubQual.createJsons(jsonFile)
        except NameError:
            print("*NO FILE DEFINED*")
            print("Please Import Test Data From File first")
    elif choice == '4':
        try:
            SubQual.printSingle(jsonFile)
        except NameError:
            print("*NO FILE DEFINED*")
            print("Please Import Test Data From File first")
    elif choice == '5':
        try:
            SubQual.testClip(jsonFile)
        except NameError:
            print("*NO FILE DEFINED*")
            print("Please Import Test Data From File first")
    elif choice == 'X' or choice == 'x':
        print("Thanks, Bye!")
        sys.exit(0)
        #break
    else:
        print("Invalid choice")
    print()