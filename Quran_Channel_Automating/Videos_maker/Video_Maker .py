import os
from moviepy.editor import ImageClip, AudioFileClip

def create_videos_from_folders(image_folder, audio_folder, output_dir, fps=24):
    # Get sorted lists of image and audio files by name
    image_files = sorted(
        [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))],
        key=lambda x: x)
    audio_files = sorted(
        [f for f in os.listdir(audio_folder) if f.endswith(('.mp3', '.wav'))],
        key=lambda x: x)
    
    # Full paths for images and audio
    image_paths = [os.path.join(image_folder, f) for f in image_files]
    audio_paths = [os.path.join(audio_folder, f) for f in audio_files]

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Ensure the lengths of image_paths and audio_paths are the same
    if len(image_paths) != len(audio_paths):
        raise ValueError("The number of images and audio files must be the same.")

    # Loop through each image and audio file
    for i, (image_path, audio_path) in enumerate(zip(image_paths, audio_paths)):
        # Print the names of the image and audio files being processed
        print(f'Creating video for: Image = {os.path.basename(image_path)}, Audio = {os.path.basename(audio_path)}')

        # Create the video for each image-audio pair
        image_clip = ImageClip(image_path)
        audio_clip = AudioFileClip(audio_path)

        # Set duration of the image clip to match the audio duration
        video_clip = image_clip.set_duration(audio_clip.duration)
        video_clip = video_clip.set_audio(audio_clip)

        output_path = os.path.join(output_dir, f'output_video_{i + 1}.mp4')
        video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

# Example usage
image_folder = 'B:/personal folders/automatic_quran_vids/output_img'
audio_folder = 'B:/personal folders/automatic_quran_vids/audios'
output_dir = 'B:/personal folders/automatic_quran_vids/output_vids'

create_videos_from_folders(image_folder, audio_folder, output_dir, fps=1)
