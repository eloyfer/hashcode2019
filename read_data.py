import numpy as np
import os
from scipy import sparse

def read_data(filename):

  if not os.path.isfile(filename):
    print('Error in file name! %s' % filename)
    exit()

  tags = dict()
  hims = []
  vims = []
  i = 0
  N = 0
  tag_ind = 0
  for line in open(filename, 'r'):
    if i == 0: # ignore first line
      i += 1
      N = int(line)
      continue

    spl = line.split()
    for tg in spl[2:]:
      if tg not in tags:
        tags[tg] = tag_ind
        tag_ind += 1

    cur_tags = list(map(lambda x: tags[x], spl[2:]))
    if spl[0] == 'H':
      hims.append(cur_tags)
    elif spl[0] == 'V':
      vims.append(cur_tags)
    else:
      print('Error in file format: %s' % line)
      exit()
    
  # print(len(tags.keys()))
  # tags = [key for key,val in tags.items() if val < len(vims) + len(hims)]
  # tags = list(tags.keys())
  # tags.sort()
  print('num vertical images:', len(vims))
  print('num horizontal images:', len(hims))
  print('num tags:', len(tags))
  # order vertical images in pairs randomly
  if len(vims) > 0:
    group1 = np.random.choice(len(vims), size=len(vims)//2, replace=False)
    group2 = list(set(list(range(len(vims)))) - set(group1))
    vims2 = [set(vims[group1[i]] + vims[group2[i]]) for i in range(len(vims)//2)]

    hims = hims + vims2

  result = np.zeros([len(hims),len(tags)], int)
  # result = sparse.dok_matrix
  for i, im in enumerate(hims):
    # print(i)
    result[i,im] = 1
    # for tag in im:
      # result[i,tags.index(tag)] = 1

  return result


if __name__ == '__main__':
  mat = read_data('b_lovely_landscapes.txt')
  # mat = read_data('c_memorable_moments.txt')
  print(mat.shape)
  print(mat)


