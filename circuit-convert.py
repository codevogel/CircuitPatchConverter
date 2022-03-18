
import zipfile
import shutil
import sys, getopt
import os



def main(argv):

    input_path = r"./Packs/Factory Pack.circuittrackspack"
    path_in_zip = r"patches/"
    output_path = r"./Patches/"

    options = "hi:o:p:"
    long_options = ["help","input=", "output=", "zip_path="]

    try:
        opts = getopt.getopt(argv, options, long_options)[0]
    except getopt.GetoptError as error:
        print(error)
        sys.exit()


    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-i", "--input"):
            input_path = arg
        elif opt in ("-o", "--output"):
            output_path = arg
        elif opt in ("-p", "--output"):
            path_in_zip = arg

    with zipfile.ZipFile(input_path) as zip:
        for file_name in zip.namelist():
            ##TODO: -p afhandelen
            # skip directory listing
            if (file_name == path_in_zip):
                continue
            if (file_name.startswith(path_in_zip)):
                with zip.open(file_name) as zipped_file, open(os.path.join(output_path, file_name[len(path_in_zip):]),  'wb') as new_file:
                    shutil.copyfileobj(zipped_file, new_file)

def print_usage():
    print('Example usage:\tcircuit-convert.py -i <inputfile> \t[-o <outputfile> -p <pathinzip> -h <help>]')

def print_help():
    print("Circuit Patch converter takes in a .circuittrackspack and converts it to the OG circuit format.\n")
    print_usage()
    print('\nshort\tlong\t\tname\t\tdescription\n')
    print('-i\t--input\t\t<inputfile>\tThe file path of the .circuittrackspack to extract.')
    print('-o\t--output\t<outputfile>\tThe path of the directory to save the resulting patches in.')
    print('-p\t--pathinzip\t<pathinzip>\tThe directory within the .circuittrackspack to extract. (default: \'patches/\')')
    print('-h\t--help\t\t<help>\t\tShows this help message.')

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        for i in range(len(sys.argv)):
            if i % 2 != 0:
                if not sys.argv[i].startswith("-"):
                    print("Incorrect usage!")
                    print_usage()
                    sys.exit()
        main(sys.argv[1:])
    else:
        print("No arguments given!")
        print_usage()