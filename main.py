import numpy as np
from PIL import Image


def rms(array1, array2):
    return np.sqrt(((array1 - array2) **2).mean())

def edges(pix_list): #get the edge and return array
    return np.array(pix_list)

#_________read the images______________
img1 = Image.open("Fr01.jpg")
img2 = Image.open("Fr02.jpg")

#_________show the images______________
img1.show()
img2.show()

#_________size of the images______________
size1 = img1.size
print(range(size1[1]))
size2 = img2.size
print(range(size2[1]))

#___________ list of pixel image 1____________
right_img1 = []
left_img1 = []
up_img1 = []
down_img1 = []

#___________ list of pixel image 2____________
right_img2 = []
left_img2 = []
up_img2 = []
down_img2 = []

#-------------------------------------------------
#بدي امر على كل البكسلات
#اول اشي بثبت الصفوف حتى اطلع البكسلات من فوق وتحت size[0]  wedth
#بعدين بثبت العمود حتى اطلع البكسلات من يمين ويسار size[1]  height


#loop on image 1
for i in range(size1[0]): # get pixel of each image on looping in size of image like (0, 468)  from width
    in_pixel = img1.getpixel((i, 0))   # append this pixels in the upperlist imag1 array
    up_img1.append(in_pixel)

# like image 1 but in (0, 469) from height
for j in range(size1[1]):
    in_pixel = img1.getpixel((size1[0] - 1, j))
    right_img1.append(in_pixel)

for i in range(size1[0]):
    in_pixel = img1.getpixel((i, size1[1] - 1))
    down_img1.append(in_pixel)

for j in range(size1[1]):
    in_pixel = img1.getpixel((0, j))
    left_img1.append(in_pixel)



# do this again for size2 from image 2 that contain width and height
for i in range(size2[0]): #from wedth
    in_pixel = img2.getpixel((i, 0))
    up_img2.append(in_pixel)

for j in range(size2[1]):  #from height
    in_pixel = img2.getpixel((size2[0] - 1, j))
    right_img2.append(in_pixel)

for i in range(size2[0]):
    in_pixel = img2.getpixel((i, size2[1] - 1))
    down_img2.append(in_pixel)

for j in range(size2[1]):
    in_pixel = img2.getpixel((0, j))
    left_img2.append(in_pixel)

#-------------------------------------------------------------------------------

#الصورتين نفس العرض والارتفاع
if size1[0] == size2[0] == size1[1] == size2[1]:
    rms_min = min(rms(edges(up_img1), edges(down_img2)),
                  rms(edges(down_img1), edges(up_img2)),
                  rms(edges(right_img1), edges(left_img2)),
                  rms(edges(left_img1), edges(right_img2)))

#----------------wedth not the same-------------------
elif size1[0] == size2[0]:
    rms_min = min(rms(edges(up_img1), edges(down_img2)),
                  rms(edges(down_img1), edges(up_img2)))

#----------------height not the same------------------
elif size1[1] == size2[1]:
    rms_min = min(rms(edges(left_img1), edges(right_img2)),
                  rms(edges(right_img1), edges(left_img2)))
#طلعت وين rms  اقل اشي بيت الصورتين الحين بدي الصق الاقل مع بعض
#_______________________________________________________
if rms_min == rms(edges(up_img1), edges(down_img2)):
    new_image = Image.new('RGB', (size1[0], (2 * size1[1])))
    new_image.paste(img2, (0, 0))
    new_image.paste(img1, (0, size2[1]))
    new_image.show()


elif rms_min == rms(edges(down_img1), edges(up_img2)):
    new_image = Image.new('RGB', (size1[0], (2 * size1[1])))
    new_image.paste(img1, (0, 0))
    new_image.paste(img2, (0, size1[1]))
    new_image.show()


elif rms_min == rms(edges(right_img1), edges(left_img2)):
    new_image = Image.new('RGB', (2 * size1[0], size1[1]))
    new_image.paste(img1, (0, 0))
    new_image.paste(img2, (size1[0], 0))
    new_image.show()


elif rms_min == rms(edges(left_img1), edges(right_img2)):
    new_image = Image.new('RGB', (2 * size1[0], size1[1]))
    new_image.paste(img2, (0, 0))
    new_image.paste(img1, (size1[0], 0))
    new_image.show()
