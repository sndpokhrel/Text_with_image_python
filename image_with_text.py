from PIL import Image, ImageDraw, ImageFont, ImageColor

file_name = 'bg_pic.jpg'

img = Image.open(file_name)
draw = ImageDraw.Draw(img)

name= "John Doe"
address= "sample1"
role= "sample2"

font1 = ImageFont.truetype('arial.ttf',280)
font2 =ImageFont.truetype('Cookie-Regular.ttf',250)
font3 = ImageFont.truetype('POORICH.TTF',200)

draw.text((140,100),name, font=font1, fill='black')
draw.text((940,320),address, font=font2, fill='gray')
draw.text((1500,320),role, font=font3, fill='yellow')

img.show()
