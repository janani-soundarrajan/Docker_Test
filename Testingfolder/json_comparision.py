import os
import json
import shutil

# # Source file path where jsons files available.
Atual_path ="/home/janani/Desktop/pythonfolder/Actual/"
Expected_path = "/home/janani/Desktop/pythonfolder/Expected/"


# #List the files which are available in the source path and store in the variable.
Actual_files = os.listdir (Atual_path)
Expected_files = os.listdir (Expected_path)

str_actual="/home/janani/Desktop/pythonfolder/str_actual/"
str_expected="/home/janani/Desktop/pythonfolder/str_expected/"

for x in Actual_files:
    Actual_json_to_string   = json.dumps(x)
    print(type(Actual_json_to_string))
    jts = Actual_json_to_string.replace(".json",".txt")
    print(jts)
    destination_file_paths = os.path.join(str_actual,jts)
	# print(destination_file_path)
    source_file_paths = os.path.join(Atual_path,x)
	# print(source_file_path)
    shutil.copy(source_file_paths,destination_file_paths)
    print(source_file_paths)
    #print(f"The filename {x} is copied to the {final_renamedfile}")

