import cv2
import os
from collections import deque
from datetime import datetime

def file_streaming(video_path, frame_interval):
    try:
        capture = cv2.VideoCapture(video_path)
        if not capture.isOpened():
            print("Error: Could not open video.")
            return None
    except:
        print('file_streaming error')
        return None

    frame_counter = 0
    recording = False
    out = None

    output_fps = 64.0

    # Folder to save recorded videos
    current_date = datetime.now().strftime('%Y-%m-%d')
    output_folder = os.path.join('[directory path]', current_date)
    # output_folder = os.path.join('/home/user/recording_stream', current_date)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output directory: {output_folder}")
    
    frame_buffer = deque(maxlen=10)

    while True:
        ret, frame = capture.read()  # Read the frame
        timestamp = datetime.now().strftime('%H-%M-%S')
        if not ret:
            print("Reached the end of the video or failed to read the video stream.")
            break  # Exit the loop if no more frames or error

        # Process every frame based on the interval
        if frame_counter % frame_interval == 0:
            # Display the frame
            # Display the frame
            frame_height, frame_width = frame.shape[:2]
            display_width = frame_width // 2
            display_height = frame_height // 2
            resized_frame = cv2.resize(frame, (display_width, display_height))
            cv2.imshow('Frame', resized_frame)
            # frame_buffer.append(frame)

            key = cv2.waitKey(1) & 0xFF

            # Press 'r' to start recording
            if key == ord('r'):
                if not recording:
                    recording = True
                    print("Recording started...")
                    # Get the codec information and create a VideoWriter object to save the video
                    fourcc = cv2.VideoWriter_fourcc(*'XVID')
                    filename = os.path.join(output_folder, f'recorded_video_{timestamp}.avi')
                    out = cv2.VideoWriter(filename, fourcc, 30.0, (frame_width, frame_height))
                    print(f"Saving video to: {filename}")

                    # while frame_buffer:
                    #     out.write(frame_buffer.popleft())
            
            # Press 's' to stop recording
            elif key == ord('s'):
                if recording:
                    print("Recording stopped.")
                    recording = False
                    out.release()
                    out = None

            # If recording is active, write the frame to the file
            if recording and out is not None:
                out.write(frame)

            # Press 'q' to quit the video stream
            if key == ord('q'):
                break
        else:
            print(f"Skipping frame {frame_counter}")

        frame_counter += 1

    # Release the video capture object and close all windows
    capture.release()
    if out:
        out.release()
    cv2.destroyAllWindows()

    return capture
