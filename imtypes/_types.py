import numpy as np
from typing import NewType, Union as U, Tuple as Tup


# Base image type: an Image is just a NumPy array
AnyImage = NewType('AnyImage', np.ndarray)

# Single Channel image
Image = NewType('Image', AnyImage)

# 2D image types: a subtype of Image that is 2D only
Image2D = NewType('Image2D', Image)

# Multichannel images: a NumPy array in which the last dimension
# represents "channels", ie measurements of different information at the same
# coordinates
ImageCh = NewType('ImageCh', AnyImage)

# Multichannel 2D images: a subtype of ImageCh restricted to only two channels
ImageCh2D = NewType('ImageCh2D', ImageCh)


AnyImage2D = U[Image2D, ImageCh2D]


Sigma = U[float, Tup[float, ...]]

Spacing = U[float, Tup[float, ...]]
