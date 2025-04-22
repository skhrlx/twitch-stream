import subprocess
import time

def stream_video(video_path, stream_key, twitch_url="rtmp://live.twitch.tv/app"):
    ffmpeg_command = [
        "ffmpeg",
        "-re",
        "-stream_loop", "-1",
        "-i", video_path,
        "-vf", "scale=256:144",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-b:v", "300k",
        "-g", "30",
        "-c:a", "libmp3lame",
        "-b:a", "128k",
        "-f", "flv",
        f"{twitch_url}/{stream_key}"
    ]

    while True:
        try:
            print("Starting stream to Twitch...")
            process = subprocess.run(ffmpeg_command)
            
            if process.returncode != 0:
                print("FFmpeg exited with an error. Restarting stream...")
                time.sleep(5)
        except KeyboardInterrupt:
            print("Streaming interrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Restarting stream...")
            time.sleep(5)

if __name__ == "__main__":
    video_path = "infinite_silence.mp4"
    stream_key = "YOUR_KEY_GOES_HERE"

    stream_video(video_path, stream_key)
