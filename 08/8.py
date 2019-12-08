import numpy as np

# digits = [int(i) for i in"123456789012"]
digits = [int(i) for i in open('input.txt', 'r').read().strip()]

size = (6,25)
layers = np.array(digits).reshape((-1,size[0]*size[1]))

# Part 1
zeros = np.apply_along_axis(lambda l: sum(l == 0), 1, layers)
min0 = np.argmin(zeros)
print("Part 1: ", sum(layers[min0] == 1) * sum(layers[min0] == 2))

# Part 2
layers = np.array(digits).reshape((-1,*size))
composite = np.apply_along_axis(lambda x: x[np.where(x != 2)[0][0]], axis=0, arr=layers)

# ASCII art version:
print("Part 2:")
print("\n".join(''.join(u" ♥️"[int(i)] for i in line) for line in composite))

# Optional: using Pillow
from PIL import Image
img_array = ((1-composite)*255).astype('int8')
img = Image.fromarray(img_array).resize((img_array.shape[1]*10, img_array.shape[0]*10))
img.show()
