import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro 


def display_mean(dfField):
    myField=dfField.copy()
    myField.dropna()
    try:
        mean_value=myField.mean()
        print("The mean of this feature is: "+str(mean_value))
    except TypeError:
        print("The mean is not defined in categorical data")


def display_median(dfField):
    myField=dfField.copy()
    myField.dropna()
    try:
        median_value=myField.median()
        print("The median of this feature is: "+str(median_value))
    except TypeError:
        print("The median is not defined in categorical data")

def display_mode(dfField):
    myCounts = dfField.value_counts()
    maxCount = myCounts.max()
    modes = []
    for i in range(len(myCounts)):
        if myCounts.values[i]==maxCount:
            modes = np.append(modes, myCounts.index[i])
    
    if len(modes)==len(myCounts):
        modes = ['no mode']
    print("The mode or modes of this feature is: ")
    for i in modes:
        print(modes)
        
    return modes

def display_var(dfField):
    print("Displaying the variation of this feature: ")
    try:
        print(dfField.var())
    except TypeError:
        print("There is no variation in categorical variables")

def display_std(dfField):
    print("Displaying the standard deviation of this feature: ")
    try:
        print(dfField.std())
    except TypeError:
        print("There is no standard deviation in categorical variables")
    
def display_distribution(dfField):
    try:
        res=shapiro(dfField)
        if (res.pvalue<.05):
            print("The shapiro test indicates that the datataset does not follow normal distribution")
        else:
            print("The dataset may follow normal distribution")
        plt.hist(dfField, edgecolor='black', bins=20)
        plt.show()
    except TypeError:
        print("Can't determine the distribution of categorical variables")  

def descriptive_stats(dataframe):
    print("Displaying the basic statistics of the dataframe:")
    print(dataframe.describe())
    
 
        
    

def display_correlation(dataframe):
    numeric_df=dataframe.copy()
    numeric_df=numeric_df.select_dtypes(['number'])
    corr_matrix = numeric_df.corr()
    plt.figure(figsize=(15, 10))
    sns.heatmap(corr_matrix, annot=True, linewidths=0.5,fmt= ".2f", cmap="YlGnBu");
    plt.show()










if __name__ == "__main__":
    dataset=input("Please enter the name of your dataset file: ")
    myDf = pd.read_csv(dataset,low_memory=False)
    print("The first 5 records of the dataset are:")
    print(myDf.head())
    print("----------------------------------------------")
    descriptive_stats(myDf)
    print("----------------------------------------------")
    print("To display the mean,median,variance and the standard deviation of a feature press 1")
    print("To display the distribution of a feature press 2")
    print("To display the correlation between the numeric features press 3")
    print("To exit press any other symbol")
    print("----------------------------------------------")
    choice=input("Please enter a number: ")
    while(True):
        if (choice=="1"):
            print("Choose one of the following columns:")
            print(myDf.columns)
            dfField=input("Please enter the name of the column here: ")
            display_mean(myDf[dfField])
            display_median(myDf[dfField])
            display_mode(myDf[dfField])
            display_var(myDf[dfField])
            display_std(myDf[dfField])
        elif (choice=="2"):
            print("Choose one of the following columns:")
            print(myDf.columns)
            dfField=input("Please enter the name of the column here: ")
            display_distribution(myDf[dfField])
        elif (choice=="3"):
            display_correlation(myDf)
        else:
            print("Good,bye!")
            break
        print("----------------------------------------------")
        print("To display the mean,median,variance and the standard deviation of a feature press 1")
        print("To display the distribution of a feature press 2")
        print("To display the correlation between the numeric features press 3")
        print("To exit press any other symbol")
        print("----------------------------------------------")
        choice=input("Please enter a number: ")
        
