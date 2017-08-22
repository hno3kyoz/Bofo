import os
from PIL import Image

for infile in filelist:
    outfile = os.path.splitext(infile)[0]+".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print('Cannot covert'),infile