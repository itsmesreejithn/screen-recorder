import pyautogui
import cv2
import numpy as np

# specifying resolutin
resolutin = (1920, 1080)

# specifying video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# specifying name of output file
filename = "Recording.avi"

# specifying frames rate
fps = 60.0

# creating videowriter object
out = cv2.VideoWriter(filename, codec, fps, resolutin)

# To displaying the recording in real-time
# creating an empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# resize this window
cv2.resizeWindow("Live", 480, 270)

# recording the screen
while True:
    # taking screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # convert the screenshot to numpy array
    frame = np.array(img)

    # convert it from BRG to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # write it to the output file
    out.write(frame)

    # displaying recording screen
    cv2.imshow("Live", frame)

    # stoping the recording on pressing q
    if cv2.waitKey(1) == ord('q'):
        break

# every thing is done
# release the video writer
out.release()

# distroy all windows
cv2.destroyAllWindows()
