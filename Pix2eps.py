import matplotlib.pyplot as plt
import matplotlib.image as img
import pathlib

class xxx2eps:
    """
    xxx to eps converter
    """
    def __init__(self, filename):
        self.filename = filename
        self.format = 'eps'
        self.dpi = 300
        self._process()
        
    def _process(self):
    
        # get extension
        path = pathlib.Path(self.filename)
        # print('Parent:', path.parent)
        # print('Filename:', path.name)
        # print('Extension:', path.suffix)
        
        # reading png image file
        im = img.imread(path.name)
          
        # Remove numbers for scales (目盛り)
        plt.xticks(color="None")
        plt.yticks(color="None")
        
        # Remove numbers for scales (目盛り)
        plt.tick_params(length=0)
        
        # show image
        plt.imshow(im)
        
        #plot
        #plt.show()
        plt.savefig(path.name+'.'+self.format, format=self.format,
                    dpi=self.dpi, transparent=True)
    
    
if __name__ == '__main__':
    
    file_name = 'hogehoge.jpg'
    xxx2eps(file_name)
    
    
