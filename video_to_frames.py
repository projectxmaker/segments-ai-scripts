import ffmpeg
import os
import argparse

def split_video_to_frames(input_file, output_folder, fps=10):
    # 1. Create folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")

    print(f"Extracting frames from: {input_file}...")

    try:
        # 2. Execute ffmpeg-python
        (
            ffmpeg
            .input(input_file)
            .filter('fps', fps=fps) # get 10 frames per second
            .output(f"{output_folder}/frame_%05d.jpg", qscale=2) # qscale=2 is high quality
            .run(capture_stdout=True, capture_stderr=True)
        )
        print(f"--- FINISHED ---")
        print(f"Frames were saved in: {output_folder}")
    except ffmpeg.Error as e:
        print(f"FFmpeg Error: {e.stderr.decode('utf8')}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract video to frames.")
    parser.add_argument("--input", required=True, help="Input video name (exp: case2.mp4)")
    parser.add_argument("--output", required=True, help="Output folder name")
    parser.add_argument("--fps", type=int, default=10, help="Number of frames per second (10 as default)")

    args = parser.parse_args()
    split_video_to_frames(args.input, args.output, args.fps)
