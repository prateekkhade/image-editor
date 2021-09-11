'''
Convolves a kernel over a matrix(image)
'''

class convolve:
	def __init__(self, kernel= None, matrix= None):
		self.kernel= kernel #2D python list
		self.matrix= matrix #2D python list, bigger in dimension than kernel
		self.ret_mat= matrix
		self.get_kernel_metrics_dims()

	def get_kernel_metrics_dims(self):

		self.len_kernel_cols, self.len_kernel_rows= len(kernel[0]), len(kernel)
		self.len_matrix_cols, self.len_matrix_rows= len(matrix[0]), len(matrix)

		self.diff_in_row_len= self.len_matrix_rows - self.len_kernel_rows
		self.diff_in_col_len= self.len_matrix_cols - self.len_kernel_cols

		if self.diff_in_row_len<0 or self.diff_in_col_len<0:
			raise Exception('kernel is not smaller in size as compared to the image')

	def convolve(self):
		for i in range(0, self.diff_in_row_len+1):
			for j in range(i, self.diff_in_col_len+1):
				
				for k in range(0, self.len_kernel_rows):
					for l in range(0, self.len_kernel_cols):
						self.ret_mat[i+k][j+l]= self.matrix[i+k][j+l]*self.kernel[k][l]


kernel= [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
'''
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
'''
matrix= [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
'''
[[ 1,  2,  3,  4,  5],
 [ 6,  7,  8,  9, 10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20], 
 [21, 22, 23, 24, 25]]
'''
con= convolve(kernel, matrix)
con.convolve()
print(con.ret_mat)