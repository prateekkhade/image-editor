'''
Convolves a kernel over a matrix(image)
'''
from median import median
import cv2
import numpy as np

class convolve2D:
	def __init__(self, kernel= None, matrix= None, padding=0, stride=1):
		self.kernel= kernel #2D python list
		self.matrix= matrix #2D python list, bigger in dimension than kernel
		self.ret_mat= [[0 for i in range(len(matrix[0]))] for _ in range(len(matrix))]
		self.padding= padding
		self.stride= stride

	def get_kernel_matrix_dims(self):
		self.len_kernel_cols, self.len_kernel_rows= len(kernel[0]), len(kernel)
		self.len_matrix_cols, self.len_matrix_rows= len(matrix[0]), len(matrix)

		self.diff_in_row_len= self.len_matrix_rows - self.len_kernel_rows
		self.diff_in_col_len= self.len_matrix_cols - self.len_kernel_cols

		if self.diff_in_row_len<0 or self.diff_in_col_len<0:
			raise Exception('kernel is not smaller in size as compared to the image')

	def reverse_kernel_up_down(self):
		'''
		Returns: kernel matrix up down reversed

		params: None
		'''
		i= 0
		j= self.len_kernel_rows-1
		
		while i<j:
			self.kernel[i], self.kernel[j]= self.kernel[j], self.kernel[i]
			i+=1
			j-=1


	def reverse_kernel_left_right(self):
		'''
		Returns: kernel matrix left to right reversed

		params: None
		[[1, 2, 3],
 		 [4, 5, 6],
 		 [7, 8, 9]]
		'''
		for i in range(self.len_kernel_cols//2):
			for j in range(self.len_kernel_rows):
				self.kernel[j][i], self.kernel[j][self.len_kernel_cols-1-i]= self.kernel[j][self.len_kernel_cols-1-i], self.kernel[j][i]
		


	def cross_correlate(self):
		'''
		#Returns cross correlated kernel matrix -> meaning, left to right reverse and up side down kernel
	
		#params: as a class method, it does not receive anything, just uses the data member, kernel matrix, flips it left to right, upside down
		
		#returns: doesn't return but modifies self.kernel matrix
		'''
		self.reverse_kernel_up_down()
		self.reverse_kernel_left_right()

	def processConv2DFor(self, row= 0, col= 0, processFor= None):
		if processFor== 'avg':
			sum= 0

			for k_row in range(0, self.len_kernel_rows):
				for k_col in range(0, self.len_kernel_cols):
					sum+= self.kernel[k_row][k_col]*self.matrix[row-1+k_row][col-1+k_col]
			self.ret_mat[row][col]= sum//(self.len_kernel_rows*self.len_kernel_cols)
			return

		if processFor=='median':
			array= []
			for k_row in range(0, self.len_kernel_rows):
				for k_col in range(0, self.len_kernel_cols):
					array.append(self.matrix[row-1+k_row][col-1+k_col])
			print(sorted(array), median(array))
			self.ret_mat[row][col]= median(array)
			return


	def _convolve2D(self):
		if self.padding is 0 and self.stride is 1:

			for row in range(1, self.diff_in_row_len+2):
				for col in range(1, self.diff_in_col_len+2):

					self.processConv2DFor(row, col, processFor='median')


	def convolve2D(self):
		# Getting kernel and matrix dimensions
		self.get_kernel_matrix_dims()

		# Cross correlating kernel matrix
		self.cross_correlate()

		# Convolve helper
		self._convolve2D()


