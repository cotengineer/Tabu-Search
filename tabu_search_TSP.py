# -*- coding: utf-8 -*-

import csv
import random
import time
import copy
import matplotlib.pyplot as plt

start = time.time()

#initialize distance matrix
cities = []

#initialize counter
t = 0

#import data
with open("TSP29.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        #variable generator
        cities.append(row)
        
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
random.shuffle(x)

#tabu list
tabu = []

#evaluation function  
def F(x):
    
    xc = [cities[x[0]][x[1]],cities[x[1]][x[2]],cities[x[2]][x[3]],
          cities[x[3]][x[4]],cities[x[4]][x[5]],cities[x[5]][x[6]],
          cities[x[6]][x[7]],cities[x[7]][x[8]],cities[x[8]][x[9]],
          cities[x[9]][x[10]],cities[x[10]][x[11]],cities[x[11]][x[12]],
          cities[x[12]][x[13]],cities[x[13]][x[14]],cities[x[14]][x[15]],
          cities[x[15]][x[16]],cities[x[16]][x[17]],cities[x[17]][x[18]],
          cities[x[18]][x[19]],cities[x[19]][x[20]],cities[x[20]][x[21]],
          cities[x[21]][x[22]],cities[x[22]][x[23]],cities[x[23]][x[24]],
          cities[x[24]][x[25]],cities[x[25]][x[26]],cities[x[26]][x[27]],
          cities[x[27]][x[28]],cities[x[28]][x[0]]]
    
    #convert string data from excel to integer to work with easier
    x_con = []
    for c in range(0,29):
        x_con.append(int(xc[c]))
        
    return(sum(x_con))

#sorting function
def getKey(item):
    return(item[0])

#current best    
CB = F(x)
fit = [CB]
   
print("Initial Tour:",x)
print("Initial Evaluation:",CB)

bx = copy.copy(x)
Global = 10000

while t < 300:
    #best of iteration
    IB = 10000
    
    #find best neighbor move for each iteration
    for i in range(0,29):
        for j in range(0,29):
            pair = i,j

            #tabu search neighborhood
            if (pair not in tabu) and (i != j):
                x1 = x        
                x1[i],x1[j] = x1[j],x1[i]
                
                if IB >= F(x1):
                    IB = F(x1)
                    bpair_f = i,j
                    bpair_b = j,i
                    bx = x1
            
            #aspiration criteria
            elif (pair in tabu) and (i != j):
               
                if (IB * 0.5 > F(x1)):
                    bx = x1
                    bpair_f = i,j
                    bpair_b = j,i
                    IB = F(x1)
                    
    x = bx   
    if (bpair_f not in tabu) and (bpair_b not in tabu):     
        tabu.append(bpair_f)
        tabu.append(bpair_b)
    fit.append(IB)
    while len(tabu) > 30:
        tabu.pop(0)
    if IB < Global:
        fx = x
        Global = IB

    t += 1

###############################################
end = time.time()

print("Final Evaluation:",Global)
print("Final Route",fx)
print("")
print("Finished in:", end-start)

plt.plot(fit)
plt.title('Tabu Search for TSP',fontsize=18,color='r')
plt.xlabel('Sequence',fontsize=14,color='b')
plt.ylabel('Distance',fontsize=14,color='b')
plt.grid()
plt.show()


