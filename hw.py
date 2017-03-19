

# #Python Interview Revision 
# var ="1"+"asd"

# #Binary form of digit
# b=0x010

# #type gives the type of data
# type(b)

# #complex numbers
# e=1+2j

# #double // to round the values
# flt=7//3.0

# #String casting 
# str(12)

# #int casting(remove decimal part)
# int (2.6)



# #Basic Structure of an app
# import sys

# def main():
# 	Hello(sys.argv[1])

# def Hello(name):
# 	print 'Hello',name


# if __name__ == '__main__':
# 	main()

# #Python runs everything at the moment not from before(This will not throw error)
# name='Alice'
# if name=='Alice':
# 	print 'blablab'
# else:
# 	DoesNotExit(name)

# #Sring fuctions
# a='AV,Aava'
# print a.lower()
# print a.upper()
# print a.find('a')
# print a[0]+a[1]
# print 'Hi %s !!'%a
# print a[:-4]
# print a.split(',')
# print a.find('V')
# print a.startswith('av')

# #String assignment reinitailizes the value where as list doesn't
# a='Hi'
# b=a
# b=b.replace(a[0],'a')
# print b
# print a


# a=[1,2,3]
# b=a
# print ' a :'+str(a)
# print ' b :'+str(b)
# b[0]=2
# print ' b[0]=2'
# print ' a :'+str(a)
# print ' b :'+str(b)


# #Sublime settings convert tabs_to_spaces:true and tab size:2 (Google Style)

# #list slices
# a=[1,2,3,4]
# print (a[-4:-1])


# #Custom Sorting is sone using tuples
# #Basically you define the method which returns a list of properties 
# #by which the value needs to be sorted
# s=((1,'z'),(2,'d'),(3,'sa'))
# def sortKey(s): return (len(s[1]),s[0])
# sorted(s,key=sortKey)


# #Dictionary
# d={}
# d['z'] = 'alpha'
# d['o'] = 'omega'
# d['g'] = 'gamma'
# print d.get('A')
# print d.keys()
# print d.values()
# print d.items() #returns tuple
# print d
# from __future__ import print_function
# import sys
# def Cat(filename):
#   f=open(filename, 'rU')
#   for line in f: #Take 1 line at a time
#     print (line,end='')
#   lines=f.readlines()#Takes the whole file in memory
#   lines=[x[:-2] for x in lines]
#   print (lines)
#   text=f.read()
#   print (text)
#   f.close()

# def main():
#   Cat(sys.argv[1])
# if __name__ == '__main__':
#   main()
#Reading unicode files
import codecs
f=codecs.open('/home/devyash/Desktop/Python_codes/google-python-exercises/basic/alice.txt','rU','utf-8')
for line in f:
  print f
