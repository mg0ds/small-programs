# OpenCV version

import cv2

dog = "dog.jpeg"
ascii_color = "@#$820O1?l!xaovcui;:>*=-',. "
new_txt_img = "ascii_img.txt"

img = cv2.imread(dog)
print(img.shape)

scale_percent = 2  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int((img.shape[0] * scale_percent / 100) * 0.5)
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape)

"""
cv.imshow("Resized image", resized)
cv.waitKey(0)
cv.destroyAllWindows()
"""

all_pixels = []
ascii_image = []

for y in range(resized.shape[0]):
    all_pixels.append([])
    new_str_line = ""
    for x in range(resized.shape[1]):
        pixel = resized[y, x]
        bw_value = int(sum(pixel)/3)
        all_pixels[y].append(bw_value)
        char = ascii_color[int(bw_value / len(ascii_color))]
        new_str_line += char
    new_str_line += "\n"
    ascii_image.append(new_str_line)

#print(all_pixels)
print(len(ascii_image[0]))
print(len(ascii_image))
with open(new_txt_img, 'w') as f:
    f.write(str(ascii_image))

print(*ascii_image)


# PILLOW version
"""from PIL import Image

dog = "dog.jpeg"
#ascii_color = " .,-=*:;coa!?0123456789$W#@"
#ascii_color = "@#W$9876543210?!aoc;:*=-,. "
ascii_color = "@#$820O1?l!xaovcui;:>*=-',. "
new_txt_img = "ascii_img.txt"

im = Image.open(dog)
(width, height) = (im.width // 40, im.height // 80)
print(im.width, im.height)
print(width, height)
im_resized = im.resize((width, height))

pixels = im_resized.load()
all_pixels = []
ascii_image = []
for y in range(height):
    all_pixels.append([])
    new_str_line = ""
    for x in range(width):
        pixel = pixels[x, y]
        bw_value = int(sum(pixel)/3)
        all_pixels[y].append(bw_value)
        char = ascii_color[int(bw_value / len(ascii_color))]
        new_str_line += char
    new_str_line += "\n"
    ascii_image.append(new_str_line)


#print(all_pixels)
print(len(ascii_image[0]))
print(len(ascii_image))
with open(new_txt_img, 'w') as f:
    f.write(str(ascii_image))

print(*ascii_image)

"""
