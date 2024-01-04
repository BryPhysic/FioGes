from ultralytics import YOLO
from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
moldel4 = YOLO('study/Models/Best Model definitivo.pt')
new_image = 'Testimages/Metaplasia_300.png'

pil = Image.open(new_image).convert('RGB')



from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def predict(image, conf=None):
    # Establecer un valor predeterminado para 'conf' si no se proporciona
    if conf is None:
        conf = 0.5
    
    new_results = moldel4.predict(image, conf=conf) 
    
    new_result_array = new_results[0].plot()
    new_result_array = np.array(new_result_array)
    new_result_image = Image.fromarray(new_result_array.astype('uint8'), 'RGB')  
    return new_result_image

#predict(pil)