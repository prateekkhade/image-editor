'''
Currently sorts an array using the built in python sort method.
But in the future we will sort using the following algorithms as well
1. Quicksort
2. Mergesort
3. Insertion sort
4. Selection sort
5. Bubble sort
6. Radix sort
'''
class Sorting:
	def __init__(self, array= [], method='default'):
		self.array= array
		self.method= method
	
	def __repr__(self):
		return 'Object sorts a given array'

	def quicksort(self):
		pass

	def mergesort(self):
		pass

	def insertionsort(self):
		pass

	def selectionsort(self):
		pass

	def bubblesort(self):
		pass

	def radixsort(self):
		pass

	def sort_array(self):
		'''
		All methods will create a new sorted_array and return it
		'''
		if self.method=='quicksort':
			return self.quicksort()
		if self.method=='mergesort':
			return self.mergesort()
		if self.method=='insertionsort':
			return self.insertionsort()
		if self.method=='selectionsort':
			return self.selectionsort()
		if self.method=='bubblesort':
			return self.bubblesort()
		if self.method=='radixsort':
			return self.radixsort()

		self.sorted_array= sorted(self.array)
		return self.sorted_array