# #Python Revision 
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

#Sring fuctions
a='AV,Aava'
print a.lower()
print a.upper()
print a.find('a')
print a[0]+a[1]
print 'Hi %s !!'%a
print a[:-4]
print a.split(',')
print a.find('V')
print a.startswith('av')

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