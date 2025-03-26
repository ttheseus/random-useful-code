import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def join_videos_from_directory(directory_path, output_file):
	video_files = [f for f in os.listdir(directory_path) if f.endswith('.avi')]
	clips = []
	
	for video_file in video_files:
		video_path = os.path.join(directory_path, video_file)
		try:
			clip = VideoFileClip(video_path)
			clips.append(clip)
		except Exception as e:
			print(f"Failed to load {video_file}: {e}")
	
	if clips:
		final_clip = concatenate_videoclips(clips, method="compose")
		final_clip.write_videofile(output_file, codec="libx264", audio=False)
		
		for clip in clips:
			clip.close()
		print(f"Videos have been successfully joined into {output_file}")
	else:
		print("No .avi files found in the specified directory.")
		
directory_path = "/home/user/Documents/SAFE_ai/testing/original"
output_file = "testing_file.mp4"

if os.path.isdir(directory_path):
	join_videos_from_directory(directory_path, output_file)

else:
	print("The specified directory does not exist.")
