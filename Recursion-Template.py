def factorial(targetNumber) :
  # Base case
  if targetNumber == 1 : # Factorial of 1 is 1
    return 1
  # Recursive case
  else :
    return (targetNumber * factorial(targetNumber - 1))

def printNaturalNumbers(lowerRange, upperRange):
  if lowerRange > upperRange :
    return
  print(lowerRange)
  printNaturalNumbers(lowerRange + 1, upperRange)

#Indirect Recursion
def printNaturalNumbers2(lowerRange, upperRange) :
	if lowerRange <= upperRange :
	  print(lowerRange)
	  lowerRange += 1
	  helperFunction1(lowerRange, upperRange)
	else :
		return
def helperFunction1(lowerRange, upperRange) :
  if lowerRange <= upperRange :
    print(lowerRange)
    lowerRange += 1
    printNaturalNumbers(lowerRange, upperRange)
  else :
      return


#Iterative 
def factorialIterative(targetNumber) :
  index = targetNumber - 1 # set the index to target - 1
  while index >= 1 :
    targetNumber = targetNumber * index # multiply targetNumber with one less than itself, i.e, index here
    index -= 1 # reduce index in each iteration
  return targetNumber

#Recursive
def factorialRecursion(targetNumber) :
  # Base case
  if targetNumber == 1 : # Factorial of 1 is 1
    return 1
  # Recursive case
  else :
    return (targetNumber * factorial(targetNumber - 1))

# Converting Iterative to Recursive
# 1. Identify the main loop
# This loop should modify one or more variables
# It should return a result based on its final values.
# 2. Use the loop condition as the base case and the body of the loop as the recursive case.
# 3. The local variables in the iterative version turn into the parameters of the recursive version.
# 4. Compile and rerun tests.
# 5. Refactor the new function: You may be able to remove some temps and find a better structure for the conditional in the recursive function.


# Passing string template
def isVowel(str):
    return None
def countVowels(string, n): # function that returns the count of vowels
	# Base Case
  if n == 1 :
	  return isVowel(string[0]) 
  # Recursive Case
  return countVowels(string, n - 1) + isVowel(string[n - 1]) 

# Passing Array template
def firstIndex(arr, testVariable, currentIndex) : # returns the first occurrence of testVariable
  # Base Case1
  if len(arr) == currentIndex :
    return -1
  # Base Case2  
  if arr[currentIndex] == testVariable :
    return currentIndex
  # Recursive Case
  return firstIndex(arr, testVariable, currentIndex + 1)

##################################
# Recursion with Numbers
##################################

def power(base, exponent):
  # Base Case
  if exponent == 0 :
    return 1
  # Recursive Case
  else :
    return base * power(base, exponent - 1)

def sumTill(targetNumber) :
  # Base Case
  if targetNumber == 1 :
    return targetNumber
  # Recursive Case
  else :
    return targetNumber + sumTill(targetNumber - 1)

def mod(dividend, divisor) :
  # Check division by 0
  if divisor == 0 :
    print("Divisor cannot be ")
    return 0
  # Base Case
  if dividend < divisor :
    return dividend
  # Recursive Case
  else :
    return mod(dividend - divisor, divisor)

def gcd(testVariable1, testVariable2) :
  # Base Case
  if testVariable1 == testVariable2 :
    return testVariable1
  # Recursive Case
  if testVariable1 > testVariable2 :
    return gcd(testVariable1 - testVariable2, testVariable2)
  else :
    return gcd(testVariable1, testVariable2 - testVariable1)

def printPascal(testVariable) :
    # Base Case
    if testVariable == 0 :
        return [1]
    else :
        line = [1]
        # Recursive Case
        previousLine = printPascal(testVariable - 1)
        for i in range(len(previousLine) - 1):
            line.append(previousLine[i] + previousLine[i + 1])
        line += [1]
    return line

