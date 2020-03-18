from .coco import CocoDataset
#import os.path as osp
from .registry import DATASETS

#import mmcv
#import numpy as np
#from mmcv.parallel import DataContainer as DC
#from torch.utils.data import Dataset
#
#from .transforms import (ImageTransform, BboxTransform, MaskTransform,
#                         SegMapTransform, Numpy2Tensor)
#from .utils import to_tensor, random_scale
#from .extra_aug import ExtraAugmentation
@DATASETS.register_module
class MyDataset(CocoDataset):

    CLASSES = ('as', 'ad', 'cn', 'dp', 'ep', 'lt', 'cl', 'cy', 'ct', 'pr', 'rt1', 'rt2', 'rt3', 'rt4', 'tp', 'tr', 'vt')
