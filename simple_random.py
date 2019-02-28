import numpy as np




if __name__ == '__main__':

	A = np.array([[0,1,1],[0,1,0]])
	print(A)
	(rows,cols) = A.shape #rows is number of images, cols is tags
	idx = np.random.randint(rows)
	first_im =  A[idx, :]
	A = np.delete(A, idx, 0)

	rows = A.shape[0]
	while rows > 0: #While there are still images

		if rows > 10:
			random_ten_idx = np.random.permutation(rows)[:10]
			random_ten = A[random_ten_idx,:]
			
		else:
			#just check them all


		#check score and if all of them are 0 than exit

		#randomly pick 10 images
	print(A)
	print(first_im)
	print(np.delete(A, 0, 0).shape[0])
