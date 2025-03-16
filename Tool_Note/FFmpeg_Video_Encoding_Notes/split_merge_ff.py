import subprocess
import sys

# Function to cut the video
def cut_video(input_file, start_time, end_time, output_file):
    cmd = [
        'ffmpeg',
        '-ss', start_time,
        '-to', end_time,
        '-i', input_file,
        '-c', 'copy',
        '-avoid_negative_ts', 'make_zero',
        output_file,
        '-y'  # Overwrite output file if it exists
    ]
    
    #subprocess.run(cmd,capture_output=True)
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)  # Print the captured standard output
    print(result.stderr)  # Print the captured standard error (useful for debugging)


# Function to merge videos
def merge_videos(files, output_file):
    with open('inputs.txt', 'w') as f:
        for file in files:
            f.write(f"file '{file}'\n")

    cmd = [
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', 'inputs.txt',
        '-c', 'copy',
        output_file,
        '-y'  # Overwrite output file if it exists
    ]
    #subprocess.run(cmd)
    result = subprocess.run(cmd, capture_output=True, text=True)  # Add capture_output and text=True for readable output
    print(result.stdout)
    print(result.stderr)
    # Cleanup
    subprocess.run(['del', 'inputs.txt'],shell=True)
   

if __name__ == "__main__":
    video_file = sys.argv[1] #input_video.mp4 
    time_ranges = sys.argv[2:]#'02:50-03:20', '05:04-09:20'
    
    # Cut the parts from the video
    for i, time_range in enumerate(time_ranges):
        start, end = time_range.split('-')
        output_part = f'part_{i}.mp4'
        #print(f"start: {start}, end: {end}, output: {output_part}")
        cut_video(video_file, start, end, output_part)
        parts.append(output_part)
        print(parts)
    # Merge the parts
    merged_video = 'merged_output.mp4'
    merge_videos(parts, merged_video)

    # Cleanup
    for part in parts:
        subprocess.run(['del', part],shell=True)

#run: cut_and_merge.bat input_video.mp4 02:50-03:20 05:04-09:20 10:12-11:30