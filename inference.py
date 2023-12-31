from ultralytics import YOLO
from PIL import Image
import numpy as np


import matplotlib.pyplot as plt

moldel4 = YOLO('study/Models/TrainbestG.pt')



new_image = '/Users/bryphy/Proyectos/FioGes/Testimages/Metaplasia_439.png'
new_results = moldel4.predict(new_image, conf=0.8) 

new_result_array = new_results[0].plot()
plt.figure(figsize=(12, 12))
plt.imshow(new_result_array)
plt.show()