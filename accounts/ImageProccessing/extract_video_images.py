import cv2
import os

if __name__ == "__main__":
    video_path = "video.mp4"  # Update the path to your video file
    output_folder = "images"

    if os.path.isfile(video_path):
        cam = cv2.VideoCapture(video_path)
        fps = cam.get(cv2.CAP_PROP_FPS)
        print(fps)
        
        total_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
        target_frames = 10
        step = total_frames // target_frames

        for i in range(target_frames):
            frame_number = i * step
            cam.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            ret, frame = cam.read()

            if ret:
                cv2.imwrite(os.path.join(output_folder, "{}.jpg".format(i)), frame)

        cam.release()
        cv2.destroyAllWindows()
    else:
        print("Error: Video file not found.")
