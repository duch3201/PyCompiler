# PyCompiler

PyCompiler is a simple wrapper around the [PyInstaller](https://www.pyinstaller.org/) library that makes it easy to compile Python scripts into standalone executables.

## Installation

Please use the [install.sh](install.sh) as it's the cleanest & fastest way to install and configure PyC

Feel free to also use the precompiled binary

## Features

- Compiles Python scripts into standalone executables for Linux, and macOS.
- Can be used via command-line arguments or a config file.
- Can remove original python files after compilation
- Can specify icon file to use for the executable
- Can specify output file name and path
- Can log the compilation process using logger module

## Usage

./PyC.py [-h] [--delete-original] [--input INPUT] [--icon ICON]
[--output-name OUTPUT_NAME] [--output-path OUTPUT_PATH]

### Command-line arguments

`--delete-original`: delete original python files after compilation.

`--input`: input python file path.

`--icon`: icon file path. (**Must be .ico**)

`--output-name`: output file name.

`--output-path`: output file path.


### Config file

The script also supports reading options from a config file named `config.json`.
It should contain a JSON object with the following fields:

{
"files": [],
"icon": "path/to/icon.ico",
"output_name": "output_file_name",
"output_path": "path/to/save"
}

## Requirements

- Python 3
- PyInstaller
- logger (should be included in this repository if not download from [here](https://github.com/duch3201/logger))

## Examples

`./PyC.py --input app_to_compile.py --icon path/to/icon.ico --output-name outfile --output-path /path/to/save --delete-original`

This command will take the `app_to_compile.py` file, and it will use the icon file at `path/to/icon.ico`, and it will save the output file as `outfile` in the `/path/to/save` directory and it will delete the original python file.

## Limitations

PyCompiler, as a wrapper around the PyInstaller library, inherits the limitations of PyInstaller. So please keep that in mind!

## Contribution

Your contributions and suggestions are heartily welcome. 
Please fork this repository and open a pull request to add features, fix bugs, improve documentation, etc.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
