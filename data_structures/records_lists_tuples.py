# records - usually a row in a database
# connect to an SQL database and run some commands

'''
# records in a database
# connect to mysql
import mysql.connector

hostname = 'localhost'
username = 'root'
password = 'password'
database = 'patterns'


def doQuery(connection):
    current_connection = connection.cursor()

    current_connection.execute( "SELECT firstname, surname, password FROM people" )

    for firstname, surname, password in current_connection.fetchall() :
        print(firstname, surname, password)


print("RESULTS of SELECT statement:")
my_connection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
doQuery( my_connection )
my_connection.close()
'''

'''
# lists
# see Python book
# can have lists of lists
# lists of anything
# lists are mutable
nums = [3, 41, 12, 9, 74, 15]
print(nums[:])
print(nums[:2])
print(nums[4:])
del nums[3]
print(nums)
nums = [3, 41, 12, 9, 74, 15]
print(nums)
nums.remove(12)
print(nums)
nums.append(33)
print(nums)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))
s = 'pining for the fjords'
print(s)
t = s.split()
print(t)
s = 'spam-spam-spam'
print(s)
delimiter = '-'
t = s.split(delimiter)
print(t)
'''


# tuples
# tuples are immutable
t = 'a', 'b', 'c', 'd', 'e'
print(t)
t = ('a', 'b', 'c', 'd', 'e')
print(t)
print(type(t))
l = tuple('lupins')
print(l)
print(t[0])
print(t[1:3])
print((0, 1, 2000000) < (0, 3, 4))
txt = 'but soft what light in yonder window breaks'
words = txt.split()
# make a list of tuples
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)
print(t)
res = list()
for length, word in t:
    res.append(word)
print(res)
# dictionaries have an items function which returns a list of tuples
d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)
# prints in hash key order (from dictionary immplementation
for key, val in list(d.items()):
    print(val, key)
# Because tuples are hashable and lists are not..
# ..if we want to create a composite key to use in a dictionary we must use a tuple as the key
