import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] > 200:
                hit("down")
                return

    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] > 200:
                hit("up")
                return
    return

if __name__ == "__main__":
   
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        # print(asarray(image))
        '''
        # Draw the rectangle for cactus
        for i in range(275, 325):
            for j in range(563, 650):
    e            data[i, j] = 0
   s     
  o      # Draw the rectangle for birds
 l       for i in range(250, 300):
c            for j in range(410, 563):
                data[i, j] = 171

        image.show()
        break
      '''


'''I have tried the code when the obstacles or the cactus changes the colour from black to white.
So what you have to do is just assume any pixel or dot on the screen as the screen is white in day time and changes to black in night and similarly change the colour of cactus or obstacle detection to black and white respectively in the IF condition as coded below
            if data[80,120]>200 and data[m,n]<100:# data[80,120] is a pixel on screen and >200 recognizes the day time or white screen and data[m,n]<100 recognizes the black cactus or obstacles
                return True
            elif data[80,120]<100 and data[m,n]>120:# data[80,120] is a pixel on screen and <100 recognizes the night time or black screen and data[m,n]>120 recognizes the white cactus or obstacles 

                return True
Note: Elif is used because either it will be day or night
Let me know if it works fine for you guys too #HappyCoding
'''
