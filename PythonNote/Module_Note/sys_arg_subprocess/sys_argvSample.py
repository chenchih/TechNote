import subprocess
import sys
if __name__ == '__main__':
    #video_file = sys.argv[1] #input_video.mp4 
    #time_ranges = sys.argv[2:] #'02:50-03:20', '05:04-09:20'
  
    print("All arguments:", sys.argv) #All arguments: ['sys_argvSample.py', 'hello']
    #print(len(sys.argv))
    if len(sys.argv) < 2:
        print('no argument')
        sys.exit()
    print(f"sys.argv[0]: {sys.argv[0]}")#sys.argv[0]: sys_argvSample.py
    print(f"sys.argv[1]: {sys.argv[1]}")#sys.argv[1]: hello
