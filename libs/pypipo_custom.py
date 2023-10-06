# -*- coding: utf-8 -*-

import cv2
import sys
import numpy as np
from tqdm import trange
from collections import defaultdict
from scipy.spatial import distance as dist
from pypipo.libs.process import Painting

class PaintingWithData(Painting):
    """Change image to painting image.
    
    Parameters
    ----------
    filepath : str
        File path that you want to convert

    Attributes
    ----------
    original_img : np.array
        Input original image
    painting : np.array
        Color clustered image (Applied K-Means Algorithm)
    color_rbg_values : np.array
        Clustered color data list
    """

    def __init__(self, bytes_data):
        self.original_img = cv2.imdecode(np.fromstring(bytes_data, dtype = np.uint8), cv2.IMREAD_COLOR)
        self.clustered_colors = np.array([])
        return 
