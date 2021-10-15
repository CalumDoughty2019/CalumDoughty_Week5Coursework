import json
import os.path

import numpy
import numpy as np


#used to go back to main menu
def validator(jsonFile):
    checker = False
    while not checker:
        try:
            print()
            print("1. Go to main menu")
            print("2. Repeat this step")
            step = input(">> ")
            if step == "1":
                return ##return to main menu
            elif step == "2":
                print()
                printSingle(jsonFile)
            else:
                print("INCORRECT: Please check value input")
                print()
        except IOError:
            print("Could not read file: ", fileName)


# Option1: Import Test Data From File
#https://www.pythontutorial.net/python-basics/python-check-if-file-exists/
def importer():
    print("===== JSON Importer =====")
    print("please type 0 to go to menu")
    #print()
    global fileName
    checker = False
    while not checker:
        try:
            fileName = input("Enter file name: ")
            if os.path.exists(fileName):
                #return fileName
                opener = open(fileName)
                newjson = json.load(opener)
                print("import: SUCCESS")
                opener.close()
                return newjson
                #return np.asarray(newjson)
            elif fileName == "0":
                return None ##return to main menu
            else:
                print("INCORRECT: Please check file is a JSON")
                print("INCORRECT: Please check input ends with .json")
                print()
        except IOError:
            print("Could not read file: ", fileName)


# Option2: Print Data Summary Report
def printReport(jsonFile):
    print("===== Print Summary Report =====")
    #if jsonFile == 0 or jsonFile is None:
    if jsonFile is None:
        print("NO file has been submitted")
        return None
    else:
        print("Test No\t\tClip ID\t\tBandwidth Setting\tAvg.Score\tMin Score\tMax Score")
        #print(jsonFile.shape())

        for i in jsonFile:
            average = (i["Subject A"] + i["Subject B"] + i["Subject C"] + i["Subject D"] + i["Subject E"] + i["Subject F"] + i["Subject G"] + i["Subject H"] + i["Subject I"] + i["Subject J"] + i["Subject K"] + i["Subject L"] + i["Subject N"] + i["Subject O"])/14
            average = int(round(average))

            #make a new dictionary with just the grades so that we can find minimum and maximum values
            gradeDict = []
            comparison = ["Subject A", "Subject B", "Subject C", "Subject D", "Subject E", "Subject F", "Subject G", "Subject H", "Subject I", "Subject J", "Subject K", "Subject L", "Subject N", "Subject O"]
            for k in i.keys():
                if k in comparison:
                    gradeDict.append(i[k])
            minElement = numpy.amin(gradeDict)
            maxElement = numpy.amax(gradeDict)
            #print(sameDict)


            print("\t" + str(i["Test Number"]) + "\t\t\t" + str(i["Video Clip ID"]) + "\t\t\t" + str(i["Bandwidth Constraint"]) + "\t\t\t\t\t" + str(average) + "\t\t\t" + str(minElement) + "\t\t\t" + str(maxElement))
            #print(i)
        #return None


# Option3: Create json "summary_data" & use numpy to scale info for second json called "scaled_data"
#https://stats.stackexchange.com/questions/281162/scale-a-number-between-a-range
def createJsons(jsonFile):
    print("===== Summary Report to File =====")
    with open("summary_data.json", "w") as summary:
        json.dump(jsonFile, summary, indent=4)

    newFile = []
    for i in jsonFile:
        total = 0
        gradeDict = []
        comparison = ["Subject A", "Subject B", "Subject C", "Subject D", "Subject E", "Subject F", "Subject G",
                      "Subject H", "Subject I", "Subject J", "Subject K", "Subject L", "Subject N", "Subject O"]
        for k in i.keys():
            if k in comparison:
                gradeDict.append(i[k])
        for j in gradeDict:
            total = total + j
        average = total / len(gradeDict)
        #average = average * 4 #to scale from range 1-5 upto 1-20
        average = np.multiply(average, 4)
        # average = int(round(six))

        newDict = {}
        newDict["Test Number"] = i["Test Number"]
        newDict["Average"] = average
        newFile.append(newDict)

    with open("scaled_data.json", "w") as scaled:
        json.dump(newFile, scaled, indent=4)
    print("Summary printed")


