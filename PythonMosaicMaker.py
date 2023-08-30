from ctypes import resize
import cv2 as cv

# Read image
img = cv.imread(cv.samples.findFile('C:\\Users\\ThomasWilk\\Pictures\\Monarch\\PrintCam2000014011.bmp'))

# Get height, length dimensions of original image, and channel
imgHeight, imgWidth, imgChannels = img.shape

print('Image Height = ' + str(imgHeight))
print('Image Width = ' + str(imgWidth))

# Choose how many images to put in mosaic:
imgsAcross = 10
imgsDown = 7

# Lay out mosaic
imgTileWidth = imgWidth / imgsAcross
imgTileHeight = imgHeight / imgsDown


# Create scaled down version of image
dim = (int(imgTileWidth), int(imgTileHeight))

imgScaled = cv.resize(img, dim, interpolation = cv.INTER_AREA)

# Show scaled down image
cv.imshow('Scaled down image',imgScaled)
cv.waitKey(0)
cv.destroyAllWindows()

# Tile image Across
#for i in range(0, imgsAcross):
xOffset = 0
yOffset = 0
for i in range(0, imgsAcross):
    img[ yOffset : yOffset + imgScaled.shape[0], xOffset * (i+1) : xOffset * (i+1) + imgScaled.shape[1]] = imgScaled

# Show tiled image
cv.imshow('Tiled image', img)
cv.waitKey(0)
cv.destroyAllWindows()