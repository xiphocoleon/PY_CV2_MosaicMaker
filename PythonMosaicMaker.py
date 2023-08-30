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
# Insert first tiled image:
img[yOffset : yOffset + imgScaled.shape[0], xOffset : xOffset + imgScaled.shape[1]] = imgScaled

# Insert rest of images:
for i  in range(0, imgsDown):
    for j in range(0, imgsAcross):

        img[(i * int(imgTileHeight)) : (i * int(imgTileHeight)) + imgScaled.shape[0], ((j) * int(imgTileWidth)) : (j * int(imgTileWidth)) + imgScaled.shape[1] ] = imgScaled


#Scale down large image to screen size
img = cv.resize(img, [1920, 1080], interpolation = cv.INTER_AREA)

cv.imshow('Tiled image', img)
cv.waitKey(0)
cv.destroyAllWindows()
