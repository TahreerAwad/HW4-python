import numpy as np
from PIL import Image


def rms(array1, array2):
    return np.sqrt(((array1 - array2) **2).mean())

def edges(pix_list): #get the edge and return array
    return np.array(pix_list)

#_________read the images______________
img1 = Image.open("Jerusalem01.jpg")
img2 = Image.open("Jerusalem02.jpg")

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
#اول اشي بثبت الصفوف حتى اطلع البكسلات من فوق وتحت size[0]  لفوق وتحت
#بعدين بثبت العمود حتى اطلع البكسلات من يمين ويسار size[1]  يمين ويسار
# وهيك بعمل لباقي الاطراف للصورتين


#-----------------up image1 -------------------------
for i in range(size1[0]):  # امشي على الصفوف واحد واحد  وبثبت العمود
    in_pixel = img1.getpixel((i, 0)) #
    up_img1.append(in_pixel) # بدي اضيفها على list up_img1

#-----------------down image1 -------------------------
for i in range(size1[0]):  # امشي على الصفوف واحد واحد  وبثبت العمود
    in_pixel = img1.getpixel((i, 0))
    down_img1.append(in_pixel)

#-----------------right image1 -------------------------
for i in range(size1[1]):  # امشي على العمود واحد واحد  وبثبت الصفوف
    in_pixel = img1.getpixel((i, 0))
    right_img1.append(in_pixel)

#-----------------left image1 -------------------------
for i in range(size1[1]):  # امشي على العمود واحد واحد  وبثبت الصفوف
    in_pixel = img1.getpixel((i, 0))
    left_img1.append(in_pixel)

#-------------------------------------------------------------------------------
# -----------------up image2 -------------------------
for i in range(size2[0]):  # امشي على الصفوف واحد واحد  وبثبت العمود
    in_pixel = img2.getpixel((i, 0))
    up_img2.append(in_pixel)

# -----------------down image2 -------------------------
for i in range(size2[0]):  # امشي على الصفوف واحد واحد  وبثبت العمود
    in_pixel = img2.getpixel((i, 0))
    down_img2.append(in_pixel)

# -----------------right image2 -------------------------
for i in range(size2[1]):  # امشي على العمود واحد واحد  وبثبت الصفوف
    in_pixel = img2.getpixel((i, 0))
    right_img2.append(in_pixel)

# -----------------left image2 -------------------------
for i in range(size2[1]):  # امشي على العمود واحد واحد  وبثبت الصفوف
    in_pixel = img2.getpixel((i, 0))
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
