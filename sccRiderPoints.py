import tkinter as tk
from tkinter import filedialog
import pandas as pd
import glob
import numpy as np
#import matplotlib.pyplot as plt
import itertools
import os, sys
from fnmatch import fnmatch

class TkFileDialogExample(tk.Frame):

  def __init__(self, root):

    tk.Frame.__init__(self, root)

    #define widgets
    
    tk.Label(self, text = 'READ THIS FIRST!!!!!!!').grid(row = 0, column = 0, columnspan = 2)
    tk.Label(self, text = 'Fill ride lengths.Fill 0 if N/A').grid(row = 1, column = 0, columnspan = 2)
    tk.Label(self, text = "Click 'RUN' button").grid(row = 2, column = 0, columnspan = 2)
    tk.Label(self, text = 'Select riders csv file').grid(row = 3, column = 0, columnspan = 2)
    tk.Label(self, text = 'Select contacts csv file').grid(row = 4, column = 0, columnspan = 2)
    tk.Label(self, text = 'If NO ERRORS, output.csv generated').grid(row = 5, column = 0, columnspan = 2)
    tk.Label(self, text = 'If ERRORS, follow pop up instructions').grid(row = 6, column = 0, columnspan = 2)
    
    tk.Label(self, text = "Very Short").grid(row = 7, column = 0)
    tk.Entry(self).grid(row = 7, column = 1)
    tk.Label(self, text = "Short").grid(row = 8, column = 0)
    tk.Entry(self).grid(row = 8, column = 1)
    tk.Label(self, text = "Medium").grid(row = 9, column = 0)
    tk.Entry(self).grid(row = 9, column = 1)
    tk.Label(self, text = "Long").grid(row = 10, column = 0)
    tk.Entry(self).grid(row = 10, column = 1)
    tk.Label(self, text = "Ultra Long").grid(row = 11, column = 0)
    tk.Entry(self).grid(row = 11, column = 1)
    
    tk.Button(self, text='RUN', command=self.askopenfilename).grid(row = 12, column = 1, columnspan = 2)

    # define options for opening or saving a file
    self.file_opt = options = {}
    options['defaultextension'] = '.csv'
    options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
    options['initialdir'] = 'C:\\'
    options['initialfile'] = 'myfile.txt'
    options['parent'] = root
    options['title'] = 'Select Rider List File'

    # This is only available on the Macintosh, and only when Navigation Services are installed.
    #options['message'] = 'message'

    # if you use the multiple file version of the module functions this option is set automatically.
    #options['multiple'] = 1

    # defining options for opening a directory
    self.contactFile_opt = contactFileoptions = {}
    contactFileoptions['defaultextension'] = '.csv'
    contactFileoptions['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
    contactFileoptions['initialdir'] = 'C:\\'
    contactFileoptions['initialfile'] = 'myfile.txt'
    contactFileoptions['parent'] = root
    contactFileoptions['title'] = 'Select Contacts List File'


  DuplicateExists = False
  def askopenfilename(self):

    """Returns an opened file in read mode.
    This time the dialog just returns a filename and the file is opened by your own code.
    """

    # get filename
    riderListFilename = filedialog.askopenfilename(**self.file_opt)
    #print(riderListFilename)
    
    contactListFilename = filedialog.askopenfilename(**self.contactFile_opt)
    #print(contactListFilename)

    # open file on your own
    if riderListFilename:
       self.riderFileStuff(riderListFilename)
       
    ###check for duplicates
    #initialize to false before every run
    self.Duplicates = False
    self.DuplicateExists = self.checkIfDuplicates (self.RiderIds)
    #print (self.DuplicateExists)
    
    # open file on your own
    if contactListFilename:
       self.contactFileStuff(contactListFilename)
    
    return


  EventFileHeaderNames = ['Registration type/Invitee reply']
  EventFileOtherHeaderNames = ['First name', 'Last name']
  EventCompleteFirstNames = []
  EventCompleteLastNames = []
  RiderIds = []
  RiderLength = []
  EventCompleteUserIdList = []
  
  rideLengthDict = {
    "Rider - Very Short" : 10,
    "Rider - Short" : 20,
    "Rider - Medium" : 30,
    "Rider - Long" : 40,
    "Rider - Ultra" : 50
    }  


  def riderFileStuff (self, riderFilename):
    dfs = pd.read_csv(riderFilename)
    dfs.columns = dfs.columns.str.strip()
    
    tempRegistrationTypeList = []
    
    
    self.EventCompleteFirstNames.clear()
    self.EventCompleteLastNames.clear()
    self.RiderIds.clear()
    self.RiderLength.clear()
    self.EventCompleteUserIdList.clear()
    
    self.EventCompleteFirstNames = dfs['First name'].tolist()
    self.EventCompleteLastNames = dfs['Last name'].tolist()
    
    #rint eventCompleteFirstNames
    #print eventCompleteLastNames
    
    #print dfs
    for headerNameIndex, value in enumerate (self.EventFileHeaderNames):
        tempRegistrationTypeList = dfs[value].tolist()
        self.EventCompleteUserIdList = dfs['User ID'].tolist()
        
        for registrationTypeIndex, registrationValue in enumerate (tempRegistrationTypeList):
            for key in self.rideLengthDict:
                #print (key)
                if key in registrationValue:
                    self.RiderIds.append(self.EventCompleteUserIdList[registrationTypeIndex])
                    self.RiderLength.append((self.rideLengthDict[key]))
                    #print (registrationTypeIndex)



  ListOfDuplicates = []
  def checkIfDuplicates(self, listOfElems):
    ''' Check if given list contains any duplicates '''    
    setOfElems = set()
    del self.ListOfDuplicates [:]
    for elem in listOfElems:
        if elem in setOfElems:
            self.ListOfDuplicates.append(elem)
        else:
            setOfElems.add(elem)         
    
    if(len(self.ListOfDuplicates) > 0):
        return True
    else:
        return False


  ContactsFileHeaderNames = ['User ID', 'Total Miles', 'No. of Rides Attended', 'Membership level']
  def contactFileStuff (self, contactFileName):
    df = pd.read_csv(contactFileName)
    df.columns = df.columns.str.strip()
    
    ContactsUserIDList = df[self.ContactsFileHeaderNames[0]].tolist()
    TotalMilesList = df[self.ContactsFileHeaderNames[1]].tolist()
    TotalRidesList = df[self.ContactsFileHeaderNames[2]].tolist()
    MembershipLevelList = df[self.ContactsFileHeaderNames[3]].tolist()
    
    if (self.DuplicateExists == True):
        self.printDuplicates(self.ListOfDuplicates, self.EventCompleteUserIdList, self.EventCompleteFirstNames, self.EventCompleteLastNames)
    else:
        #generate output file
        for userIdIndex, userIdToUpdate in enumerate (self.RiderIds):
            #print userIdToUpdate
            indexToUpdate = ContactsUserIDList.index(userIdToUpdate)
            #print 'totalMilesList before' + str(TotalMilesList)
            TotalMilesList[indexToUpdate] = TotalMilesList[indexToUpdate] + self.RiderLength[userIdIndex]
            TotalRidesList[indexToUpdate] = TotalRidesList[indexToUpdate] + 1
        
        processedDf = pd.DataFrame()
        processedDf['User ID'] = ContactsUserIDList
        processedDf['Total Miles'] = TotalMilesList
        processedDf['No. of Rides Attended'] = TotalRidesList
        processedDf['Membership level'] = MembershipLevelList
        processedDf.to_csv('output.csv', sep=',')
        print ("Output File Generated")
        self.popupmsgOutputGenerated()


  ListOfDuplicatesFullName = []
  def printDuplicates (self, 
                        listOfDuplicates, 
                        listEventCompleteUserIds, 
                        listEventCompleteFirstNames,
                        listEventCompleteLastNames):
    self.ListOfDuplicatesFullName.clear()
    for elements in listOfDuplicates:
        #print (listOfDuplicates)
        #print (elements)
        #print (len(listEventCompleteUserIds))
        #print (listEventCompleteUserIds)
        #print ("indexNeeded")
        indexNameNeeded = listEventCompleteUserIds.index(elements)
        #print (indexNameNeeded)
        #print (len(listEventCompleteFirstNames))
        #print (len(listEventCompleteLastNames))
        #print ("This rider has duplicate entries " + listEventCompleteFirstNames[indexNameNeeded] + " " + listEventCompleteLastNames[indexNameNeeded])
        #print ("Delete same entry from events list and rerun code")
        self.ListOfDuplicatesFullName.append(listEventCompleteFirstNames[indexNameNeeded] + " " + listEventCompleteLastNames[indexNameNeeded])
    fullMsgString = ""
    for fullNames in self.ListOfDuplicatesFullName:
        fullMsgString = fullMsgString + fullNames + ", "
    self.popupmsg(fullMsgString)
        
  def popupmsg(self, msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text= "These riders have duplicate entries, delete duplicate entires and rerun code")
    label.pack(side="top", fill="x", pady=10)
    label = tk.Label(popup, text= msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
  def popupmsgOutputGenerated(self):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text= "Output file generated in the same folder as your input files")
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

if __name__=='__main__':
  root = tk.Tk()
  root.title("Rider length and total rides calculator")
  #TkFileDialogExample(root).pack()
  #root.mainloop()
  TkFileDialogExample(root).grid(row = 0, column = 0)
  root.mainloop()
