from PIL import Image 
import numpy as np
## This code produces 6 flags from various Countries. It utilizes PIL and NumPY in order to create 6 unique flag designs.

# How to use: 
# 1. Run python flag.py
# 2. The flags should appear as PNGs inside the flag.py file loction

class flag:
    def __init__(self, width, height):
        self.width = width
        self.height = height

## This class creates the french flag 
class frenchFlag(flag):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.name = "French Flag"
        print("French initalizing")

        def setColors(self):
            print("Setting Colors")

        width = self.width
        height = self.height

        stripe_width = width // 3

        data = np.zeros ((height, width, 3), dtype=np.uint8)
## Colors 
        French_blue = [0, 85, 164]
        French_white = [255, 255, 255]
        French_red = [239, 65, 53]

## Color parameters 
        for y in range(height):
            for x in range(width):
                if x < stripe_width:
                    data[y, x] = French_blue
                elif x < 2 * stripe_width: 
                    data[y, x] = French_white
                else:
                    data[y, x] = French_red

        img = Image.fromarray(data, 'RGB')
        img.save("french_flag.png")

## This class creates the Estonian flag 
class estoniaFlag(flag):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.name = "Estonia Flag"
        print("Estonian initalizing")

        def setColors(self):
            print("Setting Colors")

        width = self.width
        height = self.height

        stripe_height = height // 3

        data = np.zeros ((height, width, 3), dtype=np.uint8)
## Colors 
        Estonian_blue = [0, 114, 206]
        Estonian_white = [255, 255, 255]
        Estonian_Black = [000, 000, 000]

## Color parameters 
        for y in range(height):
            for x in range(width):
                if y < stripe_height:
                    data[y, x] = Estonian_blue
                elif y < 2 * stripe_height: 
                    data[y, x] = Estonian_Black
                else:
                    data[y, x] = Estonian_white

        img = Image.fromarray(data, 'RGB')
        img.save("Estonian_flag.png")

## This class creates the Finnish Flag
class finnishFlag(flag):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.name = "Finnish Flag"
        print("Finnish initalizing")

        def setColors(self):
            print("Setting Colors")

        width = self.width
        height = self.height
## Colors 
        Finnish_blue = [0, 53, 128]
        Finnish_white = [255, 255, 255]

## Color Parameters
        vertical_column_width = width // 9
        horizontal_column_height = height // 5

        vertical_center_width = width // 3
        horizontal_center_height = height // 2

        vertical = vertical_center_width - vertical_column_width // 2
        vertical_end = vertical_center_width + vertical_column_width // 2 

        horizontal = horizontal_center_height - horizontal_column_height // 2
        horizontal_end = horizontal_center_height + horizontal_column_height // 2

        data = np.zeros ((height, width, 3), dtype=np.uint8)

       
        for y in range(height):
            for x in range(width):
                if (vertical <= x < vertical_end) or (horizontal <= y <horizontal_end):
                    data[y, x] = Finnish_blue
                else:
                    data[y, x] = Finnish_white

        img = Image.fromarray(data, 'RGB')
        img.save("finnish_flag.png")

## This class creates the belgium flag
class belgiumFlag(flag):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.name = "Belgium Flag"
        print("Belgium initalizing")

        def setColors(self):
            print("Setting Colors")

        width = self.width
        height = self.height

        stripe_width = width // 3

        data = np.zeros ((height, width, 3), dtype=np.uint8)
## Colors 
        Belgium_black = [0, 0, 0]
        Belgium_yellow = [255, 233, 54]
        Belgium_red = [239, 65, 53]
## Color parameters
        for y in range(height):
            for x in range(width):
                if x < stripe_width:
                    data[y, x] = Belgium_black
                elif x < 2 * stripe_width: 
                    data[y, x] = Belgium_yellow
                else:
                    data[y, x] = Belgium_red

        img = Image.fromarray(data, 'RGB')
        img.save("belgium_flag.png")

## This class creates the Japanese flag
class japaneseFlag(flag):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.name = "Japanese Flag"
        print("Japanese initalizing")

        def setColors(self):
            print("Setting Colors")

        width = self.width
        height = self.height

        stripe_width = width // 1

        data = np.zeros ((height, width, 3), dtype=np.uint8)
## Colors 
        Japanese_white = [255, 255, 255]

## Color parameters
        for y in range(height):
            for x in range(width):
                if x < stripe_width:
                    data[y, x] = Japanese_white

## Convert NumPy array into a PIL image
            img = Image.fromarray(data, 'RGB')

## Overlay red circle onto image
            overlay = Image.open("red_circle.png").convert("RGBA")

## sizing
            overlay = overlay.resize((150,150))   

            img = img.convert("RGBA")
            img.paste(overlay, (225,75), overlay)
             
            
            img.save("Japanese_flag.png")


## This class creates the Canadian flag
class canadianFlag(flag):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.name = "Canadian Flag"
        print("Canadian initalizing")

        def setColors(self):
            print("Setting Colors")

        width = self.width
        height = self.height

        stripe_width = width // 3

        data = np.zeros ((height, width, 3), dtype=np.uint8)
## Colors 
        Canadian_white = [255, 255, 255]
        Canadian_red = [255, 0, 0]

## Color parameters
        for y in range(height):
            for x in range(width):
                if x < stripe_width:
                    data[y, x] = Canadian_red
                elif x < 2 * stripe_width: 
                    data[y, x] = Canadian_white
                else:
                    data[y, x] = Canadian_red

## Convert NumPy array into a PIL image
            img = Image.fromarray(data, 'RGB')

## Overlay red circle onto image
            overlay = Image.open("leaf.png").convert("RGBA")

## sizing
            overlay = overlay.resize((150,150))   

            img = img.convert("RGBA")
            img.paste(overlay, (225,75), overlay)
             
            
            img.save("Canadian_flag.png")

## Create Flags 
frenchFlag(600,300)
estoniaFlag(600,300)
finnishFlag(600,300)
belgiumFlag(600,300)
japaneseFlag(600,300)
canadianFlag(600,300)