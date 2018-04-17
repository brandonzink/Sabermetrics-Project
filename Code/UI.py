import numpy as np
import matplotlib.pylab as plt
import pandas as pd

qualifier = 50

#Prints the top num %TBA player with the qualifier
def top_perTBA_seasons(data, num, qualifier):
    
    #Tracks the number of names printed
    tracker = 0
    
    #Sorts the data by %TBA
    data = data.sort_values('%TBA', ascending = False)

    #Loops through and prints the top num values
    print('##############################################')
    print('NAME \t\t\t YEAR \t AB \t %TBA')
    print('----------------------------------------------')
    for i, row in data.iterrows():
        if row['Qual. AB'] > qualifier:
            print(row['NAME'][:13],'\t\t',row['Year'],'\t',row['Qual. AB'],'\t',round(row['%TBA'], 3))
            tracker += 1
        if tracker == num:
            print('##############################################')
            print('')
            return

    return

#Prints the top num REC player with the qualifier
def top_REC_seasons(data, num, qualifier):
    #Tracks the number of names printed
    tracker = 0
    
    #Sorts the data by %TBA
    data = data.sort_values('REC', ascending = False)

    #Loops through and prints the top num values
    print('################################################')
    print('NAME \t\t\t YEAR \t AB \t REC')
    print('------------------------------------------------')
    for i, row in data.iterrows():
        if row['Qual. AB'] > qualifier:
            print(row['NAME'][:13],'\t\t',row['Year'],'\t',row['Qual. AB'],'\t',round(row['REC'], 3))
            tracker += 1
        if tracker == num:
            print('################################################')
            print('')
            return

    return

#Scatterplot of %TBA v ABs
def perTBA_v_AB(data, qualifier):
    #Plot vertical line at qualifier with text
    plt.axvline(x=qualifier, c='r')
    plt.text(qualifier+10,1,'Current Qualifying AB Level',rotation=90)
    #Plot scatterplot
    plt.scatter(data['Qual. AB'], data['%TBA'], s=2)
    #Labels
    plt.ylabel('%TBA')
    plt.xlabel('ABs')
    plt.title('%TBA v. # of ABs')

    plt.show()
    return

#Scatterplot of REC v ABs
def REC_v_AB(data, qualifier):
    #Plot vertical line at qualifier with text
    plt.axvline(x=qualifier, c='r')
    plt.text(qualifier+10,150,'Current Qualifying AB Level',rotation=90)
    #Plot scatterplot
    plt.scatter(data['Qual. AB'], data['REC'], s=2)
    #Labels
    plt.ylabel('REC')
    plt.xlabel('ABs')
    plt.title('REC v. # of ABs')

    plt.show()
    return

#Scatterplot of %TBA v REC
def perTBA_v_REC(data):
    #Plot scatterplot
    plt.scatter(data['%TBA'], data['REC'], s=2)
    #Labels
    plt.ylabel('REC')
    plt.xlabel('%TBA')
    plt.title('REC v %TBA')

    plt.xlim(0,0.6)

    plt.show()
    return

#Plots side by side boxplots for each year of %TBA
def perTBA_by_year(data):
    data.boxplot(column=['%TBA'], by='Year')
    plt.show()

#Plots side by side boxplots for each year of %TBA
def REC_by_year(data):
    data.boxplot(column=['REC'], by='Year')
    plt.show()

#Print the menu, takes user inputs, and calls appropriate functions.
def menu(data):

    global qualifier

    user_options = ['0: Exit',
    '1: Top X %TBA seasons with qualifier',
    '2: Top X REC seasons with qualifier',
    '3: Change qualifier value',
    '4: Graph of %TBA v. Qualifying ABs',
    '5: Graph of REC v. Qualifying ABs',
    '6: Graph of %TBA v. REC',
    '7: Graph of %TBA by year',
    '8: Graph of REC by year',
    '9: Explanation of %TBA',
    '10: Explanation of REC']

    #Prints options, gets user inputs
    print('[ MENU ]')
    for i in range(0,len(user_options)):
        print(user_options[i])
    option = input("> ")

    #Catches if the input is not an int
    if option.isdigit() == False:
        print('Invalid option. Please try again.')
        print('')
        menu(data)

    if int(option) == 0:
        return

    elif int(option) == 1:
        option = int(input('How many top %TBA players would you like: > '))
        top_perTBA_seasons(data, option, qualifier)

    elif int(option) == 2:
        option = int(input('How many top REC players would you like: > '))
        top_REC_seasons(data, option, qualifier)

    elif int(option) == 3:
        qualifier = int(input('New qualifying ABs number: >'))

    elif int(option) == 4:
        perTBA_v_AB(data, qualifier)

    elif int(option) == 5:
        REC_v_AB(data, qualifier)

    elif int(option) == 6:
        perTBA_v_REC(data)

    elif int(option) == 7:
        perTBA_by_year(data)

    elif int(option) == 8:
        REC_by_year(data)

    else:
        print('Invalid option. Please try again.')
        print('')

    menu(data)









def main():
    StatsDF = pd.read_csv('AdvancedBaseStats.csv')
    menu(StatsDF)

main()
