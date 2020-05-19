#Modules
import os
import csv
#Open dataset
csvpath=os.path.join("Resources","budget_data.csv")

#Tipo de csv
totalm=0
totalavr=0
maxtotal=0
mintotal=10000000
totalp=[]

with open(csvpath) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    Lista=list(csvreader)
    mes=len(Lista)
    #print(mes)
    totalpf=float(Lista[0][1])
    for i in range(1,mes):
        current=float(Lista[i][1])
        past=float(Lista[i-1][1])
        totalpf=current+totalpf
        total=current-past
        totalp.append(total)
        totalavr=totalavr+total
        if total>maxtotal:
            maxtotal=total
        if total<mintotal:
            mintotal=total
            
Totalprofit=totalpf
avr=totalavr/(mes-1)
max1=maxtotal
min1=mintotal

print("Financial Analysis")
print("----------------------------")
print(F'Total months: {mes}')
print(F'Total net profit: {Totalprofit}')
print(F'Greatest Increase in Profits: {max1}')
print(F'Greatest Decrease in Profits: {min1}')


L=['Financial Analysis\n',
    '----------------------------\n',
    F'Total months: {mes}\n',
    F'Total net profit: {Totalprofit}\n',
    F'Greatest Increase in Profits: {max1}\n',
    F'Greatest Decrease in Profits: {min1}\n']


output_file=os.path.join("Resources","HW3.txt")
with open(output_file,"w") as datafile:
    datafile.writelines(L)
