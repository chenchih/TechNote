'''
Split video into specfic start and end 
'''
import subprocess

# Command to cut a segment of a video using FFmpeg
#input_file = 'input_video.mp4'
input_file=input('enter input video name: ')
output_file=input('enter save output video name: ')
start_time = '00:00:00'
end_time = '00:01:20'
#output_file = 'part_1.mp4'
output_file=output_file+'.mp4'
# Run the FFmpeg command
cmd = [
    'ffmpeg',
    '-ss', start_time,
    '-to', end_time,
    '-i', input_file,
    '-c', 'copy',
    '-avoid_negative_ts', 'make_zero',
    output_file,
    '-y'
]

# Execute the command
subprocess.run(cmd, check=True, capture_output=True)
print(f"Segment saved as {output_file}")