# Option4: Display data for a specific test number
def printSingle(jsonFile):
    print("===== Print Single Test =====")
    print("please type 0 to go to menu")
    if jsonFile is None:
        print("NO file has been submitted")
        return None
    else:
        checker = False
        while not checker:
            try:
                id = input("Enter ID number: ")
                if id == "0":
                    return None  ##return to main menu
                for i in jsonFile:
                    if i["Test Number"] == int(id):
                        print("Test No\t\tClip ID\t\tBandwidth Setting\tAvg.Score\tMin Score\tMax Score")

                        average = (i["Subject A"] + i["Subject B"] + i["Subject C"] + i["Subject D"] + i["Subject E"] +
                                   i[
                                       "Subject F"] + i["Subject G"] + i["Subject H"] + i["Subject I"] + i[
                                       "Subject J"] + i[
                                       "Subject K"] + i["Subject L"] + i["Subject N"] + i["Subject O"]) / 14
                        average = int(round(average))

                        # make a new dictionary with just the grades so that we can find minimum and maximum values
                        gradeList = []
                        comparison = ["Subject A", "Subject B", "Subject C", "Subject D", "Subject E", "Subject F",
                                      "Subject G", "Subject H", "Subject I", "Subject J", "Subject K", "Subject L",
                                      "Subject N", "Subject O"]
                        for k in i.keys():
                            if k in comparison:
                                gradeList.append(i[k])
                        minElement = numpy.amin(gradeList)
                        maxElement = numpy.amax(gradeList)
                        # print(sameDict)

                        print("\t" + str(i["Test Number"]) + "\t\t\t" + str(i["Video Clip ID"]) + "\t\t\t" + str(
                            i["Bandwidth Constraint"]) + "\t\t\t\t\t" + str(average) + "\t\t\t" + str(
                            minElement) + "\t\t\t" + str(maxElement))

                        checker = True
                        #validator(jsonFile)
                    #else:
                if checker:
                    print()
                    input("Press Enter to continue...")
                    return
                else:
                    print("NOT a recognised id number")

            except IOError:
                print("Could not read file: ", fileName)
            except NameError:
                print("No recognised ID")


# Option5: prompt for a clip ID and produce a report
def testClip(jsonFile):
    print("===== Clip Report =====")
    print("please type 0 to go to menu")
    if jsonFile is None:
        print("NO file has been submitted")
        return None
    else:
        maxList = []
        #maxCount = 0
        avList = []
        neg3List = []
        neg5List = []
        neg10List = []
        pos10List = []
        maxMean = 0
        avMean = 0
        neg3Mean = 0
        neg5Mean = 0
        neg10Mean = 0
        pos10Mean = 0

        checker = False
        while not checker:
            try:
                clip = input("Enter clip ID: ")
                if clip == "0":
                    return None  ##return to main menu
                for i in jsonFile:
                    if i["Video Clip ID"] == clip:
                        comparison = ["Subject A", "Subject B", "Subject C", "Subject D", "Subject E", "Subject F",
                                      "Subject G",
                                      "Subject H", "Subject I", "Subject J", "Subject K", "Subject L", "Subject N",
                                      "Subject O"]
                        if i["Bandwidth Constraint"] == "MAX":
                            #maxCount += 1
                            for k in i.keys():
                                if k in comparison:
                                    maxList.append(i[k])
                            maxMean = sum(maxList) / len(maxList)
                            maxMean = int(round(maxMean))
                        if i["Bandwidth Constraint"] == "AV":
                            for k in i.keys():
                                if k in comparison:
                                    avList.append(i[k])
                            avMean = sum(avList) / len(avList)
                            avMean = int(round(avMean))
                        if i["Bandwidth Constraint"] == -3:
                            for k in i.keys():
                                if k in comparison:
                                    neg3List.append(i[k])
                            neg3Mean = sum(neg3List) / len(neg3List)
                            neg3Mean = int(round(neg3Mean))
                        if i["Bandwidth Constraint"] == -5:
                            for k in i.keys():
                                if k in comparison:
                                    neg5List.append(i[k])
                            neg5Mean = sum(neg5List) / len(neg5List)
                            neg5Mean = int(round(neg5Mean))
                        if i["Bandwidth Constraint"] == -10:
                            for k in i.keys():
                                if k in comparison:
                                    neg10List.append(i[k])
                            neg10Mean = sum(neg10List) / len(neg10List)
                            neg10Mean = int(round(neg10Mean))
                        if i["Bandwidth Constraint"] == 10:
                            for k in i.keys():
                                if k in comparison:
                                    pos10List.append(i[k])
                            pos10Mean = sum(pos10List) / len(pos10List)
                            pos10Mean = int(round(pos10Mean))


                        checker = True

                if checker:
                    print()
                    print("Summary Data for Test Clip: " + clip)
                    print("Total number of tests conducted: " + str(len(jsonFile)))
                    print("Bandwidth Setting\t\t\tMAX\t\tAV\t\t-3\t\t-5\t\t-10")
                    print("Mean Opinion Score\t\t\t " + str(maxMean) + "\t\t " + str(avMean) + "\t\t " + str(
                        neg3Mean) + "\t\t " + str(neg5Mean) + "\t\t " + str(neg10Mean))
                    print("Count (N)\t\t\t\t\t " + str(len(maxList)) + "\t\t " + str(len(avList)) + "\t\t " + str(
                        len(neg3List)) + "\t\t " + str(len(neg5List)) + "\t\t " + str(len(neg10List)))
                    print()
                    input("Press Enter to continue...")
                    return
                else:
                    print("NOT a recognised clip ID")

            except IOError:
                print("Could not read file: ", fileName)
            except NameError:
                print("No recognised ID")