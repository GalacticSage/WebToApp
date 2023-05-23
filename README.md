# WebToApp
WebToApp is a Python script that allows you to easily convert a web application into a standalone desktop application using the Nativefier tool and package it as an AppImage. It simplifies the process of creating a desktop application from a web app by automating the necessary steps and providing a streamlined workflow.
## Features
- Converts web applications into standalone desktop applications.
- Packages the application as an AppImage for easy distribution and execution on various Linux distributions.
- Automatically sets up the required directory structure and dependencies.
- Supports customization of the application name, icon, and other settings through a configuration file.
- Optional cleaning and linting steps to ensure a clean and optimized AppImage package.
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

## Disclaimer
WebToApp is provided as-is without any warranty. Use it at your own risk.

## Acknowledgements
WebToApp is built upon the [Nativefier](https://github.com/nativefier/nativefier) tool and utilizes the [AppImage](https://github.com/AppImage/AppImageKit) ecosystem for packaging and distribution.
