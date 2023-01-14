import json
import os
import subprocess
import logger
import argparse

# setup argparse
parser = argparse.ArgumentParser()
parser.add_argument("--delete-original", help="delete original python files after compilation", action="store_true")
parser.add_argument("--input", help="input python file path")
parser.add_argument("--icon", help="icon file path")
parser.add_argument("--output-name", help="output file name")
parser.add_argument("--output-path", help="output file path")
args = parser.parse_args()

# check if input file is provided
if args.input:
    input_file = args.input
    files_list = [input_file]
else:
    print("input file not provided")
    exit()

# check if icon file is provided
if args.icon:
    icon_file = args.icon
    if not icon_file.endswith('.ico'):
        print("Invalid icon file. Please provide a valid ico file")
        exit()
else:
    #read from config.json
    with open('config.json', 'r') as f:
        data = json.load(f)
    icon_file = data.get('icon')
    if not icon_file:
        print("icon file not provided")
        exit()
    if not icon_file.endswith('.ico'):
        print("Invalid icon file. Please provide a valid ico file")
        exit()

# check if output file name is provided
if args.output_name:
    output_name = args.output_name
else:
    input_filename = os.path.splitext(input_file)[0]
    output_name = input_filename

# check if output path is provided
if args.output_path:
    output_path = args.output_path
    if not os.path.exists(output_path):
        os.makedirs(output_path)
else:
    output_path = './'

#run pyinstaller command to compile all the files
try:
    logger.info("Started Compilation")
    subprocess.call(["pyinstaller", "--onefile", "--clean", "-p", ".", "-n", output_name, "-d", output_path, "--noconsole", "--icon", icon_file] + files_list)
    logger.info("Compilation complete.")
except subprocess.CalledProcessError as e:
    logger.error(f'Error: {e}')
    exit()

#delete all the original python files that were compiled
if args.delete_original:
    for f in files_list:
        if os.path.exists(f):
            os.remove(f)
            logger.debug(f'{f} removed')
            logger.info("All original python files removed.")
else:
    logger.info("Original files not removed.")

