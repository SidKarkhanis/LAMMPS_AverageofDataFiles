############################################
#Reads
#Gives you average of files 
#Creator :- Sid S. Karkhanis 
############################################

#Importing Section 

import numpy as np
import pandas as pd

#################################################################################
#This is for log files
#Change the Details
NumberofFiles=10                                         #Number of Total of File
IndividualMeans="Mean_AllFiles.txt"                      #Output File where Mean Values from All files will be saved
TemporaryFiles="Lines_MeanAllFiles.txt"                  #Output File where Mean of All values from above file is stored
FileNames=[]
ContentNames=[]
RefinedContentNames=[]
print("___________________________________________________")
print("These are the available files")
for i in range(0,NumberofFiles):
    FileNames.append("File_" + str(i+1) + ".txt")                 #Input File Name Structure [eg. for three files as : File_1.txt, File_2.txt, File_3.txt]
    ContentNames.append("Contents_"+ "Text_" + str(i+1))
    RefinedContentNames.append(ContentNames[i])
    print("{}".format(FileNames[i]))
print("___________________________________________________")

##############################################
#Dont Change This Section

for i in range(0,NumberofFiles):
    ContentNames[i]=pd.read_csv(FileNames[i], delim_whitespace=True,header=None)                   #Choose According to your Data Files
    #ContentNames[i]=pd.read_csv(FileNames[i], delimiter='\t',header=None)                          #Choose According to your Data Files
    RefinedContentNames[i]=ContentNames[i].drop(ContentNames[i].columns[0],axis=1)
    print(RefinedContentNames[i].head(3))
    print("___________________________________________________")
Files_1=open(IndividualMeans,"w+")
for i in range(0,NumberofFiles):
    Means=RefinedContentNames[i].mean()
    for j in range (1,len(RefinedContentNames[i].axes[1])):
        Files_1.write("{}\t".format(Means[j]))
    Files_1.write("\n")
Files_1.close()
Average=pd.read_csv(IndividualMeans, delim_whitespace=True,header=None)
Average=pd.read_csv(IndividualMeans, delimiter='\t',header=None)
print("___________________________________________________")
print("Final File Looks Like This :-")
print(Average)
FinalAverage=Average.drop(Average.columns[-1],axis=1)
print("___________________________________________________")
print(FinalAverage)
Means=FinalAverage.mean()
Files_2=open(TemporaryFiles,"w+")
print("___________________________________________________")
for j in range (0,len(FinalAverage.axes[1])):
    print(Means[j],end="\t")
    Files_2.write("{:.2f}\t".format(Means[j]))
Files_2.close()
print("Done")

