import sklearn as sk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import numpy as np
import tkinter as tk
from PIL import ImageTk,Image

#Realise modern machine learning doesn't require good math because it's all programmed into libraries already thanks sklearn so deleted last 20 lines of code and R

#import data with pandas no header
data = pd.read_csv('agaricus-lepiota.data', sep = ',', header = None)
#print(data) shows column start from 0 to 22

#use one hot encoder to create dummy variables for amount of different items in a column -1
onehotencoder = OneHotEncoder(handle_unknown='ignore')
labelencoder = LabelEncoder()

#use label encoder for y value as its either poisonous or not eg, binary no dummy variable needed
#the .iloc thing is to select the columns with the data because column 0 has the y values of poisonous or not
y = labelencoder.fit_transform(data[0])
x = onehotencoder.fit_transform(data.iloc[:,1:23]).toarray()

#transpose columns to rows
y = y.T

#split x and y vars into x_train, x_test, y_train, y_test vars with randomly selected data for each at a chosen ratio of 20% test 80% train
#done using sklearn train_test_split
#random state is 42 because hitch hikers guide says so (it is a seed to generate reproducible splitting of data)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

#now there are 4 data sets x_train x_test y_train y_test
#this is the part which killed the statisticians job in ML, just pick the machine learning module which best fits the data type eg , binary classification in this case
#use the Naive Bayes module

#initiate classifier
gnb = GaussianNB()
#train classifier with my PHD in math
gnb.fit(x_train, y_train)

#now with the model trained compare its predicitons with the test data
#print(accuracy_score(y_test, pred))
#96% accuracy

#function for the submit button to predict mushroom edibility based on trained data
def b1():
    #teemo image
    imgpoi = ImageTk.PhotoImage(Image.open('poisonous.jpg'))
    imggood = ImageTk.PhotoImage(Image.open('good.jpg'))

    inputdict = {

        'Bell': 'b',
        'Conical': 'c',
        'Convex': 'x',
        'Flat': 'f',
        'Knobbed': 'k',
        'Sunken': 's',
        'Fibrous': 'f',
        'Grooves': 'g',
        'Scaly': 'y',
        'Smooth': 's',
        'Brown': 'n',
        'Buff': 'b',
        'Cinnamon': 'c',
        'Grey': 'g',
        'Green': 'r',
        'Pink': 'p',
        'Purple': 'u',
        'Red': 'e',
        'White': 'w',
        'Yellow': 'y',
        'True': 't',
        'False': 'f',
        'Almond': 'a',
        'Anise': 'l',
        'Creosote': 'c',
        'Fishy': 'y',
        'Foul': 'f',
        'Musty': 'm',
        'Pungent': 'p',
        'Spicy': 's',
        'None': 'n',
        'Attached': 'a',
        'Descending': 'd',
        'Free': 'f',
        'Notched': 'n',
        'Close': 'c',
        'Crowded': 'w',
        'Distant': 'd',
        'Broad': 'b',
        'Narrow': 'n',
        'Black': 'k',
        'Chocolate': 'h',
        'Orange': 'o',
        'Enlarging': 'e',
        'Tapering': 't',
        'Bulbous': 'b',
        'Club': 'c',
        'Cup': 'u',
        'Equal': 'e',
        'Rhizomorphs': 'z',
        'Rooted': 'r',
        'Missing': '?',
        'Silky': 'k',
        'Partial': 'p',
        'Universal': 'u',
        'One': 'o',
        'Two': 't',
        'Cobwebby': 'c',
        'Evanescent': 'e',
        'Flaring': 'f',
        'Large': 'l',
        'Pendant': 'p',
        'Sheathing': 's',
        'Zone': 'z',
        'Abundant': 'a',
        'Clustered': 'c',
        'Numerous': 'n',
        'Scattered': 's',
        'Several': 'v',
        'Solitary': 'y',
        'Grasses': 'g',
        'Leaves': 'l',
        'Meadows': 'm',
        'Paths': 'p',
        'Urban': 'u',
        'Waste': 'w',
        'Woods': 'd'

    }

    arr = []

    arr.append(inputdict[input1.get()])
    arr.append(inputdict[input2.get()])
    arr.append(inputdict[input3.get()])
    arr.append(inputdict[input4.get()])
    arr.append(inputdict[input5.get()])
    arr.append(inputdict[input6.get()])
    arr.append(inputdict[input7.get()])
    arr.append(inputdict[input8.get()])
    arr.append(inputdict[input9.get()])
    arr.append(inputdict[input10.get()])
    arr.append(inputdict[input11.get()])
    arr.append(inputdict[input12.get()])
    arr.append(inputdict[input13.get()])
    arr.append(inputdict[input14.get()])
    arr.append(inputdict[input15.get()])
    arr.append(inputdict[input16.get()])
    arr.append(inputdict[input17.get()])
    arr.append(inputdict[input18.get()])
    arr.append(inputdict[input19.get()])
    arr.append(inputdict[input20.get()])
    arr.append(inputdict[input21.get()])
    arr.append(inputdict[input22.get()])

    # transpose data frame from column to row
    arr = pd.DataFrame(arr).T
    # encode use input
    arr_encoded = onehotencoder.transform(arr).toarray()
    b2 = tk.Button(window, text=gnb.predict(arr_encoded), command=b1)
    b2.grid(row=24, column =6)

    if gnb.predict(arr_encoded) == 1:
        img = tk.Label(window, image = imgpoi)
        img.photo = imgpoi
        img.place(x=300.,y = 20)
    elif gnb.predict(arr_encoded) == 0:
        img = tk.Label(window, image=imggood)
        img.photo = imggood
        img.place(x=300., y=20)

