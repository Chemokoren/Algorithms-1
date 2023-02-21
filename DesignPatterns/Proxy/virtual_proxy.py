"""
"""
class Bitmap:
    
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image from {filename}')
        
    def draw(self):
        print(f'Drawing image {self.filename}')
        
        
def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')
    
class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self.bitmap = None
        
    def draw(self):
        if not self.bitmap:
            self.bitmap = Bitmap(self.filename)
        self.bitmap.draw()
    
if __name__=='__main__':
    bmp = LazyBitmap('facepalm.jpg')
    draw_image(bmp)
    draw_image(bmp)