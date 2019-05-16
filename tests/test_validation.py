from __future__ import annotations


import numpy as np
from scipy import ndimage as ndi
from imtypes import Image, Sigma
from typing import get_type_hints


def gaussian_filter(image : Image, sigma : Sigma) -> Image:
    out = ndi.gaussian_filter(image, sigma)
    return out


def test_gaussian_annots():
    pass


def test_gaussian_check():
    image : Image = np.random.random((50, 50))
    out = gaussian_filter(image, 3.)
