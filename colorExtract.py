
from PIL import Image
import numpy as np


def extractColors(file_, ch):
    im = Image.open(file_)
    img_ = im.load()
    img_mat = np.array(im)

    size_ = img_mat.shape[0]

    if(ch == 2):
        channels = ['__r_.', '__g_.', '__b_.', '__rg_.', '__gb_.', '__rb_.']
        values = [[1, 0, 0], [0, 1, 0], [0, 0, 1],
                  [1, 1, 0], [0, 1, 1], [1, 0, 1]]
    elif(ch == 1):
        channels = ['__r_.', '__g_.', '__b_.']
        values = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    for (channel, value) in zip(channels, values):
        success_ = 0
        new_i = []
        name = channel[2]

        for row_ in img_mat:
            row_new = []
            for pix_ in row_:
                dotCol = [pix_[0]*value[0], pix_[1]*value[1], pix_[2]*value[2]]
                row_new.append(dotCol)
            new_i.append(row_new)
            success_ += 1
            print('\r Completed : ', name, str(
                round(success_*100/size_, 2))+'%  ', end='')
        new_i = np.array(new_i)

        img_x = Image.fromarray(new_i.astype(np.uint8))

        fileX = file_.rsplit('.', 1)
        fileX.insert(1, channel)
        fileX = ''.join(fileX)
        print('Created', fileX, '   ----------   Saving Now')
        print('\n')
        img_x.save(fileX)
