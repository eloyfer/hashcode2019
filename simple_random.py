import numpy as np


def get_score(array, row):
	score1 = np.dot(array, row.T)
	score2 = np.dot(1 - array, row.T)
	score3 = np.dot(array, 1 - row.T)

	stack_the_layers = np.stack((score1, score2, score3), axis=-1)
	adj = np.min(stack_the_layers, axis=-1)
	return adj

if __name__ == '__main__':
	A = np.array([[0,1,1],[0,1,0]])
	A = np.append(A, np.array([range(A.shape[0])]).T, axis=1)

	(rows,cols) = A.shape #rows is number of images, cols is tags
	idx = np.random.randint(rows)
	first_im =  A[idx, :]
	A = np.delete(A, idx, 0)

	slideshow_list = [first_im[-1]]

	rows = A.shape[0]
	cur_im = first_im
	while rows > 0: #While there are still images

		if rows > 10:
			random_ten_idx = np.random.permutation(rows)[:10]
			random_ten = A[random_ten_idx,:]

			score = get_score(random_ten, first_im)
			if score < 1:
				break #adding more slides won't add to show

			slideshow_list.append([])
		else:
			#just check them all
			score = get_score(random_ten, first_im)
			if score < 1:
				break #adding more slides won't add to show
			slideshow_list.append([])

	# This is final list
	print(slideshow_list)
