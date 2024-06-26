#-------------------------# 1. append( "yaha uvh value" )  #------------------------------# 

list = [1, 3, 4, 5]

list.append ( 7 )           # Adds one element at the end of list
# print ( list )              # O/p => [1, 3, 4, 5, 7]

list.append ( "hello" )     
# print ( list )              # O/p => [1, 3, 4, 5, 7, 'hello']


#-------------------------# 2. sort () #----------------------------#


list1 = [ 4, 3, 7, 1, 8, 4 ]

list1.sort()                # sorts in ascending order
# print ( list1 )             # O/p => [1, 3, 4, 4, 7, 8]

list2 = ["banana", "litchi", "apple"]


list2.sort()                # sorts in ascending order
# print ( list2 )             # O/p => ['apple', 'banana', 'litchi']


#-------------------------# 3. sort ( reverse = True ) #---------------------#


list3 = [ 4, 3, 7, 1, 8, 4 ]

list3.sort ( reverse = True )   # sorts in descending order
# print ( list2 )                 # O/p => [8, 7, 4, 4, 3, 1]


list4 = ["banana", "litchi", "apple"]

list4.sort ( reverse = True )   # sorts in descending order
# print ( list4 )                 # O/p => ['litchi', 'banana', 'apple']


#--------------------------# 4. reverse () #--------------------------------#


list5 = [2, 3, 4, 6, 1, 0]      

list5.reverse ()                # reverses list
# print ( list5 )                 # O/p => [0, 1, 6, 4, 3, 2]


list6 = ['a', 'r' , 'e', 'd', 'i' , 'u', 'o']

list6.reverse ()                # reverses list
# print ( list6 )                 # O/p => ['o', 'u', 'i', 'd', 'e', 'r', 'a']


#------------------------# 5. insert (idx, el) #--------------------------------#


list7 = [2, 3, 4, 6, 1, 0]

list7.insert ( 3, 99 )          # insert element at index
# print ( list7 )                 # O/p => [2, 3, 4, 99, 6, 1, 0]


#------------------------# 6. remove ("remove value") #-------------------------#


list8 = [2, 3, 4, 6, 1, 0]

list8.remove ( 3 )              # removes first occurrence of element
# print ( list8 )                 # O/p => [2, 4, 6, 1, 0]


#----------------------------# 7. pop (idx) #----------------------------------#


list9 = [2, 1, 3, 6, 5, 7, 8,]

list9.pop( 4 )                  # removes element at idx
print ( list9 )                 # O/p => [2, 1, 3, 6, 7, 8]
