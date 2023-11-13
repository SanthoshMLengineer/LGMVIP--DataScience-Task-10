from os.path import join,isdir
from os import getcwd,mkdir
from os import scandir,remove

import cv2
from mtcnn.mtcnn import MTCNN

from recognize_emotions import recognize_images
from logging_utils import logger

present_working_directory = getcwd()

input_images = join(
                     present_working_directory,
                     "input_images"
                     )

detector = MTCNN()


def detect_face(faceCascade, image):
    '''
    function which detects the faces in an images, returns the bounding-box
    cordinates and draws an rectangle around the given co-ordinates.
    
    input parameters : 
        faceCascade : an object an class haarcascade_frontalface_default
        image       : image against which the faces to be detected
        
    return parameters :
        image  : image having detected faces in bounding box
    '''
    try:
        faces = detector.detect_faces(image)
        logger.info("faces extracted")
        return faces
    except Exception as e:
        logger.error("Something went wrong while extracting "
                    +"faces from mtcnn"
                     + f": {e}", exc_info=True)
        raise e
    


def recognize_face_expression(filename):
    """
    This function detects the faces and predicts
    the emotion
    Parameters
    ----------
    filename: str
            Input image file name
    Predictions:list()
            Prediction in a list format

    """
    image_path = join(input_images, filename)

    img = cv2.imread(image_path)
    faces = detect_face(detector, img)
    try:
        predictions = []
        for counter, face in enumerate(faces):
            confidence = face['confidence']
            if confidence > 0.80:
                x, y, w, h = face['box']
                crop_face_img = img[y:y+h, x:x+w]
                predictions.append(recognize_images(crop_face_img))
        return predictions
    except Exception as e:
        logger.error("Something went wrong while getting prediction "
                    +"from model"
                     + f": {e}", exc_info=True)
        raise e
    

    
    
    
    
    
    
    
    
    
    
    