def decimalToBinary(testVariable) :
  # Base Case
  if testVariable <= 1:
    return str(testVariable)
  # Recursive Case
  else:
    return decimalToBinary(testVariable // 2) + decimalToBinary(testVariable % 2) # Floor division - 
      # division that results into whole number adjusted to the left in the number line


##################################
#Recursion with Strings
##################################

def remove(string):
  # Base Case
  if not string:
      return ""
  # Recursive Case
  if string[0] == "\t" or string[0] == " ":
      return remove(string[1:])
  else:
      return string[0] + remove(string[1:])

def removeDuplicates(string):
    # Base Case1
    if not string:
        return ""
    # Base Case2
    elif len(string) == 1 :
        return string
    # Recursive Case1
    elif string[0] == string[1] :
        return removeDuplicates(string[1:])
    # Recursive Case2
    return string[0] + removeDuplicates(string[1:])


def merge(string1, string2) :
  # Base Case1
  if string1 == "" :
    if string2 == "" : 
      return ""
    return string2
  # Base Case2
  elif string2 == "" :
    return string1
  # Recursive Case1
  elif string1[0] > string2[0] :
      return string2[0] + merge(string1, string2[1:])
  # Recursive Case2
  return string1[0] + merge(string1[1:], string2)

def recursiveLength(testVariable) : 	
	# Base Case	
	if (testVariable == "") : 
		return 0
	# Recursive Case
	else : 
		return 1 + recursiveLength(testVariable[1:]) 

def sumDigits(testVariable):
  # Base Case
  if testVariable == "":
    return 0
  # Recursive Case 
  else:
    return int(testVariable[0]) + sumDigits(testVariable[1:])

def isPalindrome(testVariable) :
  # Base Case
  if len(testVariable) <= 1 : # Strings that have length 1 or 0 are palindrome
      return True
  # Recursive Case
  length = len(testVariable)
  if testVariable[0] == testVariable[length - 1] : # compare the first and last elements
      return isPalindrome(testVariable[1: length - 1])
  return False

##################################
# Recursion with Arrays
##################################

def count(array, key) :
  # Base Case
  if array == []: 
      return 0

  # Recursive case1
  if array[0] == key:
      return 1 + count(array[1:], key)

  # Recursive case2
  else:
      return 0 + count(array[1:], key)

def reverse(array):
  # Base case1
  if len(array) == 0: # If we encounter an empty array, simply return an empty array
    return []
  # Base case2
  elif len(array) == 1 : # Inverting an array of size 1 returns the same array
   return array
  # Recursive case
  return [array[len(array) - 1]] + reverse(array[:len(array) - 1])

def replace(array, currentIndex) :
  if currentIndex < len(array) :
    if array[currentIndex] < 0 :
      array[currentIndex] = 0

    replace(array, currentIndex + 1)

  return

def average(testVariable, currentIndex = 0) : 
	# Base Case
	if currentIndex == len(testVariable) - 1 : 
		return testVariable[currentIndex] 
  # Recursive case1
	# Recursive case
	# When currentIndex is 0, divide sum computed so far by len(testVariable). 
	if currentIndex == 0 : 
		return ((testVariable[currentIndex] + average(testVariable, currentIndex + 1)) / len(testVariable)) 
  # Recursive case2
	# Compute sum 
	return (testVariable[currentIndex] + average(testVariable, currentIndex + 1)) 

def balanced(testVariable, startIndex = 0, currentIndex = 0) :
  # Base case1 and 2
  if startIndex == len(testVariable) : 
    return currentIndex == 0
  # Base case3
  if currentIndex < 0 : # A closing bracket did not find its corresponding opening bracket
    return False
  # Recursive case1
  if testVariable[startIndex] == "(" : 
    return  balanced(testVariable, startIndex + 1, currentIndex + 1)
  # Recursive case2
  elif testVariable[startIndex] == ")" : 
    return  balanced(testVariable, startIndex + 1, currentIndex - 1)


def sort(testVariable, length):
	# Base case
	if length <= 1 :
		return
	# Sort first n-1 elements
	sort(testVariable, length - 1)
	# Insert last element at its correct position in sorted array
	lastElement = testVariable[length - 1] # fetch the last element
	temp = length - 2 # start finding its correct location from one element before it
	# Move elements of testVariable[0..i-1], that are greater than key, to one position ahead of their current position 
	while (temp >= 0 and testVariable[temp] > lastElement):
		testVariable[temp + 1] = testVariable[temp]
		temp = temp - 1

	testVariable[temp + 1] = lastElement # place the element in its correct position


##################################
# Recursion with Data Stucture
##################################
# import linkedList as l
def helperFunction2(myLinkedList, current, previous) : # This function reverses the linked list recursively
	# Base case
	if current.next is None : 
		myLinkedList.head = current  
		current.next = previous 
		return 
	next = current.next
	current.next = previous 
	# Recursive case
	helperFunction2(myLinkedList, next, current)  

def reverseList(myLinkedList): 
	# Check if the head node of the linked list is null or not
	if myLinkedList.head is None: 
		return 
	# Call the helper function --> main recursive function
	helperFunction2(myLinkedList, myLinkedList.head, None) 



import graph as g
def helperFunction3(myGraph, currentNode, visited) : 
  # Mark the currentNode as visited and print it 
  if(visited[currentNode] == False) :
    visited[currentNode] = True
    print(currentNode) 
  # Recur for all the vertices adjacent to currentNode
  for i in myGraph.graph[currentNode]: 
    if visited[i] == False: 
      helperFunction3(myGraph, i, visited) 

def DFS(myGraph): 
  visited = [False]*(myGraph.vertices) # Initially all vertices are marked as unvisited
  helperFunction3(myGraph, 0, visited) # Call helper function starting from node 0



# import linkedList as l
def length(testVariable, head) :
	# Base case
	if (not head) :
		return 0
	# Recursive case
	else :
		return 1 + length(testVariable, head.next) 


def isEmpty(stack) :
  return len(stack) == 0
def push(stack, item) : # push item to stack
  stack.append( item ) 
def pop(stack) : # pop item from stack
  if(isEmpty(stack)) : # display error if stack empty  
    print("Stack Underflow ")
    exit(1)
  return stack.pop() 

def insertAtBottom(stack, item) : # Recursive function that inserts an element at the bottom of a stack.
  # Base case
  if isEmpty(stack) :
    push(stack, item)
  # Recursive case
  else:
    temp = pop(stack)
    insertAtBottom(stack, item)
    push(stack, temp) 

def reverseStack(stack) :
  # Recursive case
  if not isEmpty(stack) :
    temp = pop(stack)
    reverse(stack)
    insertAtBottom(stack, temp) 



import graph as g
def helperFunction(myGraph, currentNode, visited, result) :
  visited[currentNode] = True # Mark the current node as visited
  # Recur for all the adjacent vertices of currentNode
  for i in myGraph.graph[currentNode] :
    if visited[i] == False :
      helperFunction(myGraph, i, visited, result)
  result.insert(0, currentNode) # Push current vertex to result

def topologicalSort(myGraph) :
  visited = [False] * myGraph.vertices  # Mark all the vertices as not visited
  result = [] # Our stack to store the result/output
  for currentNode in range(myGraph.vertices) :
    if visited[currentNode] == False :
      helperFunction(myGraph, currentNode, visited, result)
  return(result)

