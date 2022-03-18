# CircuitPatchConverter
Circuit Patch converter takes in a .circuittrackspack (or other .zip file), 
extracts the patches and converts these to the OG circuit format.
It does this by altering the 5th hexadecimal value from `64` to `60`.
By Kamiel de Visser.

Requirements: 
1. Python 3.6+

Step by step example:
1. Clone this repository or download it as a .zip
2. (Extract zip to a directory)
3. Put your .circuittrackspack files in a folder called 'Packs' (like `someDir\CircuitPatchConverter\Packs`)
4. Open your favourite console that supports python and navigate (using `cd`) to `someDir\CircuitPatchConverter\` 
4. Launch the script using `python circuit-convert.py -i ./Packs/example.circuittrackspack` 
5. Find your newly converted patches in `someDir\CircuitPatchConverter\Patches`

**Please note:** this program will overwrite existing `.syx` files in the output folder. If you are converting multiple packs one by one, be sure to alter the output directory using the `-o` option.

Usage:

`python circuit-convert.py -i <inputfile> \[-o <outputfile> -p <pathinzip> -h <help>\]`

| short | long        | name               | description                                                 | default    |
|-------|-------------|--------------------|-------------------------------------------------------------|------------|
| -i    | --input     | <input file>       | The file path of the .circuittrackspack or .zip to extract. | N/A        |
| -o    | --output    | <output file>      | The path of the folder to extract the converted patches to. | ./Patches/ |
| -p    | --pathinzip | <path in zip file> | Path to folder in the zip file that contains the patches.   | patches/   |
| -h    | --help      | <help>             | Shows the help message.                                     | N/A        |