import numpy as np
from PIL import Image

im_ori = Image.open('./1.png')
im = Image.open('./2.png')
print(np.unique(np.array(im_ori)))
print(np.unique(np.array(im)))