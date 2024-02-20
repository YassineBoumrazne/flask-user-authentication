import os
import cv2
from pytube import YouTube

def download_youtube_video(url, filename):
    yt = YouTube(url)
    video_stream = yt.streams.filter(file_extension="mp4", res="360p").first()
    downloaded_path = video_stream.download(filename=filename)
    return downloaded_path

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=1eRrG3-rSlQ"  # Replace with the actual YouTube video URL
    custom_filename = "vid1.mp4"  # Replace with your desired filename

    # Download YouTube video and save it in the current working directory
    video_path = download_youtube_video(youtube_url, custom_filename)

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
                cv2.imwrite(os.path.join('images', "{}.jpg".format(i)), frame)

        cam.release()
        cv2.destroyAllWindows()
    else:
        print("Error: Video file not found.")
