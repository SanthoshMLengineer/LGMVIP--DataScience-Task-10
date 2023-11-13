from tensorflow.keras.models import load_model

import cv2

import numpy as np

from logging_utils import logger

dict_num_cate = {0:"angry",
                       1:"disgust",
                       2:"fear",
                       3:"happy",
                       4:"neutral",
                       5:"sad",
                       6:"surprise"
                    }
model = load_model('.//..//dataFiles//best_cnn_model.h5')


def recognize_images(image):
    """
    This function gives prediction from
    model for input image
    image: np.array
        image in numpy.ndarray
    prediction:str
        prediction from the model
    """
    try:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        image = cv2.resize(img,(64,64))
        img = image.reshape(1,64,64,1)
        img = img/255.0

        prediction = model.predict(img)
        p = np.argmax(prediction)
        return dict_num_cate[p]
    except Exception as e:
        logger.error("Something went wrong while extracting "
                    +"faces from mtcnn"
                     + f": {e}", exc_info=True)
        raise e
   