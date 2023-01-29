############################################
#Gives you average of Multiple RDF Data files
#Plots the RDF plot of Final Averaged Values 
#Author :- Sid Karkhanis
############################################

import sys
argv = sys.argv
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#################################################################################
#This is for RDF files
#Change the Details
NumberofFiles=10                                                          #Number of Versions of File
NumberofColumns=4			                                  #Final Number of Columns
IndividualMeans="FileMeans.txt"                                           #Where Mean of All values from above file is stored
PlotNameSaved="RDF_Plot.png"                                              #Name of the [File] graph to be plotted
FileNames=[]
ContentNames=[]
RefinedContentNames=[]
TempoFiles=[]
TempoFilesAgain=[]
print("___________________________________________________")
print("These are the available files")
for i in range(0,NumberofFiles):
    FileNames.append("File_" + str(i+1) + ".csv")                       #Change the First Names
    ContentNames.append("Contents_" + FileNames[i] + str(i+1))
    RefinedContentNames.append("Refined_" + ContentNames[i])
    print("{}".format(FileNames[i]))
print("___________________________________________________")

############################################################################################
#Dont Change This Section

for i in range(0,NumberofFiles):
    ContentNames[i]=pd.read_csv(FileNames[i], delim_whitespace=True, skiprows=4, header=None)                   #Data Files prefer this
    #ContentNames[i]=pd.read_csv(FileNames[i], delimiter='\t',header=None)                    
    RefinedContentNames[i]=ContentNames[i].drop(ContentNames[i].columns[[0,3,5,7,9]],axis=1)                    #These columns are not the RDF values
    RefinedContentNames[i].columns=range(RefinedContentNames[i].columns.size)
    #print(RefinedContentNames[i].head(20))
    #print("___________________________________________________")

FinalCSV=RefinedContentNames[0][0]

for i in range(0,NumberofColumns-1):
    TempoFiles.append("File_" + str(i+1))
    TempoFiles[i]=RefinedContentNames[i][0]
    TempoFilesAgain.append("File_" + str(i+1)+ "_Again")
    for j in range(0,NumberofFiles):
        TempoFiles[i]=pd.concat([TempoFiles[i],RefinedContentNames[j][i+1].reindex(TempoFiles[i].index)], axis=1)
    TempoFiles[i].columns=range(TempoFiles[i].columns.size)
    TempoFilesAgain[i]=TempoFiles[i].drop(TempoFiles[i].columns[0],axis=1)
    TempoFilesAgain[i].columns=range(TempoFilesAgain[i].columns.size)
    #print(TempoFilesAgain[i].head(20))
    #print("__________________________")
    FinalCSV=pd.concat([FinalCSV,TempoFilesAgain[i].mean(axis=1).reindex(TempoFiles[i].index)], axis=1)
FinalCSV.columns=range(FinalCSV.columns.size)
print("Done")
print(FinalCSV.head(20))
FinalCSV.to_csv(IndividualMeans, sep='\t', header=False, index=False)
############################################################################################
print("Done")


##################################################################################
#Add or Remove the number of curves depending on youe system under Investigation
DataPlot=np.genfromtxt(IndividualMeans,delimiter='\t')
X=DataPlot[:,0]
Y1=DataPlot[:,1]
Y2=DataPlot[:,2]
Y3=DataPlot[:,3]

#Plotting Section
plt.plot(X,Y1,c='red',marker='o',label="Cation-Cation")
plt.plot(X,Y2,c='blue',marker='o',label="Anion-Anion")
plt.plot(X,Y3,c='green',marker='o',label="Cation-Anion")
plt.title("Radial Distribution Function")
plt.legend(scatterpoints=1)
plt.xlabel("r [Angstrom]");plt.ylabel("g(r)")
plt.savefig(PlotNameSaved)
#################################################################################

