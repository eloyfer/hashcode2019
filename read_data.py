import numpy as np
import os

def read_data(filename):

  if not os.path.isfile(filename):
    print('Error in file name! %s' % filename)
    exit()

  tags = set()
  hims = []
  vims = []
  i = 0
  N = 0
  for line in open(filename, 'r'):
    if i == 0: # ignore first line
      i += 1
      N = int(line)
      continue

    spl = line.split()
    if spl[0] == 'H':
      hims.append(spl[2:])
    elif spl[0] == 'V':
      vims.append(spl[2:])
    else:
      print('Error in file format: %s' % line)
      exit()
    tags.update(spl[2:])

  # order vertical images in pairs randomly
  if len(vims) > 0:
    group1 = np.random.choice(len(vims), size=len(vims)//2, replace=False)
    group2 = list(set(list(range(len(vims)))) - set(group1))
    vims2 = [set(vims[group1[i]] + vims[group2[i]]) for i in range(len(vims)//2)]

    hims = hims + vims2

  tags = sorted(list(tags))
  result = np.zeros([len(hims),len(tags)], int)
  for i, im in enumerate(hims):
    for tag in im:
      result[i,tags.index(tag)] = 1

  return result


if __name__ == '__main__':
  mat = read_data('b_lovely_landscapes.txt')
  print(mat.shape)
  print(mat)


