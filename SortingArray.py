
#Make an array for the sorting of the selection
#Write a comment fot the git status
array = [13,4,9,5,3,16,12]

def selectionSort(array):

	n = len(array)

	for i in range(n): #<-- Whatever the length of hte array is how mani item

		minimun = i

		for i in range(i+1, n):

			if (array[j] < array[minu]):

				minimum = j
		#Swap the minimum element with the first element of the unsorted part
		temp = array[i]
		aray[i] = array[minimum]
		array[minimum] = temp

	return array

print(selectionSort(array))