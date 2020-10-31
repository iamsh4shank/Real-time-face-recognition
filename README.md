# Real-Time-Face-Recognition (OpenCV)

This is a full step Python program to create an efficient real-time face recognition app.

## Steps:

1) Run `Face_taker.py` script. The script will generate and save 50 images from the photo present in person's admit card and save it to the `images` folder. So for now there is the test2.png image for testing but we can use database to fetch the image of the person who is giving exam. 

2) The `Face_tain.py` script will train a model to recognize your face from the 50 images taken using `Face_taker.py` script, and save the training output in the `training.yml` file.

3) The `Face_Recognizer.py` is the main script. You need to change the name of each person who sees his/her picture taken in the `Face_taker.py` script. The program will recognize the face according to the id given in the same script. Note: If the recognizer could predict a face, we put a text over the image with the probable id and how much is the "probability" in % that the match is correct ("probability" = 100 - confidence index). If not, an "Who are you?" label is put on the face.

### Todo
- Add some data augmentation techniques to increase accuracy and prediction probabiltity
