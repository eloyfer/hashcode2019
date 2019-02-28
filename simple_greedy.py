import numpy as np
import argparse





def get_score(array):
	score1 = np.dot(array, array.T)
	score2 = np.dot(1 - array, array.T)
	score3 = np.dot(array, 1 - array.T)

	stack_the_layers = np.stack((score1, score2, score3), axis=-1)
	adj = np.min(stack_the_layers, axis=-1)
	return adj

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('input')
	args = parser.parse_args()

	from read_data import read_data
	A, im_inds = read_data(args.input)

	score_mat = get_score(A)

	start = np.argmax(score_mat)
	i1, i2 = np.unravel_index(start, score_mat.shape)
	score_mat[:,i1] = -1
	score_mat[:,i2] = -1

	print(score_mat)
	print(start)
	slideshow =[i1,i2]
	while True:
		# print(score_mat)

		end1 = np.argmax(score_mat[i1])
		end2 = np.argmax(score_mat[i2])
		if end1 == end2:
			end2 = -1

		val1 = score_mat[i1,end1]
		val2 = score_mat[i2,end2]

		if val1 >= 0:
			slideshow = [end1] + slideshow
			i1 = end1
			score_mat[:,i1] = -1
		if val2 >= 0 and end2 > 0:
			slideshow = slideshow + [end2]
			i2 = end2
			score_mat[:,i2] = -1

		if val1 < 0 and val2 < 0:
			break

	# print(slideshow)
	with open(args.input + '.out', 'w') as fid:
		fid.write(str(len(slideshow)) + '\n')
		for elem in slideshow:
			inds = im_inds[elem]
			if type(inds) == int:
				inds = [inds]
			inds = list(inds)
			inds = [str(x) for x in inds]
			fid.write(' '.join(inds) + '\n')