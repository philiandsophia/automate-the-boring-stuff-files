# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 07:11:00 2017

@author: user
"""

import os
import shelve

#os.path('usr','bin','spam')
#make sure programs can work on windows and linux and other operating systems

#os.makedirs('C:\delicious\walnut\waffles')
#created a folder called delicous, which contains folde walnut.
#the folder walnut contains the folder waffles

#print (os.path.abspath('.\\Scripts'))
#return a string of the absoulte path of the argument

#print (os.path.isabs(os.path.abspath('')))
#return ture if the arugment is an abouslte path and false if it is a relative path

#print (os.path.relpath('C\\Windows','C:\\'))
#return a string of a relative path
#from start path to path
#os.path.relpath(path,start)

#print (os.getcwd())
#return a string of current working directory

path = 'C:\\Windows\\System32\\calc.exe'

#print (os.path.basename(path))
#returns basename, which is the name that follows the last slash in a path
#base name is also file name

#print (os.path.dirname(path))
#returns a sring of everything that comes before the last slash in the path argument

#print (os.path.split(path))
#give a tuple of basename and dirname

#print (path.split(os.path.sep))
#split and give each folder name

#print (os.path.getsize(path))
#return the size in bytes of the file

#print (os.listdir('C:\Windows\System32'))
#retrun a list of filename strings for each file in the path argument

#total_size = 0
#for filenames in os.listdir('C:\Windows\System32'):
    #total_size = os.path.getsize(os.path.join('C:\Windows\System32', filenames))

#print(total_size)
#print the total size of all files in system 32

#os.path.exists(path) returns True if the file or folder referred exist
#os.path.isfile(path) returns True if the path argument exists and is a file
#os.path.isdir(path) returns True if the path arugment exists and is a folder

#print (os.path.exists('C:\\Windows\\system32\\Desktop\\eh'))
#if there is an unicode error, duplicate all the backlashes

#helloFile = open("C:\\Users\\user\\Desktop\\eh.txt")
#saves helloFile as a variable as the file indicated

#helloContent = helloFile.read()
#saves the content, this case a test line as a varible
#redlines() saves one string for each line of text in a list

baconFile = open('bacon.txt', 'w')
#creates baconfile in write mode, this allows for writing new things to files
baconFile.write('Hello world!')
baconFile.close()
baconFile = open('bacon.txt', 'a')
#a is append mode, now we can add to the text file instead of replacing it, just like in write mode
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()


#shelves module let you save save variables in your Python programs to binary shelf file
shelfFile = shelve.open('mydata')
#file name is mydata
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
#'cats' now refer to the list cats
#this stores the list in shelffile as a value associated with the key 'cats'
#print (shelfFile['cats']) returns the list cats
#print list(shelfFile.keys() returns ['cats'], the key)
#print list(shelfFile.values()) returns the list cats, the values
shelfFile.close()


#> import pprint
#>>> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
#>>> pprint.pformat(cats)
#"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
#>>> fileObj = open('myCats.py', 'w')
#>>> fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
#83
#>>> fileObj.close()
#Here, we import pprint to let us use pprint.pformat(). We have a list of dictionaries, stored in a variable cats. To keep the list in cats available even after we close the shell, we use pprint.pformat() to return it as a string. Once we have the data in cats as a string, it’s easy to write the string to a file, which we’ll call myCats.py.
#
#The modules that an import statement imports are themselves just Python scripts. When the string from pprint.pformat() is saved to a .py file, the file is a module that can be imported just like any other.
#
#And since Python scripts are themselves just text files with the .py file extension, your Python programs can even generate other Python programs. You can then import these files into scripts.
#
#
#>>> import myCats
#>>> myCats.cats
#[{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
#>>> myCats.cats[0]
#{'name': 'Zophie', 'desc': 'chubby'}
#>>> myCats.cats[0]['name']
#'Zophie'
#The benefit of creating a .py file (as opposed to saving variables with the shelve module) is that because it is a text file, the contents of the file can be read and modified by anyone with a simple text editor. For most applications, however, saving data using the shelve module is the preferred way to save variables to a file. 