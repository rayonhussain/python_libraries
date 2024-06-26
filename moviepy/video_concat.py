#pip install moviepy

from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def list_mp4_files(directory):
    mp4_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4'):
                mp4_files.append(os.path.join(root, file))
    for idx, file in enumerate(mp4_files):
        print(f"{idx}: {file}")
    return mp4_files

def get_file_details(mp4_files, file_index):
    if file_index < 0 or file_index >= len(mp4_files):
        print("Invalid file index.")
        return None, None
    selected_file = mp4_files[file_index]
    file_path = selected_file
    file_name = os.path.basename(selected_file)
    return file_path, file_name


def main():
    intro_path = "/Users/rayon/Desktop/YT/BIGRIP YT/DEV/INTRO 1.mp4"
    outro_path = "/Users/rayon/Desktop/YT/BIGRIP YT/DEV/MAIN OUTRO 1.mp4"
    input_directory = "/Users/rayon/Desktop/YT/BIGRIP YT/DEV/COD"
    output_directory = "/Users/rayon/Desktop/YT/BIGRIP YT/PROD/"

    mp4_files = list_mp4_files(input_directory)

    intro_clip = VideoFileClip(intro_path)
    outro_clip = VideoFileClip(outro_path)

    for file_path in mp4_files:
        main_clip = VideoFileClip(file_path)
        combined_clip = concatenate_videoclips([intro_clip, main_clip, outro_clip])

        output_filename = os.path.basename(file_path).replace(".mp4", "_COMBINED.mp4")
        output_path = os.path.join(output_directory, output_filename)

        combined_clip.write_videofile(
            output_path,
            codec='libx264',
            fps=60,
            preset='slow',
            ffmpeg_params=['-vf', 'scale=2560:1440']  # 2K resolution
        )


if __name__ == "__main__":
    main()
