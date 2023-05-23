# WebToApp

## Requirements

- Linux operating system
- Python 3
- `nativefier` command-line tool
- `appimagetool` and `appimagelint` binaries (downloaded automatically by script)

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/Johoski/WebToApp.git
cd WebToApp
```

2. Install the required dependencies:

- Python packages:

  ```
  pip install -r requirements.txt
  ```

- `nativefier`:

  ```
  npm install nativefier -g
  ```

- `appimagetool` and `appimagelint` binaries:

  The script expects the following files to be present in the `dependencies` directory if not they are gonna be downloaded automatically:
  - `appimagetool-x86_64.AppImage` [Download from: AppImageKit Releases](https://github.com/AppImage/AppImageKit/releases)

  - `appimagelint-x86_64.AppImage` [Download from: AppImageLint Releases](https://github.com/TheAssassin/appimagelint/releases)


3. Customize the configuration file:

Edit the `conf.json` file and provide the necessary details for your application. Refer to the existing structure for guidance.

## Usage

1. Open a terminal and navigate to the cloned repository:

```
cd WebToApp
```

2. Run the script with the desired options:

```
python main.py -a app_name --noclean --lint
```

Available options:
- `-a, --app`: Specify the name of the app in the configuration file.
- `--noclean`: Skip cleaning the source and temporary folders after building the AppImage.
- `--lint`: Perform linting on the created AppImage.

3. Follow the script's output and prompts for any additional actions or inputs required.

4. Once the script finishes, the generated AppImage file will be available in the output directory.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

