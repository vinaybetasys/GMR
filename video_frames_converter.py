import cv2
import os
import argparse


def video_to_frames(video_path, output_folder=None, every=1, img_format="jpg"):
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    # Default output folder = video name + "_frames"
    if output_folder is None:
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        output_folder = f"{base_name}_frames"

    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Could not open video: {video_path}")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Video: {video_path}")
    print(f"Total frames: {total_frames}, FPS: {fps:.2f}")
    print(f"Saving every {every} frame(s) to: {output_folder}")

    frame_index = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_index % every == 0:
            filename = os.path.join(
                output_folder, f"frame_{saved_count:06d}.{img_format}"
            )
            cv2.imwrite(filename, frame)
            saved_count += 1

        frame_index += 1

    cap.release()
    print(f"Done. Saved {saved_count} frames to '{output_folder}'.")
    return output_folder, saved_count


def main():
    video_path = "input_video.mp4"  # Replace with your video file path
    output_folder = None  # Optional: specify output folder

    video_to_frames(video_path, output_folder)

if __name__ == "__main__":
    main()