import torch
import cv2
import numpy as np
from torch.utils.data import Dataset

"""
This class is going to be use to take the paths of the images and convert
them into normalized tensor images.
"""

class SegmentationDataset(Dataset):
    
    def __init__(self,df):
        
        self.df = df
        
        
    def __len__(self):
        return len(self.df)
    
    def __getitem__(self, idx):
        
        row = self.df.iloc[idx]
        
        image_path = row.Image_path
        mask_path = row.Segmentation_path
        
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) #esto estaría bien??
        
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
        mask = np.expand_dims(mask, axis=-1) #add a dimension
        
        image = np.transpose(image,(2,0,1)).astype(np.float32)
        mask = np.transpose(mask,(2,0,1)).astype(np.float32)
        
        image = torch.Tensor(image) /255.0
        mask = torch.round(torch.Tensor(mask)/ 255.0)
        
        return image,mask
        
        
        
        
