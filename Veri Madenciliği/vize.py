import numpy as np
import pandas as pd
from pytictoc import TicToc
# import os
#author Zeynep Acar

# currentDirectory = os.getcwd()
# parentDirectory = os.path.dirname(currentDirectory) + "/Veri Madenciliği" 
#filePath = parentDirectory + "/Datasets" + "/FIMdata10A.xlsx"
filePath = r"C:\Users\bernv\OneDrive\Masaüstü\onlus.xlsx"


MinSupp = 8 #burasını hoca vericek sık öğe seti için olacak 
# 131 . kurallar için gerekecek
#rules için conf yazana bakacağız

df = pd.read_excel(filePath, header=None)
numOfTransactions = df.shape[0]
allItems = []
for row in np.array(df):
    for item in row[0].split(', '):
        if item not in allItems:
            allItems.append(item)
            
numOfUniqueItems = len(allItems)
allItems.sort()
print(allItems)

counts = {}
for key in allItems:
    counts[key] = 0

maxTransactionLength = 0
totalNumOfItems = 0
for row in np.array(df):
    totalNumOfItems += len(row[0].split(', '))
    if len(row[0].split(', ')) > maxTransactionLength:
        maxTransactionLength = len(row[0].split(', '))
    for item in row[0].split(', '):
        counts[item] += 1
averageLengthOfTransactions = totalNumOfItems/numOfTransactions
density = averageLengthOfTransactions/numOfUniqueItems
print("numOfTransactions............", numOfTransactions)           
print("numOfUIniqueItems............", numOfUniqueItems)
print("maxTransactionLength.........", maxTransactionLength)            
print("avarageLengthOfTransactions...",averageLengthOfTransactions)
print("density......................",density)
for item in allItems:
    print(item, ' :',counts[item])
print("_________Finding Frequent Itemsets________")    
DATABASE = np.zeros((numOfTransactions,numOfUniqueItems),dtype = "int8")
i = -1    
for row in np.array(df):
    i+=1
    for item in row[0].split(', '):
        j = allItems.index(item)
        DATABASE[i,j] = 1 

ElapsedTime = TicToc()
ElapsedTime.tic()
# ----------------------------------------------        
# ----------------------------------------------
def CandidateGeneration_Serdar(Fk,numOfUniqueItems):
    Ck = []
    for i in range(0,len(Fk)):
        itemset1 = list(Fk[i])
        lastelement = itemset1[-1]
        for item2 in range(lastelement+1,numOfUniqueItems):
            xxxx = list(itemset1)
            xxxx.append(item2)
            Ck.append(xxxx)
    return Ck
# ----------------------------------------------
# ----------------------------------------------
def CandidateGeneration_Apriori(Fk, numOfUniqueItems):
    Ck = []
    for i in range(0,len(Fk)-1):
        itemset1 = list(Fk[i])
        rem1 = itemset1[1:]
        for j in range(i+1,len(Fk)):
            itemset2 = list(Fk[j])
            rem2 = itemset2[:-1]
            if rem1 == rem2:
                xxxx = list(itemset1)
                xxxx.append(itemset2[-1])
                Ck.append(xxxx)
    return Ck
# ---------------------------------------------    
def findSupport(itemset, DATABASE):
    supportOfItemset = sum(np.prod(DATABASE[:,itemset], axis = 1))
    return supportOfItemset
# ----------------------------------------------
# ----------------------------------------------
I = np.nonzero(MinSupp <= np.array(list(counts.values())))[0]
uniqueItems = [allItems[i] for i in I]
DATABASE = DATABASE[:,I]
SUPPORTS = list(np.array(list(counts.values()))[I])
FREQUENTITEMSETS = {}
NUMERICAL_FREQUENTITEMSETS = []
for item, support in zip(uniqueItems,SUPPORTS):
    # print(item,support)
    FREQUENTITEMSETS['['+item+']'] = support
    NUMERICAL_FREQUENTITEMSETS.append([I[uniqueItems.index(item)]])
numOfUniqueItems = len(uniqueItems)
Fk = [ [i] for i in range(0,numOfUniqueItems)]
# ----------------------------------------------
while len(Fk) > 0:
    Ck = CandidateGeneration_Serdar(Fk, numOfUniqueItems)
    Fk = []
    for itemset in Ck:
        support = findSupport(itemset, DATABASE)
        if MinSupp <= support:
            Fk.append(itemset)
            item = "["
            for itm in itemset:
                item += uniqueItems[itm] + " / "
            item = item[:-3] + "]"
            FREQUENTITEMSETS[item] = support
            NUMERICAL_FREQUENTITEMSETS.append(list(I[itemset]))
            SUPPORTS.append(support)
# ---------------------------------------------
i = 0
for key in FREQUENTITEMSETS.keys():
    i += 1
    print("#", str(i), ".....", key, "..... absolute support: ", str(FREQUENTITEMSETS[key]))
# ---------------------------------------------
print("________Finding Association Rules ________") 
def numerical2string(numericalFI):
    string = "["
    for item in numericalFI:
        string += allItems[item] + ', '
    string = string[:-2] + ']'
    return string

minconf = 0.5 #burasını da hoca vericek
import itertools
SUPPORTS = [supp/numOfTransactions for supp in SUPPORTS]
for frequentitemset, supportXY in zip(NUMERICAL_FREQUENTITEMSETS, SUPPORTS):
    if len(frequentitemset) > 1:
        for L in range(1, len(frequentitemset)):
            for antecedent in itertools.combinations(frequentitemset, L):
                antecedent = list(antecedent)
                antecedent.sort
                consequent = list(set(frequentitemset) - set(antecedent))
                consequent.sort()
                # print(frequentitemset.antecedent.consequent)
                supportX = SUPPORTS[NUMERICAL_FREQUENTITEMSETS.index(antecedent)]
                supportY = SUPPORTS[NUMERICAL_FREQUENTITEMSETS.index(consequent)]
                confXY = supportXY / supportX
                inteXY = abs(supportXY - supportX * supportY)
                liftXY = supportXY / (supportX*supportY)
                kulcXY = 0.5*(supportXY/supportX + supportXY/supportY)
                if minconf <= confXY:
                    if 0 < inteXY:
                        print(numerical2string(antecedent), '--->',numerical2string(consequent), 'supp.: ', supportXY ,'conf.: ',confXY ,'inte.: ',inteXY ,'lift: ',liftXY, 'kulc.: ', kulcXY)
    print('--------------------------------------------------------------------------------------')
# ---------------------------------------------
ElapsedTime.toc("Geçen zaman...")