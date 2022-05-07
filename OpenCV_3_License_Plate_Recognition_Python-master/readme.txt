The video pretty much explains it all:
https://www.youtube.com/watch?v=fJcl6Gw1D8k


For Video

You can use the following function:

cap = cv2.VideoCapture(path_to_folder + 'nameofvideo.avi')

Then to capture the frames (use it in a loop):

ret, frame = cap.read()

frame variable holds each frame of the video.

For more information, search for this function and youll get more examples?