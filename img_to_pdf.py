from PIL import Image
#method1
'''path = 'E:\sample\me.jfif'
pdf = Image.open(path)
pdf.save('E:\sample\me.pdf')'''

#method2
image_1 = Image.open(r'E:\sample\me.jfif')
image_2 = Image.open(r'E:\sample\img1.png')
image_3 = Image.open(r'E:\sample\drwaing.png')
im_1 = image_1.convert('RGB')
im_1.save(r'E:\sample\me.png')
image_4= Image.open(r'E:\sample\me.png')

im_2 = image_2.convert('RGB')#we convert it into RBG because PNG files are in RGBA mode and pdf does not support RGBA mode it supports only RGB Morever for jpg files there is no need to convert into RGB bcz jpg or jpeg are in RGB mode only
im_3 = image_3.convert('RGB')
im_4 = image_4.convert('RGB')

image_list = [ im_3, im_4]
im_2.save(r'E:\sample\my_images.pdf',save_all=True, append_images=image_list)



