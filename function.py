from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import cv2
import numpy as np

classes = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy',
 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
 'Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight',
 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
 'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot',
 'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus',
 'Tomato_healthy']

def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None :
            image = cv2.resize(image, tuple((256, 256)))
            return img_to_array(image)
        else :
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None

def evaluate(image_location):
    loaded_model = load_model(f"./model.h5")
    
    im=convert_image_to_array(image_location)
    np_image_li = np.array(im, dtype=np.float16) / 255.0
    npp_image = np.expand_dims(np_image_li, axis=0)

    result = loaded_model.predict(npp_image)

    itemindex = np.where(result==np.max(result))
    #print(itemindex[1][0]) #for testing
    #print("probability:"+str(np.max(result)))
    return classes[itemindex[1][0]] 
   
#print(evaluate('/home/debjyoti/Devs/leaf_dis/src/image/414f6249-9f78-4af5-9593-9d5a7e7d979f___RS_HL 1918.JPG')) # for testing

