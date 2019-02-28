import numpy as np
import os
from scipy.sparse import dok_matrix
from scipy.sparse import csr_matrix

def read_data(filename, sparse=False):

  if not os.path.isfile(filename):
    print('Error in file name! %s' % filename)
    exit()

  tags = dict()
  hims = []
  vims = []
  hims_inds = []
  vims_inds = []
  first_line = True
  i = 0
  tag_ind = 0
  for line in open(filename, 'r'):
    if first_line: # ignore first line
      first_line = False
      continue

    spl = line.split()
    for tg in spl[2:]:
      if tg not in tags:
        tags[tg] = tag_ind
        tag_ind += 1

    cur_tags = sorted(list(map(lambda x: tags[x], spl[2:])))
    if spl[0] == 'H':
      hims.append(cur_tags)
      hims_inds.append(i)
      i += 1
    elif spl[0] == 'V':
      vims.append(cur_tags)
      vims_inds.append(i)
      i += 1
    else:
      print('Error in file format: %s' % line)
      exit()

  print('num vertical images:', len(vims))
  print('num horizontal images:', len(hims))
  print('num tags:', len(tags))
  # order vertical images in pairs randomly
  im_inds = hims_inds
  if len(vims) > 0:
    group1 = np.random.choice(len(vims), size=len(vims)//2, replace=False)
    group2 = list(set(list(range(len(vims)))) - set(group1))
    vims2 = [sorted(list(set(vims[group1[i]] + vims[group2[i]]))) for i in range(len(vims)//2)]

    hims = hims + vims2
    vims_inds = np.array(vims_inds)
    im_inds += list(zip(vims_inds[group1], vims_inds[group2]))

  if not sparse:
    result = np.zeros([len(hims),len(tags)], np.int8)
  else:
    result = dok_matrix((len(hims),len(tags)), np.int8)

  for i, im in enumerate(hims):
    # print(i)
    # print(im)
    result[i,im] = 1
    # for tag in im:
      # result[i,tags.index(tag)] = 1

  result = result.tocsr().astype(np.int8)
  return result, im_inds


if __name__ == '__main__':
  mat, im_inds = read_data('b_lovely_landscapes.txt', sparse=True)
  # mat, im_inds = read_data('c_memorable_moments.txt', sparse=True)
  # print(im_inds)
  print(mat.shape)
  print(type(mat))
  # print(mat)
  print('nonzeros of row 0:', np.nonzero(mat[0]))
  print('num nonzero of row 1:', mat[1].sum())
  print('row 2:', mat[2])

