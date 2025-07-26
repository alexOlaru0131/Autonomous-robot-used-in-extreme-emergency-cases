# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 14:35:26 2025

@author: alexo
"""

import cv2
import numpy as np
import ArducamDepthCamera as ac

MAX_DISTANCE = 4000
confidence_value = 30

def getPreviewRGB(preview: np.ndarray, confidence: np.ndarray) -> np.ndarray:
    preview = np.nan_to_num(preview)
    preview[confidence < confidence_value] = (0, 0, 0)
    return preview

def on_confidence_changed(value):
    global confidence_value
    confidence_value = value
    
def main():
    cam = ac.ArducamCamera()
    ret = cam.open(ac.Connection.CSI, 0)
    ret = cam.start(ac.FrameType.DEPTH)
    cam.setControl(ac.Control.RANGE, MAX_DISTANCE)
    r = cam.getControl(ac.Control.RANGE)
    
    while True:
        frame = cam.requestFrame(2000)
        if frame is not None and isinstance(frame, ac.DepthData):
            depth_buf = frame.depth_data
            confidence_buf = frame.confidence_data
            
            result_image = (depth_buf * (255.0 / r)).astype(np.uint8)
            result_image = cv2.applyColorMap(result_image, cv2.COLORMAP_RAINBOW)
            result_image = getPreviewRGB(result_image, confidence_buf)
            
            cv2.normalize(confidence_buf, confidence_buf, 1, 0, cv2.NORM_MINMAX)
            
            cam.releaseFrame(frame)
            
    cam.stop()
    cam.close()
            