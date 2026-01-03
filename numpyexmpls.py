import numpy as np

my_list = [1, 2, 3, 4, 5]

my_list = my_list * 2

print(my_list)


array = np.array([1, 2, 3, 4, 5])

array = array * 2

print(type(array))

print(array)

# 1 diemensuon_array 
array = np.array(['A', 'B', 'C', 'D', 'E'])

print(array.ndim)

# 2 diemensuon_array 

array = np.array([['A', 'B', 'C'], 
                  ['D', 'E', 'F'], 
                  ['G', 'H', 'I']])

print(array.ndim)

# 3 diemensuon_array 

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['D', 'E', 'F']],
                  [['D', 'E', 'F'], ['A', 'B', 'C'], ['D', 'E', 'F']],
                  [['S', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', '']]])

print(array.ndim)

# prints the shape of the n dimensional array
print(array.shape)

print(array[0][0][0])  # Output: A

#mutidiemensional array indexing
print(array[0,0,0])  # Output: A
print(array[2,1,1])  # Output: K

word = array[0, 0, 0] + array[2,0, 0] + array[2, 0, 0]
print(word)

#Slicing in n dimensional array

array = np.array ([[1,2, 3, 4], 
                  [5,6, 7, 8], 
                  [9,10,11,12], 
                  [13,14,15,16]])

#array[start: end: step]

print(array[0])   #first row
print(array[-1])  #last row

print(array[0:3])  #first three rows

print(array[0:4:2])  #rows with step 2

print(array[::2])  #rows with step 2

print(array[::-1]) #reversing the array rows

#slicing columns

array = np.array ([[1,2, 3, 4], 
                  [5,6, 7, 8], 
                  [9,10,11,12], 
                  [13,14,15,16]])

print(array[:,0])  #first column [ 1  5  9 13]

print(array[0:4:2,1])  # [ 2 10]

print(array[0:4:2,-1])  # [ 4 12]

print(array[:, 0:3])  

print(array[:, 1:])  

print(array[:, ::2]) # every second column

print(array[:, 1::2]) # every second column

print(array[:, ::-1]) # reversing the columns

print(array[0:2,0:2])

print(array[ :2, 2:])

print(array[2:, :2 ])

#--------------------------------
#. Scalar Arthmetic Operations  
#--------------------------------

array = np.array([1, 2, 3])

print(array + 1)  # Output: [2 3 4]

print(array - 2)  # Output: [-1  0  1]

print(array / 4) # Output: [0.25 0.5  0.75]

print(array ** 5)  # Output: [  1  32 243]

#vector Arthmetic Operations

array = np.array([1, 2, 3])

print(np.sqrt(array))  # Output: [1.         1.41421356 1.73205081] 

print(np.round(np.sqrt(array)))  # Output: [1. 1. 2.]

radii = np.array([1, 2, 3])

print(np.round(np.pi * radii ** 2))  # Output: [ 3.14159265 12.56637061 28.27433388]


array1 = np.array([1, 2, 3])

array2 = np.array([4, 5, 6])

print(array1 + array2)  # Output: [5 7 9]

print(array2 - array1)  # Output: [3 3 3]

print(array1 * array2)  # Output: [ 4 10 18]

print(array2 / array1)  # Output: [4.  2.5 2. ]

print(array2 ** array1)  # Output: [4 2 2]

scores = np.array([91, 55, 100, 73, 82, 64 ])

print(scores == 100)  # Output: [False False  True False False False]


print(scores >= 100)  # Output: [False False  True False False False]   

print(scores < 60)  # Output: [False  True False False False  True]

scores[scores == 0] = 0
print(scores)  # Output: [ 0 55  0 73 82  0]
print(scores[scores >= 60])  # Output: [73 82]
print(scores[scores < 60])  # Output: [55]
print(scores[(scores >= 60) & (scores < 80)])  # Output: [73]
print(scores[(scores < 60) | (scores > 80)])  # Output:
# Output: [ 0 55  0 82  0]
print(np.mean(scores))  # Output: 51.666666666666664
print(np.median(scores))  # Output: 55.0
print(np.std(scores))  # Output: 34.52723666237365


#--------------------------------
#. Broadcasting in numpy 
#--------------------------------

# Allows Numpy to perform operations on arrays of different shapes
# The diemnesions need the same size or one of them should be 1

array1 = np.array([[1, 2, 3, 4]])  # Shape (1, 4)
array2 = np.array([[1], [2], [3], [4]])  # Shape (4, 1)

print(array1.shape)  # Output: (1, 4)
print(array2.shape)  # Output: (4, 1)

print(array1 *  array2) 

array1 = np.array([[1, 2, 3,4,  5, 6, 7, 8, 8, 10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array1.shape)  # Output: (1, 10
print(array2.shape)  # Output: (10, 1
# compatible shapes for broadcasting

print(array1 + array2)



#--------------------------------
#. Aggregate functions in numpy 
#--------------------------------

array = np.array([[1, 2, 3, 4, 5], 
                 [6, 7, 8, 9, 10]])

print(np.sum(array))  # Output: 55
print(np.mean(array))  # Output: 5.5
print(np.median(array))  # Output: 5.5
print(np.std(array))  # Output: 2.8722813232690143
print(np.var(array))  # Output: 8.25
print(np.min(array))  # Output: 1
print(np.max(array))  # Output: 10
print(np.argmin(array))  # Output: 0
print(np.argmax(array))  # Output: 9        
print(np.sort(array))  # Output: [ 1  2  3  4  5  6  7  8  9 10]
print(np.unique(array))  # Output: [ 1  2  3  4  5  6  7  8  9 10]
print(np.sqrt(array))  # Output: [1.         1.41421356 1.73205081 2.         2.23606798 2.44948974

print(np.sum(array, axis=0))  # Output: [ 7  9 11 13 15]
print(np.sum(array, axis=1))  # Output: [15 40]  row sum



#--------------------------------
#. Filtering in numpy 
#--------------------------------

ages = np.array([[25, 15, 35, 40, 45], 
                [20, 22, 10, 26, 28]])

# Filter ages greater than 30
Teenagers = ages[ages <= 16]
print("Teenagers:", Teenagers)  # Output: Teenagers: [15 16 14 13]

adults = ages[ages > 18]
print("Adults:", adults)  # Output: Adults: [25 35 40 45 20 22 26 28]


adults = ages[(ages > 18) & (ages < 40) ]
print("Adults between 18 and 40:", adults)  # Output: Adults between 18 and 40: [25 35 20 22 26 28]


#--------------------------------
#. Random numbers in numpy 
#--------------------------------
# Generate random numbers from a uniform distribution over [0.0, 1.0)

random_numbers = np.random.rand(5)
print("Random numbers:", random_numbers)
# Generate random integers between 10 and 50    
random_integers = np.random.randint(1, 7, size=1)
print("Random integers:", random_integers)

rng = np.random.default_rng()
print("Random Number:", rng.integers(low = 1, high = 7, size = 3))
print("Random Number:", rng.integers(low = 1, high = 7, size = (1,3)))



rng = np.random.default_rng(seed= 1)
print("Random Number with seed 1:", rng.integers(low = 1, high = 7, size = 3))


print(np.round(np.random.uniform(1, 10, size=5)), 3)  # Output: Random numbers between 1 and 10

array = np.array([1, 2, 3, 4, 5])
np.random.shuffle(array)
print("Shuffled array:", array)  # Output: Shuffled array: [3

fruits = np.array(['apple', 'banana', 'cherry', 'date', 'elderberry'])
print(fruits)
np.random.shuffle(fruits)
print("Shuffled fruits:", fruits)  # Output: Shuffled fruits: ['date'

print("Random fruit:", np.random.choice(fruits, size = 2))  # Output: Random fruit: 'banana'

