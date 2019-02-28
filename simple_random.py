import numpy as np
from read_data import read_data
from random import shuffle

def get_score(array):
	score1 = np.dot(array, array.T)
	score2 = np.dot(1 - array, array.T)
	score3 = np.dot(array, 1 - array.T)

	stack_the_layers = np.stack((score1, score2, score3), axis=-1)
	adj = np.min(stack_the_layers, axis=-1)
	return adj

if __name__ == '__main__':

	RANDOM_SAMPLES_PER_CHOICE = 10
	# A = read_data('b_lovely_landscapes.txt')
	# A = read_data('d_pet_pictures.txt')
	A = read_data('c_memorable_moments.txt')

	#calc scores
	adj = get_score(A)

	(rows, cols) = A.shape #rows is number of images, cols is tags
	indicies = list(range(rows))

	# Get random first im
	idx = np.random.randint(rows)
	indicies.remove(idx) # Removes from the rest
	slideshow_list = [idx]

	while len(indicies) > 0:

		# Get random 10 indicies
		random_indicies = indicies.copy()
		shuffle(random_indicies)
		random_ten_idx = random_indicies[:RANDOM_SAMPLES_PER_CHOICE]
		orig_row = adj[idx, :]

		#get best index from
		idx_score_row = adj[idx,random_ten_idx]
		best_idx = np.argmax(idx_score_row)
		chosen_idx = random_indicies[best_idx]

		# add chosen index to slideshow + remove from indices list
		slideshow_list.append(chosen_idx)
		indicies.remove(chosen_idx)

	print(slideshow_list)
	print(len(slideshow_list))





	#
	# slideshow_list = [first_im[-1]]
	#
	# rows = A.shape[0]
	# cur_im = first_im
	# while rows > 0: #While there are still images
	#
	# 	if rows > 10:
	# 		random_ten_idx = np.random.permutation(rows)[:10]
	# 		random_ten = A[random_ten_idx,:]
	#
	# 		score = get_score(random_ten, cur_im)
	# 		if score < 1:
	# 			break #adding more slides won't add to show
	#
	# 		slideshow_list.append([])
	# 	else:
	# 		#get remaining indicies list
	#
	# 		slideshow_list.append([])
	#
	# # This is final list
	# print(slideshow_list)
