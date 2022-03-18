### Circuit Patch converter takes in a .circuittrackspack (or other .zip file), 
### extracts the patches and converts these to the OG circuit format.
### It does this by altering the 5th hexadecimal value from 64 to 60.
### By Kamiel de Visser.

import zipfile      # for handling zips
import shutil       # for copying to other directories
import sys, getopt  # for handling args
import os           # for consistent directory pathing

def main(argv):
    # default paths
    input_path = r"./Packs/example.circuittrackspack"
    path_in_zip = r"patches/"
    output_path = r"./Patches/"

    # Keeps track of number of patches converted
    files_handled = 0

    # set options
    options = "hi:o:p:"
    long_options = ["help","input=", "output=", "zip_path="]
    try:
        opts = getopt.getopt(argv, options, long_options)[0]
    # Handle unknown options
    except getopt.GetoptError as error:
        print(error)
        sys.exit()

    # handle options
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-i", "--input"):
            input_path = arg
        elif opt in ("-o", "--output"):
            output_path = arg
        elif opt in ("-p", "--pathinzip"):
            path_in_zip = arg

    # 
    with zipfile.ZipFile(input_path) as zip:
        if (not os.path.exists(output_path)):
            os.makedirs(output_path)
        for file_name in zip.namelist():
            # skip directory listing
            if (file_name == path_in_zip) or not (file_name.endswith('.syx')):
                continue
            if (file_name.startswith(path_in_zip)):
                new_file_name = os.path.join(output_path, file_name[len(path_in_zip):])
                # Extract from zip to output path
                with zip.open(file_name) as zipped_file, open(new_file_name, 'wb') as new_file:
                    shutil.copyfileobj(zipped_file, new_file)
                # Replace circuit version hex value
                with open(new_file_name, 'r+b') as patch_file: 
                    patch_file.seek(5)
                    patch_file.write(b'\x60')
            files_handled += 1
    
    # Print end message
    print("Finished! Converted " + str(files_handled) + " patches.")
    if (output_path.startswith('.')):
        output_path = output_path[1:]
        print("You can find them in " + (os.getcwd() + output_path).replace('/', '\\'))
    else:
        print("You can find them in " + output_path.replace('/', '\\'))
    print("Enjoy your day and good luck! :)")


# print usage
def print_usage():
    print('Example usage:\tcircuit-convert.py -i <inputfile> \t[-o <outputfile> -p <pathinzip> -h <help>]')

# print help message
def print_help():
    print("Circuit Patch converter takes in a .circuittrackspack or other .zip file and converts it to the OG circuit format.")
    print("By Kamiel de Visser.\n")
    print_usage()
    print('\nshort\tlong\t\tname\t\tdescription\n')
    print('-i\t--input\t\t<inputfile>\tThe file path of the .circuittrackspack or .zip to extract.')
    print('-o\t--output\t<outputfile>\tThe path of the directory to save the resulting patches in.')
    print('-p\t--pathinzip\t<pathinzip>\tThe directory within the .circuittrackspack to extract. (default: \'patches/\')')
    print('-h\t--help\t\t<help>\t\tShows this help message.')

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        # Check whether any option argument has incorrect syntax
        for i in range(len(sys.argv)):
            if i % 2 != 0:
                if not sys.argv[i].startswith("-"):
                    print("Incorrect usage!")
                    print_usage()
                    sys.exit()
        # run main code
        main(sys.argv[1:])
    else:
        # Handle missing arguments
        print("No arguments given!")
        print_usage()