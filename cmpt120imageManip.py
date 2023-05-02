# Yet Another Image Processor
# Mahim Chaudhary:301463607 & Ariel Tyson:301458219
# December 6th, 2021.
# Define functions to use in manipulation options
# Cmpt120:D300


import cmpt120imageProjHelper as helper
import numpy
import copy


# Functions to be used in manipulation options

# Function to apply red filter to image
def applyRedFilter(pixels):
    manipulated = helper.getBlackImage(len(pixels[0]), len(pixels))
    for row in range(len(pixels)):
      for col in range(len(pixels[0])):
        manipulated[row][col][0] = pixels[row][col][0]
        manipulated[row][col][1] = 0
        manipulated[row][col][2] = 0
    
    return manipulated


# Function to apply green filter to image
def applyGreenFilter(pixels):
    manipulated = helper.getBlackImage(len(pixels[0]), len(pixels))
    for row in range(len(pixels)):
      for col in range(len(pixels[0])):
        manipulated[row][col][0] = 0
        manipulated[row][col][1] = pixels[row][col][1]
        manipulated[row][col][2] = 0
       
    return manipulated


# Function to apply blue filter to image
def applyBlueFilter(pixels):
    manipulated = helper.getBlackImage(len(pixels[0]), len(pixels))
    for row in range(len(pixels)):
      for col in range(len(pixels[0])):
        manipulated[row][col][0] = 0
        manipulated[row][col][1] = 0
        manipulated[row][col][2] = pixels[row][col][2]
    
    return manipulated


# Function to apply sepia filter to image
def applySepiaFilter(pixels):
    manipulated = helper.getBlackImage(len(pixels[0]), len(pixels))
    for row in range(len(pixels)):
      for col in range(len(pixels[0])):
        red = pixels[row][col][0]
        green = pixels[row][col][1]
        blue = pixels[row][col][2]
        if int((red*0.393) + (green*0.769) + (blue*0.189)) < 255:
          manipulated[row][col][0] = int((red*0.393) + (green*0.769) + (blue*0.189))

        else: 
          manipulated[row][col][0] = 255

        if int((red*0.349) + (green*0.686) + (blue*0.168)) < 255:
          manipulated[row][col][1] = int((red*0.349) + (green*0.686) + (blue*0.168))

        else: 
          manipulated[row][col][1] = 255

        if int((red*0.272) + (green*0.534) + (blue*0.131)) < 255:
          manipulated[row][col][2] = int((red*0.272) + (green*0.534) + (blue*0.131))

        else:
          manipulated[row][col][2] = 255

    return manipulated

# Function to Scale up color
def scaleUp(value):
  if value<64:
    return int((value/64)*80)

  elif value >= 64 and value < 128:
    return int(((value-64)/(128-64))*(160-80))+80
  
  else:
    return int(((value-128)/(255-128))*(255-160))+160

# Function to scale down color
def scaleDown(value):
  if value < 64:
    return int((value/64)*50)
  
  elif value >= 64 and value < 128:
    return int(((value-64)/(128-64))*(100-50))+50

  else:
    return int(((value-128)/(255-128))*(255-100))+100


# Function to apply warm filter to image
def applyWarmFilter(pixels):
    manipulated = helper.getBlackImage(len(pixels[0]), len(pixels))
    for row in range(len(pixels)):
      for col in range(len(pixels[0])):
        manipulated[row][col][0] = scaleUp(pixels[row][col][0])
        manipulated[row][col][1] = pixels[row][col][1]
        manipulated[row][col][2] = scaleDown(pixels[row][col][2])

    return manipulated


# Function to apply cold filter to image
def applyColdFilter(pixels):
    manipulated = helper.getBlackImage(len(pixels[0]), len(pixels))
    for row in range(len(pixels)):
      for col in range(len(pixels[0])):
        manipulated[row][col][0] = scaleDown(pixels[row][col][0])
        manipulated[row][col][1] = pixels[row][col][1]
        manipulated[row][col][2] = scaleUp(pixels[row][col][2])

    return manipulated

# Function to rotate the image to the left.
def rotateLeft(pixels):
    length = len(pixels)
    width = len(pixels[0])
    manipulated = helper.getBlackImage(length, width)
    for row in range(length):
      for col in range(width):
        manipulated[width-1-col][row] = pixels[row][col]

    return manipulated


# Function to rotate the image to the right
def rotateRight(pixels):
    length = len(pixels)
    width = len(pixels[0])
    manipulated = helper.getBlackImage(length, width)
    for row in range(length):
      for col in range(width):
        manipulated[col][length-1-row] = pixels[row][col]

    return manipulated


# Function to half the size of image
def halfSize(pixels):
    length = len(pixels)
    width = len(pixels[0])
    manipulated = helper.getBlackImage(int(width/2), int(length/2))
    for row in range(length-1):
      for col in range(width-1):
        r1 = pixels[row][col][0]
        r2 = pixels[row+1][col][0]
        r3 = pixels[row][col+1][0]
        r4 = pixels[row+1][col+1][0]
        r_avg = int((r1+r2+r3+r4)/4)
        g1 = pixels[row][col][1]
        g2 = pixels[row+1][col][1]
        g3 = pixels[row][col+1][1]
        g4 = pixels[row+1][col+1][1]
        g_avg = int((g1+g2+g3+g4)/4)
        b1 = pixels[row][col][2]
        b2 = pixels[row+1][col][2]
        b3 = pixels[row][col+1][2]
        b4 = pixels[row+1][col+1][2]
        b_avg = int((b1+b2+b3+b4)/4)
        manipulated[int(row/2)][int(col/2)] = [r_avg, g_avg, b_avg]

    return manipulated


# Function to double size image
def doubleSize(pixels):
    length = len(pixels)
    width = len(pixels[0])
    manipulated = helper.getBlackImage(2*width, 2*length)
    for row in range(length):
      for col in range(width):
        manipulated[2*row][2*col] = pixels[row][col]
        manipulated[2*row][2*col+1] = pixels[row][col]
        manipulated[2*row+1][2*col] = pixels[row][col]
        manipulated[2*row+1][2*col+1] = pixels[row][col]

    return manipulated


# Function to locate fish in image
def locateFish(pixels):
  length = len(pixels)
  width = len(pixels[0])
  manipulated = copy.deepcopy(pixels)
  upperBorder = 0
  lowerBorder = 0
  leftBorder = 0
  rightBorder = 0
  fishFound = False

  for row in range(length):
    for col in range(width):
      hsv = helper.rgb_to_hsv(pixels[row][col][0],pixels[row][col][1],pixels[row][col][2])
      h = hsv[0]
      s = hsv[1]
      v = hsv[2]

      if 70 >= h >= 55 and 100 >= s >= 45 and 100 >= v >= 80:
        if fishFound == False:
          upperBorder = row
          leftBorder = col
          rightBorder = col
        lowerBorder = row

        if col<leftBorder:
          leftBorder = col
          
        if col>rightBorder:
          rightBorder = col
        fishFound = True

  if fishFound == True:
    for row in range(length):
      for col in range(width):
        if row == upperBorder and col>=leftBorder and col<=rightBorder:
          manipulated[row][col] = [0,255,0]

        if row == lowerBorder and col>=leftBorder and col<=rightBorder:
          manipulated[row][col] = [0,255,0]

        if col == leftBorder and row>=upperBorder and row<=lowerBorder:
          manipulated[row][col] = [0,255,0]

        if col == rightBorder and row>=upperBorder and row<=lowerBorder:
          manipulated[row][col] = [0,255,0]

  return manipulated