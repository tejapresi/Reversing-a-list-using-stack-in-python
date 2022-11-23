#empty list named stack
stack = []

#ask user to enter the size of the list
N = int(input('Enter the size of the list: '))

#create N size arr with None values default
arr = [None] * N 

#ask user to enter the list elements
print('Enter list elements: ')

#iterating loop N times
for i in range(N):
	#ask user to enter element and store it in arr at index i
	arr[i] = int(input('Enter element: '))

#print the List
print('List: ',arr)

#iterating loop through arr
for i in arr:
	#push the list element in stack
	stack.append(i)

#iterating loop N times
for i in range(N):
	#pop the stack element and store it in arr at i
	arr[i] = stack.pop()

#print the list
print('Reversed list: ',arr)