import os, subprocess, time

overwrite_message = "Want to overwrite the already compressed files present with same name in destination directory? [Y/N]  "

try:
    os.remove('err.log')                                               # Removing previous error logs
except:
    pass                                                               # Error file already cleaned

overwrite = ''
while overwrite!='Y' and overwrite!='N':                               # Ask user whether he/she wants to overwrite the files or not
    overwrite = input(overwrite_message)

handbrake_path = "HandBrakeCLI.exe"                                    # Path where you have downloaded HandbrakeCLI

source_dir = r"C:\Users\ypank\Videos\test"                             # Source Directory Path
source_dir_files = os.listdir(source_dir)                              # Getting all files in source directory

destination_dir = r"E:\Videos"                                         # Destination Directory Path
if overwrite=='N':
    destination_dir_files = os.listdir(destination_dir)                # Getting all files in destination directory
    source_dir_files = set(source_dir_files) - set(destination_dir_files)

quality_value = "25"                                                   # Compression quality
count = 0                                                              # File count
for file in source_dir_files:
    count+=1                                                          
    
    source_filename =  os.path.join(source_dir, file)                  # Full path of source file
    destination_filename = os.path.join(destination_dir, file)         # Full path of destination file
    
    print("\n---------------------------------------------------------------------------")
    print("{}. Compressing {}\n".format(count, source_filename))
    
    # Command with all params to be executed, the stdout redirected to /dev/null (os.devnull) and stderr to err.log
    command = [handbrake_path, "-i", source_filename, "-o", destination_filename, "-e", "x264", "-q", quality_value, "-B", "160", "1>{}".format(os.devnull), "2>>err.log" ]
    
    try:
        start_time = time.time()                                        # Initializing Start time
        subprocess.run(command, shell=True, check=True)                 # Executing the command
        print("--- %s seconds ---" % (time.time() - start_time))        # Time taken for execution
    except:
        print(">>>>>>> Compression failed, check err.log for more info.\n")


print("\n------------------------------| Process finished |-----------------------------")
