# immutable tuple
tup = (1,2,3)

# get first element
print(tup[0])

# unpack values
a,b,c = tup
print(c)

# dict
di = {'a':'hi','b':'bye'}
print(di['b'])

# iterate over keys
# for key in di:
for key in di.keys():
    print(di[key])
    
for val in di.values():
    print(val)
    
# continue to go to next iterative
# break to exit loop

# lambda functions: any number of arguments, only one expression

mult = lambda x,y: x*y
mult(3,4)

# all python class attributes are public
# _ prefix = protected 
# __ prefix = private

# creating class with two attributes
class MyClass(object):
    
    # method called when instance of class constructed
    # arg2 is optional, has a default value if not given anything
    def __init__(self, arg1, arg2='circle'):
        # define attributes of class
        self.color = arg1
        self.shape = arg2
    
    def what_color(self):
        return self.color
    
class MySecondClass(MyClass):
    def __init__(self, arg1):
        # call constructor for parent class
        super(MySecondClass, self).__init__(arg1)
        
# create instance of class
thing1 = MyClass('blue','oval')
print(thing1.shape)

# setting value of second attribute
thing1.shape = 'square'

uhm = thing1.what_color('pink')
print(uhm)

thing2 = MySecondClass(MyClass)
print(thing2.color)

# organization into modules by splitting code into directories/files
# in order to be recognized as module, need to contain file __init__.py

# use import directive to access code from other modules
import module_1.sub_module_1a

# string formatting
'{} {} and {}'.format('values are', 2, 3.4)

import csv

rows = ['i','like','cats','5','6']
# write list of lists into csv file
with open('eggs.csv','w') as file:
    wr = csv.writer(file)
    for row in rows:
        wr.writerow(row)

# read with row headings into a list of dictionaries
with open('eggs.csv', 'r') as file:
    rows = csv.DictReader(file)
    
import warnings
# default category = UserWarning
warnings.warn('hi')

# ignore class of warnings
warnings.simplefilter("ignore", UserWarning)
warnings.warn('bye')

# issuing exception
raise Exception('what')

# define own exception
class MyException(Exception):

# handling exceptions
try:
    # code which raises exception?
except:
    # code to execute if try block raises exception
# or    
except Exception as exception:
    # code if try block raises exception and exception is instance of Exception (issued above?)
    
class RNA(object):
    # a public dict variable(?)
    translation_table = {
        'TTT': 'F',
        'CAT': 'H',
        'ATG': 'M'
    }
    
    def __init__(self,arg1):
        self.seq = arg1
    
    # create dictionary where each set of three amino acids 
    def translate(self):
        aa = ''
        # assuming starts with ATG start codon
        for i in range(int(len(self.seq)/3)):
            aa += self.translation_table[self.seq[3*i:3*i + 3]];
        return aa
    
myrna = RNA('ATGTTTCAT')
# to make surethat's right
assert myrna.translate()[0] == 'M'
print(myrna.translate())

import numpy as np

arr1 = np.array([[1,2,3],[7,3,0]])
arr2 = np.array([[0,2,6],[1,1,1]])

# element-wise multiplication
print(arr1 * arr2)

# matrix multiplication
print(arr1 ** 2.)

a = np.zeros((3,1))
b = np.ones((3,1))
c = np.concatenate((a,b),axis=1)
print(np.shape(c))

# matrix of random numbers
d = np.random.rand(2,3)
print(d)

e = np.transpose(d)
print(e)

f = np.round(e)
print(f)

# matrix of random poisson-distributed values 
g = np.random.poisson(10,(2,3))
print(g.mean())

assert np.inf > 1e100