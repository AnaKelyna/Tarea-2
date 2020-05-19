#Modules
import os
import csv
#Open dataset
csvpath=os.path.join("Resources","election_data.csv")

#Tipo de csv
with open(csvpath) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    Lista=list(csvreader)
    Totalvotes=len(Lista)

    candidates=[]
    Khan=0
    Correy=0
    Li=0 
    OTooley=0
    for i in range(0,Totalvotes):
        Candidate=Lista[i][2]
        if Candidate not in candidates:
            candidates.append(Candidate)
        if Candidate=="Khan":
            Khan=Khan+1
        if Candidate=="Correy":
            Correy=Correy+1
        if Candidate=="Li":
            Li=Li+1
        if Candidate=="O'Tooley":
            OTooley=OTooley+1

    per_Khan=float(Khan/Totalvotes)
    per_Correy=float(Correy/Totalvotes)
    per_Li=float(Li/Totalvotes)
    per_OTooley=float(OTooley/Totalvotes)
    
    winner=[]

    if Khan>Correy>Li>OTooley:
        winner="Kahn"
    if Correy>Khan>Li>OTooley:
        winner="Correy"
    if Li>Khan>Correy>OTooley:
        winner="Li"
    if OTooley>Khan>Correy>Li:
        winner="O'Tooley"


print("Election Results")
print("----------------------------")
print(F'Total votes:{Totalvotes}')
print("----------------------------")
print(F'Kahn:{"{:.2%}".format(per_Khan)} ({Khan})')
print(F'Correy:{"{:.2%}".format(per_Correy)} ({Correy})')
print(F'Li:{"{:.2%}".format(per_Li)} ({Li})')
print(F'OTooley:{"{:.2%}".format(per_OTooley)} ({OTooley})')
print("----------------------------")
print(F'Winner: {winner}')

L=['Election Results\n',
    '----------------------------\n',
    F'Total votes:{Totalvotes}\n',
    '----------------------------\n',
    F'Kahn:{"{:.2%}".format(per_Khan)} ({Khan})\n',
    F'Correy:{"{:.2%}".format(per_Correy)} ({Correy})\n',
    F'Li:{"{:.2%}".format(per_Li)} ({Li})\n',
    F'OTooley:{"{:.2%}".format(per_OTooley)} ({OTooley})\n',
    '----------------------------\n',
    F'Winner: {winner}\n']



output_file=os.path.join("Resources","HW3-2.txt")
with open(output_file,"w") as datafile:
    datafile.writelines(L)

