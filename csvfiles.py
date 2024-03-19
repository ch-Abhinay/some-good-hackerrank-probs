import csv
import random
import matplotlib.pyplot as plt
a=[  ['Chocolate', 'Vanilla', 'Coffee'],
  ['N/A'],
  ['Coffee', 'Strawberry', 'Chocolate'],
  ['Mint Chocolate Chip', 'Cookies and Cream', 'Vanilla'],
  ['Butter Pecan', 'Chocolate', 'Cookie Dough'],
  ['Rocky Road', 'Vanilla', 'Pistachio'],
  ['Coffee', 'Mint Chocolate Chip', 'Chocolate'],
  ['Chocolate Chip Cookie Dough', 'Vanilla', 'Strawberry'],
  ['Pistachio', 'Chocolate', 'Vanilla'],
  ['Neapolitan', 'Chocolate', 'Vanilla'],
  ['Cookie Dough', 'Chocolate', 'Vanilla'],
  ['Salted Caramel', 'Chocolate', 'Vanilla'],
  ['Cherry Garcia', 'Chocolate', 'Vanilla'],
  ['Peanut Butter', 'Chocolate', 'Vanilla'],
  ['Mango', 'Chocolate', 'Vanilla'],
  ['Strawberry Cheesecake', 'Chocolate', 'Vanilla'],
  ['Coconut', 'Chocolate', 'Vanilla'],
  ['Dulce de Leche', 'Chocolate', 'Vanilla'],
  ['Raspberry Ripple', 'Chocolate', 'Vanilla'],
  ['Maple Walnut', 'Chocolate', 'Vanilla'],
  ['Black Cherry', 'Chocolate', 'Vanilla'],
  ['Bubblegum', 'Chocolate', 'Vanilla'],
  ['Lemon Sorbet', 'Chocolate', 'Vanilla'],
  ['Red Velvet', 'Chocolate', 'Vanilla'],
  ['Caramel Swirl', 'Chocolate', 'Vanilla'],
  ['Orange Creamsicle', 'Chocolate', 'Vanilla'],
  ['Pistachio Almond', 'Chocolate', 'Vanilla'],
  ['Blueberry', 'Chocolate', 'Vanilla'],
  ['Rocky Mountain Road', 'Chocolate', 'Vanilla'],
  ['Tiramisu', 'Chocolate', 'Vanilla'],
  ['N/A'],
  ['Lactose Intolerant'],
  ['Vanilla', 'Chocolate', 'Coffee'],
  ['N/A'],
  ['Coffee', 'Strawberry', 'Chocolate'],
  ['Mint Chocolate Chip', 'Cookies and Cream', 'Vanilla'],
  ['Butter Pecan', 'Chocolate', 'Cookie Dough'],
  ['Rocky Road', 'Vanilla', 'Pistachio'],
  ['Coffee', 'Mint Chocolate Chip', 'Chocolate'],
  ['Chocolate Chip Cookie Dough', 'Vanilla', 'Strawberry'],
  ['Pistachio', 'Chocolate', 'Vanilla'],
  ['Neapolitan', 'Chocolate', 'Vanilla'],
  ['Cookie Dough', 'Chocolate', 'Vanilla'],
  ['Salted Caramel', 'Chocolate', 'Vanilla'],
  ['Cherry Garcia', 'Chocolate', 'Vanilla'],
  ['Peanut Butter', 'Chocolate', 'Vanilla'],
  ['Mango', 'Chocolate', 'Vanilla'],
  ['Strawberry Cheesecake', 'Chocolate', 'Vanilla'],
  ['Coconut', 'Chocolate', 'Vanilla'],
  ['Dulce de Leche', 'Chocolate', 'Vanilla'],
  ['Raspberry Ripple', 'Chocolate', 'Vanilla'],
  ['Maple Walnut', 'Chocolate', 'Vanilla'],
  ['Black Cherry', 'Chocolate', 'Vanilla'],
  ['Bubblegum', 'Chocolate', 'Vanilla'],
  ['Lemon Sorbet', 'Chocolate', 'Vanilla'],
  ['Red Velvet', 'Chocolate', 'Vanilla'],
  ['Caramel Swirl', 'Chocolate', 'Vanilla'],
  ['Orange Creamsicle', 'Chocolate', 'Vanilla'],
  ['Pistachio Almond', 'Chocolate', 'Vanilla'],
  ['Blueberry', 'Chocolate', 'Vanilla']
]
preferences=[]
for i in a:
    if len(i)!=1:
        temp=[]
        for j in range(len(i)):
            cal=i[j].lower()
            temp.append(cal)
        preferences.append(temp)
with open('survey001.csv','w') as csvfile:
    writer= csv.writer(csvfile)
    writer.writerow(['person', 'preferences'])
    for i in range(0,len(preferences)):
        writer.writerow(['person'+str(i+1),preferences[i]])
with open('survey001.csv','r') as csvfile:
    reader= csv.reader(csvfile)
    for row in reader:
        print(row)
        pass
#print(preferences)
data={}
flavores=[]
for i in preferences:
    if len(i)!=1:
        for j in i:
            if j not in flavores:
                flavores.append(j)
            if j not in data.keys():
                data[j]=1
            else:
                data[j]+=1
print(flavores)
prob={}
for i in flavores:
    for j in flavores:
        for k in preferences:
            if k[0]==i and k[1]==j:
                prob[i,j]=[k[2]]
fice=input('your 1st preference from the above flavours of ice cream').lower()
sice=input('your 2nd preference from the above flavours of ice cream').lower()
temp= False
for i in prob.keys():
    #print(i)
    if i[0]==fice and i[1]==sice:
        print(prob[fice,sice])
        temp= True
        break
if temp== False:
    print(random.choice(flavores))
print(data)