#use tkinter to make a gui

window = tk.Tk()
window.geometry('1000x800')
window.title("Mushroom Information")

#Qualatative data

input1 = tk.StringVar()
input2 = tk.StringVar()
input3 = tk.StringVar()
input4 = tk.StringVar()
input5 = tk.StringVar()
input6 = tk.StringVar()
input7 = tk.StringVar()
input8 = tk.StringVar()
input9 = tk.StringVar()
input10 = tk.StringVar()
input11 = tk.StringVar()
input12 = tk.StringVar()
input13 = tk.StringVar()
input14 = tk.StringVar()
input15 = tk.StringVar()
input16 = tk.StringVar()
input17 = tk.StringVar()
input18 = tk.StringVar()
input19 = tk.StringVar()
input20 = tk.StringVar()
input21 = tk.StringVar()
input22 = tk.StringVar()

#Catagory Titles

lb1 = tk.Label(window, text = 'Cap Shape', font=("Arial", 12))
lb1.grid(row=0)

lb2 = tk.Label(window, text = 'Cap Surface', font=("Arial", 12))
lb2.grid(row=1)

lb3 = tk.Label(window, text = 'Cap Color', font=("Arial", 12))
lb3.grid(row=2)

lb4 = tk.Label(window, text = 'Bruises', font=("Arial", 12))
lb4.grid(row=3)

lb5 = tk.Label(window, text = 'Odor', font=("Arial", 12))
lb5.grid(row=4)

lb6 = tk.Label(window, text = 'Gill Attachment', font=("Arial", 12))
lb6.grid(row=5)

lb7 = tk.Label(window, text = 'Gill Spacing', font=("Arial", 12))
lb7.grid(row=6)

lb8 = tk.Label(window, text = 'Gill Size', font=("Arial", 12))
lb8.grid(row=7)

lb9 = tk.Label(window, text = 'Gill Color', font=("Arial", 12))
lb9.grid(row=8)

lb10 = tk.Label(window, text = 'Stalk Shape', font=("Arial", 12))
lb10.grid(row=9)

lb11 = tk.Label(window, text = 'Stalk Root', font=("Arial", 12))
lb11.grid(row=10)

lb12 = tk.Label(window, text = 'Stalk Surface Above Ring', font=("Arial", 12))
lb12.grid(row=11)

lb13 = tk.Label(window, text = 'Stalk Surface Below Ring', font=("Arial", 12))
lb13.grid(row=12)

lb14 = tk.Label(window, text = 'Stalk Color Above Ring', font=("Arial", 12))
lb14.grid(row=13)

lb15 = tk.Label(window, text = 'Stalk Color Below Ring', font=("Arial", 12))
lb15.grid(row=14)

lb16 = tk.Label(window, text = 'Veil Type', font=("Arial", 12))
lb16.grid(row=15)

lb17 = tk.Label(window, text = 'Veil Color', font=("Arial", 12))
lb17.grid(row=16)

lb18 = tk.Label(window, text = 'Ring Number', font=("Arial", 12))
lb18.grid(row=17)

lb19 = tk.Label(window, text = 'Ring Type', font=("Arial", 12))
lb19.grid(row=18)

lb20 = tk.Label(window, text = 'Spore Print Color', font=("Arial", 12))
lb20.grid(row=19)

lb21 = tk.Label(window, text = 'Population When Picked', font=("Arial", 12))
lb21.grid(row=20)

