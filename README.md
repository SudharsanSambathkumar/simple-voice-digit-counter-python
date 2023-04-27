# voice-digit-counter-python
 mediapipe|OpenCV|pyttsx3
# Here is an overview of the main parts of the code:

- First, it imports the necessary libraries: cv2 (OpenCV), mediapipe, time, and pyttsx3.
- Then, it initializes the text-to-speech engine with pyttsx3.
- The code sets the voice to use for text-to-speech output.
- It initializes the camera using OpenCV's VideoCapture function.
- The code initializes a MediaPipe Hands object, which will be used to detect hands in the video stream.
- It also initializes a MediaPipe Drawing Utilities object, which will be used to draw landmarks on the detected hands in the video stream.
- The main loop of the program starts, where the code reads frames from the video stream and processes them with the Hands object.
- If hands are detected in the frame, the code extracts the landmarks of the hands and draws them on the frame.
- The code then counts the number of fingers that are extended based on the position of the hand landmarks and displays the count on the frame.
- Finally, the code uses text-to-speech output to say the finger count aloud.
- The loop continues until the user presses the "q" key to exit.
- The code releases the camera and destroys any remaining OpenCV windows.
