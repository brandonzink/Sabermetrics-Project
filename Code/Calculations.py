import numpy as np
import matplotlib.pylab as plt
import pandas as pd

#Set to 1 to use the test file instead of the full one, faster excecution
test = 1

#Return the RE24 expected run value for a given out/base situation
#first/second/third should be 1 if runner on, else 0
def RE24_lookup(outs, first, second, third):
    
    if outs == 0:
        if (first == 0 and second == 0 and third == 0): #No one on
            return 0.481
        if (first == 1 and second == 0 and third == 0): #First
            return 0.859
        if (first == 0 and second == 1 and third == 0): #Second
            return 1.1
        if (first == 1 and second == 1 and third == 0): #First, second
            return 1.437
        if (first == 0 and second == 0 and third == 1): #Third
            return 1.35
        if (first == 1 and second == 0 and third == 1): #First, third
            return 1.784
        if (first == 0 and second == 1 and third == 1): #Second, third
            return 1.964
        if (first == 1 and second == 1 and third == 1): #Bases loaded
            return 2.292

    elif outs == 1:
        if (first == 0 and second == 0 and third == 0): #No one on
            return 0.254
        if (first == 1 and second == 0 and third == 0): #First
            return 0.509
        if (first == 0 and second == 1 and third == 0): #Second
            return 0.664
        if (first == 1 and second == 1 and third == 0): #First, second
            return 0.884
        if (first == 0 and second == 0 and third == 1): #Third
            return 0.95
        if (first == 1 and second == 0 and third == 1): #First, third
            return 1.13
        if (first == 0 and second == 1 and third == 1): #Second, third
            return 1.376
        if (first == 1 and second == 1 and third == 1): #Bases loaded
            return 1.541

    else: #2 outs
        if (first == 0 and second == 0 and third == 0): #No one on
            return 0.098
        if (first == 1 and second == 0 and third == 0): #First
            return 0.224
        if (first == 0 and second == 1 and third == 0): #Second
            return 0.319
        if (first == 1 and second == 1 and third == 0): #First, second
            return 0.429
        if (first == 0 and second == 0 and third == 1): #Third
            return 0.353
        if (first == 1 and second == 0 and third == 1): #First, third
            return 0.478
        if (first == 0 and second == 1 and third == 1): #Second, third
            return 0.58
        if (first == 1 and second == 1 and third == 1): #Bases loaded
            return 0.752

#Calculates the REC (Runs Expected Change) as described in the writeup
#pre/post first, second, and third should be 1 if runner on, else 0
def REC_calculation(pre_outs, pre_first, pre_second, pre_third, post_outs, post_first, post_second, post_third, runs_scored):
    
    #Get the before and after expected run values
    pre_REC = RE24_lokup(pre_outs, pre_first, pre_second, pre_third)
    post_REC = RE24_lookup(post_outs, post_first, post_second, post_third)

    #Calculate and return the REC value
    REC = (post_REC - pre_REC) + runs_scored
    return REC

#Calculates total bases advanced, the numerator for the %TBA calculation
#batter, first, second, third fate should correspond to the base they end up at, 0 if runner DNE
def TBA(batter_fate, first_fate, second_fate, third_fate):
    
    #Keeps track of total bases
    TBA = 0
    
    #Calculate TBA if the runner exists
    TBA += batter_fate
    if first_fate != 0:
        TBA += first_fate - 1
    if second_fate != 0:
        TBA += second_fate - 2
    if third_fate != 0:
        TBA += third_fate - 3

    return TBA

#Calculate the total possible bases advanced, the denominator for the %TBA calculation
#first, seond, thirdshould be 1 if exists, else 0
def TPBA(first, second, third):
    TBA = 4 + (first*3) + (second*2) + (third*3)
    return TBA

#Changes the baserunners to a 1/0 boolean instaed of the baserunnerID, returns a dataframe
def bool_baserunners(df):
    df['1B_Runner'] = np.where(df['1B Runner'].isnull(), 0, 1)
    df['2B_Runner'] = np.where(df['2B Runner'].isnull(), 0, 1)
    df['3B_Runner'] = np.where(df['3B Runner'].isnull(), 0, 1)
    df = df.drop(['1B Runner', '2B Runner', '3B Runner'], axis = 1)
    return df

#Reads the csv files, returns a dataframe
def read_in_data():
    global test

    if test == 1:
        return pd.read_csv('baseStatsTest.csv')
    else:
        return pd.read_csv('baseStats.csv')


def main():
    #Get the data
    BaseDF = read_in_data()
    #Get boolean values instead of baserunner ID
    BaseDF = bool_baserunners(BaseDF)

    print(BaseDF.head(20))
    


main()