from PIL import Image, ImageDraw, ImageFont

sourceFileName = "/Users/Yu/Desktop/yu.png"
avatar         = Image.open(sourceFileName)
drawAvatar     = ImageDraw.Draw(avatar)

xSize, ySize = avatar.size
fontSize     = min(xSize, ySize) // 11

myFont       = ImageFont.truetype("/Library/Fonts/OsakaMono.ttf", fontSize)

drawAvatar.text([0.9 * xSize, 0.1 * ySize - fontSize],\
    "3", fill = (255, 0, 0), font = myFont)
del drawAvatar

avatar.show()