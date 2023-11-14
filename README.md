# Face Expression Recognition(Letsgrowmore--More Adavnced Level Task)

## Problem Statement
Develop a system that recognizes facial expressions of input image and recommends the genre of music based on the detected emotions. 
The system will enhance user experience by providing personalized music genre recommendations aligned with their current emotional state. 

## Dataset Information
The dataset was taken from Kaggle (
URL: https://www.kaggle.com/datasets/msambare/fer2013), 
This dataset contains images for each emotion. There are 7 emotion are their in this data set
1.	Angry
2.	Disgust
3.	Fear
4.	Happy
5.	Neutral
6.	Sad
7.	Surprise


## Technical Details
The mainly divided into three parts
1. Image preprocessing:
           1. Image are converted into grayscale. And resized to (64, 64).
           2. And image is scaled so that model performs well on scaled data.
2. Model building and Evaluation:
           1. In this we will split dataset into two parts training and testing sets.
           2. We will use various algorithm CNN, VGG16, CRNN.
           3. Among all these models CNN performs well so we use this CNN model for production.
3. Deployment using Flask
           Here we deployed the model using Flask.

## Project Structure

```
├── dataFiles 
│   └── train
│   └── best_cnn_model.h5
│   └── best_crnn_model.h5
├── jupyterNotebook
│   └── constants.py
│   └── CNN_model_training.ipynb
│   └── CRNN_model_training.ipynb
│   └── image_processing.ipynb
├── flaskSrc
│   └── input_images
│   └── app.py
│   └── face_detection.py
│   └── music_recommend.py
│   └── recognize_emotions.py
│   └── logging_utils.py
```
## Technologies Used
1. Pandas
2. Matplotlib
3. Seaborn
4. Tensforflow
5. CNN, CRNN
6. Flask

## Istallation
The Code is written in Python 3.10.1. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:

```bash
pip install -r requirements.txt
cd flaskSrc
python app.py
```
