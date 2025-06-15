from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import cv2
import numpy as np

classes = ['Potato Healthy', 'Pepper Bell Healthy', 'Tomato Leaf Mold', 'Tomato Spider Mites - Two Spotted Spider Mite', 'Tomato Early Blight', 'Tomato Yellow Leaf Curl Virus', 'Potato Late blight',
           'Tomato Late Blight', 'Tomato Healthy', 'Potato Early Blight', 'Tomato Target Spot', 'Tomato Bacterial Spot', 'Tomato Mosaic Virus', 'Pepper Bell Bacterial Spot', 'Tomato Septoria Leaf Spot']


def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None:
            image = cv2.resize(image, tuple((256, 256)))
            return img_to_array(image)
        else:
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None


def evaluate(image_location):
    loaded_model = load_model(f"./model.h5")

    im = convert_image_to_array(image_location)
    np_image_li = np.array(im, dtype=np.float16) / 255.0
    npp_image = np.expand_dims(np_image_li, axis=0)

    result = loaded_model.predict(npp_image)

    itemindex = np.where(result == np.max(result))
    # print(itemindex[1][0]) # for testing
    # print("probability:"+str(np.max(result))) # for testing
    return classes[itemindex[1][0]]

# print(evaluate('<image location>')) # for testing
