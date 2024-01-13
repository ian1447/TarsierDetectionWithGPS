from tkinter import *
import customtkinter as ctk
import cv2

#set themes
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Variables
camera_1_no_tarsier = 3
camera_1_location = "9.8500° N, 124.1435° E"
camera_2_no_tarsier = 2
camera_2_location = "9.8500° N, 124.1435° E"

#initialize
root = ctk.CTk()
root.title("Tarsier Detection")

#FIRST FRAME FOR CAMERA 1
frame = ctk.CTkFrame(master=root,
                     width=380,
                     height=150,
                     border_color="red")
frame.pack_propagate(False)
frame.grid(padx=10,
           pady=10)

camera_label = ctk.CTkLabel(frame, text = "Camera 1")
camera_label.pack()

camera1_description = ctk.CTkLabel(frame,
                                   text = f"No of Tarsiers last recorded: {camera_1_no_tarsier}",
                                   anchor="nw",
                                   width=380,
                                   font=("Arial",15))
camera1_description.pack(padx = 10)

camera1_location = ctk.CTkLabel(frame,
                                text = f"Location of Camera: {camera_1_location}",
                                anchor="nw",
                                width=380,
                                font=("Arial",15))
camera1_location.pack(padx = 10)

camera1_open_button = ctk.CTkButton(frame,
                                    text = "Open Camera 1",
                                    height=50,
                                    width=370,
                                    command = lambda:Open_Camera(0))
camera1_open_button.pack()


#SECOND FRAME FOR CAMERA 2
frame2 = ctk.CTkFrame(master=root,
                      width=380,
                      height=150,
                      border_color="red")
frame2.pack_propagate(False)
frame2.grid(padx=0,
            pady=10)

camera2_label = ctk.CTkLabel(frame2,
                             text = "Camera 2")
camera2_label.pack()

camera2_description = ctk.CTkLabel(frame2,
                                   text = f"No of Tarsiers last recorded: {camera_2_no_tarsier}",
                                   anchor="nw",
                                   width=380,
                                   font=("Arial",15))
camera2_description.pack(padx = 10)

camera2_location = ctk.CTkLabel(frame2,
                                text = f"Location of Camera: {camera_2_location}",
                                anchor="nw",
                                width=380,
                                font=("Arial",15))
camera2_location.pack(padx = 10)

camera2_open_button = ctk.CTkButton(frame2,
                                    text = "Open Camera 2",
                                    height=50,
                                    width=370,
                                    command=lambda: Open_Camera(0))
camera2_open_button.pack()

def Open_Camera(cam):
    vid = cv2.VideoCapture(cam)
    while (True):

        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        # Display the resulting frame
        cv2.imshow(f'Camera {cam + 1}', frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

root.mainloop()