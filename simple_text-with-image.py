from PIL import Image, ImageDraw, ImageFont, ImageColor

img = Image.new(mode="RGBA", size=(1290,1080), color='darkorange')
draw = ImageDraw.Draw(img)
text = "Hello world!"
font = ImageFont.truetype('arial.ttf',163)
draw.text((100,100), text, font=font, fill='black')
img.show()