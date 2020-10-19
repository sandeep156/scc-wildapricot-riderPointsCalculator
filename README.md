# scc-wildapricot-riderPointsCalculator

This GUI was created in Python using http://effbot.org/zone/tkinter-index.htm as reference.
GUI was developed to help keep track of rider mileages for the Schlumberger Cycling Club.

Get the executable file from the release tab. 
V1 released on 10/18/2020.

To use this GUI, you will need input files from WildApricot.
The input files are: 

1. Event registration file that contains ride registration type (short, medium etc.)
2. Contacts file that contains information on all members.

***Steps to get input files and run GUI***

0. Download the executable from the release tab

1. Go to the admin view of the Wild Apricot site.

2. Click on Events > Event list as show below:

![Image of events list](https://github.com/sandeep156/scc-wildapricot-riderPointsCalculator/blob/master/readmeImages/1_EventsList.jpg)

3. Select an event. In this case, Fulshear High School event was selected. 

4. Click on the "Export registrants" button at the top, as seen in screenshot below:

![Image of reigstrants export](https://github.com/sandeep156/scc-wildapricot-riderPointsCalculator/blob/master/readmeImages/3_ExportRegistrants.jpg)

5. In the pop up that ensues, keep the csv file setting, and check the rest of the boxes as shown below:

![Image of export list 1](https://github.com/sandeep156/scc-wildapricot-riderPointsCalculator/blob/master/readmeImages/4_exportDetails1.jpg)
![Image of export list 2](https://github.com/sandeep156/scc-wildapricot-riderPointsCalculator/blob/master/readmeImages/5_exportDetails2.jpg)

6. Click on "Export" and select where to save the file on your machine.

7. Now go to Contacts. Click on "Export" link to bring up the pop up in the next step.

![Image of contacts tab](https://github.com/sandeep156/scc-wildapricot-riderPointsCalculator/blob/master/readmeImages/6_ContactsTab.jpg)

8. In the Contact Export pop up, keep the csv file setting, and check the rest of the boxes as shown below:

![Image of export contacts 1](https://github.com/sandeep156/scc-wildapricot-riderPointsCalculator/blob/master/readmeImages/7_exportContacts1.jpg)
![Image of export contacts 2](https://github.com/sandeep156/scc-wildapricot-riderPointsCalculator/blob/master/readmeImages/8_exportContacts1.jpg)

9. Click on "Export" and select where to save the file on your machine.

10. **Run the GUI and follow self-explanatory instructions on the GUI**

![Image of GUI](https://github.com/sandeep156/scc-wildapricot-riderPointsCalculator/blob/master/readmeImages/11_GUIScreenshot.jpg)

11. GUI generates an output file in the folder where it's run from. It should be called **output.csv**.


***Steps to upload output file back on Wild Apricot***

12. In the admin view of the wild apricot site, go back to the "Contacts" tab and click on "Import" to bring up screenshot below:

![Image of import](https://github.com/sandeep156/scc-wildapricot-riderPointsCalculator/blob/master/readmeImages/9_ImportTab.jpg)

13. Browse and select the "output.csv" file that was generated by the GUI in step 10, then click on "Upload". Click "Next" on the prompts that follow until import
is completed.

![Image of import_upload](https://github.com/sandeep156/scc-wildapricot-riderPointsCalculator/blob/master/readmeImages/10_SelectOutputcsv.jpg)

14. Updated mileages and ride count should now reflect on each rider's profile page!
