'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
array = []
num = int(input())
for i in range(num):
    array.insert(0, int(input()))
    
for i in range(num):
    print(array[i])



