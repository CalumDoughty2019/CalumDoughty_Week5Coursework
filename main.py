import json
from inspect import currentframe, getframeinfo
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

        for i in jsonFile:
            frameinfo = getframeinfo(currentframe())
            #check to make sure there is no missing "Test number"'s
            # key = "Test Number"
            # if key not in i:
            #     print("WARNING::: NO \"Test Number\" FOUND!")
            #     print("\tPlease verify integrity/spelling of file data. Line No: " + str(newjson.lineno))
            #check to make sure there is no missing "Video Clip ID"'s
            key = "Video Clip ID"
            if key not in i:
                print("WARNING::: NO \"Video Clip ID\" FOUND!")
                print("\t\t\tPlease verify integrity/spelling of file data. Test No: " + str(i["Test Number"]))
            #check to make sure there is no missing "Bandwidth Constraint"'s
            key = "Bandwidth Constraint"
            if key not in i:
                print("WARNING::: NO \"Bandwidth Constraint\" FOUND!")
                print("\t\t\tPlease verify integrity/spelling of file data. Test No: " + str(i["Test Number"]))


        # Check there are no duplicate ID's. If there is then WARN user
        try:
            for i in newjson: #use newJson so we can remove elements, otherwise we get repeat alerts if there are duplicates meaning If 2 ID's have value 1 then we will see alert twice.
                IDcounter = 0
                for j in jsonFile:
                    if i["Test Number"] == j["Test Number"]:
                        IDcounter += 1
                if IDcounter > 1:
                    print("WARNING::: DUPLICATE \"Test Number\" FOUND! ID:" + str(i["Test Number"]))
                newjson.remove(i)
        except KeyError:
            print("WARNING::: NO \"Test Number\" FOUND for an item!")
            print("\t\t\tPlease verify integrity/spelling of file data.")
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
        print("Thanks for using our service, Bye!")
        sys.exit(0)
        #break
    else:
        print("Invalid choice")
    print()