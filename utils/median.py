'''
Finds median given a sorted array
'''
from __future__ import division
from sort import Sorting

def median(array, int_return=True, array_sorted= False):
	'''
	# Returns: median of a sorted array

	# Parameters:
	# array: sorted array of integers/floats

	# Returns:
	# med: median of the sorted array(int/float)
	'''
	if not array:
		raise Exception("Array is empty!")

	array_len= len(array)

	if array_len==1:
		return array[0]

	if not array_sorted:
		sortarr= Sorting(array)
		array= sortarr.sort_array()

	if array_len%2!=0:#odd length array
		return array[array_len//2]

	#[1, 2, 3, 4]
	if not int_return: #returning the average of two middle values
		sum_mid_vals= array[array_len//2]+array[(array_len//2)-1]
		return sum_mid_vals/2

	return array[(array_len//2)-1] #Not taking the average of two middle values as we need an integer return for images