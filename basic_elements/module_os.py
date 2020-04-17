"""
The os Python module provides a big range of useful methods to manipulate files and directories.

Script presenting basic operations using module os
"""
import os

pwd = os.getcwd() # print current working directory
print("Current working directory: {0}\n".format(pwd))

path_dir = "main_dir/sub_dir"
os.makedirs(path_dir) # create a new directory recursively with subdirectories

abs_path_dir = os.path.join(pwd, path_dir) # join path with dir/file name
print("Absolut path to a sub_dir is: {0}\n".format(abs_path_dir))

os.chdir(abs_path_dir) # change working directory to sub_dir
print("Current working directory after change: {0}\n".format(os.getcwd()))

os.chdir(pwd)
print("Return to start directory: {0}\n".format(pwd))

dir_content = os.listdir(pwd) # return a list of directories and files in the path
print("Content of the directory: {0}\n".format(dir_content))

new_file = 'os_test.txt'
new_file_command = 'touch {0}'.format(new_file)
os.system(new_file_command) # creating a file using bash command with the use of os.system
print("Content of the directory after creation additional file: {0}\n".format(os.listdir(pwd)))

abs_path_new_file = os.path.join(pwd, new_file)
# basename of the file using os.path.basename
print("Basename of the new file: {0}\n".format(os.path.basename(abs_path_new_file)))

# dirname of the file using os.path.dirname
print("Dirname of the new file: {0}\n".format(os.path.dirname(abs_path_new_file)))

# split name of the file for basename and dirname using os.path.split
print("Split name of the new file: {0}\n".format(os.path.split(abs_path_new_file)))

# split name of the file for main name and extension using os.path.splitext
print("Split name of the new file with extension: {0}\n".format(os.path.splitext(abs_path_new_file)))

# checking existence of a path
check_exis = os.path.exists(abs_path_new_file)
print("Checking if path {0} really exists: {1}\n".format(abs_path_new_file, check_exis))

# checking if a path is a directory
check_dir = os.path.isdir(abs_path_new_file)
print("Checking if path {0} is a directory: {1}\n".format(abs_path_new_file, check_dir))

# checking if a path is a file
check_file = os.path.isfile(abs_path_new_file)
print("Checking if path {0} is a directory: {1}\n".format(abs_path_new_file, check_file))

# print home directory using environmental variable - os.environ.get
home = os.environ.get('HOME')
print("Home directory: {0}\n".format(home))

# rename an existing file with os.rename
renamed_file = "renamed_filed.txt"
os.rename(new_file, renamed_file)
print("Renamed file: {0}\n".format(renamed_file))

# checking size of the current directory using os.stat().st_size
size = os.stat(pwd).st_size
print("Size of the current working directory: {0}\n".format(size))

# show content of this directory and all subdirectories with os.walk
tree = os.walk(pwd)
print("Tree of file and directories:")
print("root dirs files")
for root, dirs, files in tree:
    print(root, dirs, files)
print("")

# remove a created file with os.remove
os.remove(renamed_file)

# remove created directories
os.removedirs(abs_path_dir)
print("Content of the directory after removal all newly created files and direcotues: \n{0}\n".format(os.listdir()))