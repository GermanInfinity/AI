from PIL import Image 

class image_diff:
    def __init__(self, image1, img_save1, image2, img_save2):
        self.image1= image1
        self.image2= image2
        self.img_save_name1 = img_save1
        self.img_save_name2 = img_save2
        
    def blackened_white(self):
        """Black and white images"""
        image_file1 = Image.open(self.image1) # open colour image
        image_file1 = image_file1.convert('1') # convert image to black and white
        image_file1.save(self.img_save_name1+'.png')
        
        image_file2 = Image.open(self.image2) # open colour image
        image_file2 = image_file2.convert('1') # convert image to black and white
        image_file2.save(self.img_save_name2+'.png')
        
    def compare(self):
        """Compare images"""

        i1 = Image.open(self.img_save_name1+'.png')
        i2 = Image.open(self.img_save_name2+'.png')
        
        assert i1.mode == i2.mode, "Different kinds of images."
        assert i1.size == i2.size, "Different sizes."
         
        pairs = zip(i1.getdata(), i2.getdata())
        if len(i1.getbands()) == 1:
            # for gray-scale jpegs
            dif = sum(abs(p1-p2) for p1,p2 in pairs)
        else:
            dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
         
        ncomponents = i1.size[0] * i1.size[1] * 3
        return ((dif / 255.0 * 100) / ncomponents)
                
            
        