lb22 = tk.Label(window, text = 'Habitat Where Found', font=("Arial", 12))
lb22.grid(row=21)

#Drop menus

drop1 = tk.OptionMenu(window, input1, 'Bell', 'Conical', 'Convex','Flat', 'Knobbed','Sunken')
drop1.grid(column=1, row=0)

drop2 = tk.OptionMenu(window, input2, 'Fibrous', 'Grooves', 'Scaly','Smooth')
drop2.grid(column=1, row=1)

drop3 = tk.OptionMenu(window, input3, 'Brown', 'Buff', 'Cinnamon', 'Grey', 'Green', 'Pink', 'Purple', 'Red', 'White', 'Yellow')
drop3.grid(column=1, row=2)

button = tk.Radiobutton(window, variable=input4, cursor = 'arrow', borderwidth = 4, activeforeground = 'light grey', text = 'True', value = 'True', tristatevalue=0)
button.grid(column=1,row=3)

button1 = tk.Radiobutton(window, variable=input4, cursor = 'arrow', borderwidth = 4, activeforeground = 'light grey', text = 'False', value = 'False', tristatevalue=0)
button1.grid(column=2,row=3)

drop5 = tk.OptionMenu(window, input5, 'Almond', 'Anise', 'Creosote', 'Fishy', 'Foul', 'Musty', 'Pungent', 'Spicy', 'None')
drop5.grid(column=1, row=4)

drop6 = tk.OptionMenu(window, input6, 'Attached', 'Descending', 'Free', 'Notched')
drop6.grid(column=1, row=5)

drop7 = tk.OptionMenu(window, input7, 'Close', 'Crowded', 'Distant')
drop7.grid(column=1, row=6)

drop8 = tk.OptionMenu(window, input8, 'Broad', 'Narrow')
drop8.grid(column=1, row=7)

drop9 = tk.OptionMenu(window, input9, 'Black', 'Brown', 'Buff', 'Chocolate', 'Grey', 'Green', 'Orange', 'Pink', 'Purple', 'Red', 'White', 'Yellow')
drop9.grid(column=1, row=8)

drop10 = tk.OptionMenu(window, input10, 'Enlarging', 'Tapering')
drop10.grid(column=1, row=9)

drop11 = tk.OptionMenu(window, input11, 'Bulbous', 'Club', 'Cup', 'Equal', 'Rhizomorphs', 'Rooted', 'Missing')
drop11.grid(column=1, row=10)

drop12 = tk.OptionMenu(window, input12, 'Fibrous', 'Scaly', 'Silky', 'Smooth')
drop12.grid(column=1, row=11)

drop13 = tk.OptionMenu(window, input13, 'Fibrous', 'Scaly', 'Silky', 'Smooth')
drop13.grid(column=1, row=12)

drop14 = tk.OptionMenu(window, input14, 'Brown', 'Buff', 'Cinnamon', 'Grey', 'Orange', 'Pink', 'Red', 'White', 'Yellow')
drop14.grid(column=1, row=13)

drop15 = tk.OptionMenu(window, input15, 'Brown', 'Buff', 'Cinnamon', 'Grey', 'Orange', 'Pink', 'Red', 'White', 'Yellow')
drop15.grid(column=1, row=14)

drop16 = tk.OptionMenu(window, input16, 'Partial', 'Universal')
drop16.grid(column=1, row=15)

drop17 = tk.OptionMenu(window, input17, 'Brown', 'Orange', 'White', 'Yellow')
drop17.grid(column=1, row=16)

drop18 = tk.OptionMenu(window, input18, 'None', 'One', 'Two')
drop18.grid(column=1, row=17)

drop19 = tk.OptionMenu(window, input19, 'Cobwebby', 'Evanescent', 'Flaring', 'Large', 'Pendant', 'Sheathing', 'Zone', 'None')
drop19.grid(column=1, row=18)

drop20 = tk.OptionMenu(window, input20, 'Black', 'Brown', 'Buff', 'Chocolate', 'Green', 'Orange', 'Purple', 'White', 'Yellow')
drop20.grid(column=1, row=19)

drop21 = tk.OptionMenu(window, input21, 'Abundant', 'Clustered', 'Numerous', 'Scattered', 'Several', 'Solitary')
drop21.grid(column=1, row=20)

drop22 = tk.OptionMenu(window, input22, 'Grasses', 'Leaves', 'Meadows', 'Paths', 'Urban', 'Waste', 'Woods')
drop22.grid(column=1, row=21)

b = tk.Button(window, text = 'Submit Information', command = b1)
b.place(x = 360, y =700)

window.mainloop()




