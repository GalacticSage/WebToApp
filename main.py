import json
import os
import platform
import shutil
import subprocess
import requests
from PIL import Image
import argparse

parser = argparse.ArgumentParser()

# import options

parser.add_argument('-a', '--app', help='Pass the app name')
parser.add_argument('--noclean', help='Dosnt clean the source and temp folder after building', action='store_true')
parser.add_argument('--lint', help='Lint the AppImage', action='store_true')

args = parser.parse_args()  # instantiate parser

# Common variables
dependencies = 'dependencies'
dep_config = 'dependencies/conf.json'
url_config = "https://raw.githubusercontent.com/Johoski/WebToApp/main/dependencies/conf.json"
temp = 'temp'
icon_size = 256
arch = 'ARCH=x86_64'
appimagetool = './dependencies/appimagetool-x86_64.AppImage'
url_appimagetool = "https://github.com/AppImage/AppImageKit/releases/download/13/appimagetool-x86_64.AppImage"
appimagelint = './dependencies/appimagelint-x86_64.AppImage'
url_appimagelint = "https://github.com/TheAssassin/appimagelint/releases/download/continuous/appimagelint-x86_64.AppImage"


def run_command_with_sudo(command):
    subprocess.run(['sudo', 'sh', '-c', command])


def read_json(file):
    with open(file) as f:
        conf = json.load(f)
        app = conf[args.app]

        name = app['name']
        AppImage = app['AppImage']
        url = app['url']
        source = app['source']
        dep = app['dep']
        AppDir = app['AppDir']
        usr = app['usr']
        var_bin = app['bin']
        url_AppRun = app['url_AppRun']
        url_desktop = app['url_desktop']
        dep_AppRun = app['dep_AppRun']
        dep_desktop = app['dep_desktop']
        AppRun = app['AppRun']
        desktop = app['desktop']
        url_icon = app['url_icon']
        icon1 = app['icon1']
        icon2 = app['icon2']

        return name, AppImage, url, source, dep, AppDir, usr, var_bin, url_AppRun, url_desktop, dep_AppRun, dep_desktop, AppRun , desktop, url_icon, icon1, icon2


# checks if needed stuff is there
def check():
    if platform.system() == "Windows":
        print("OS:                  FAILED (This script is made for Linux only)")
        exit()
    elif platform.system() == "Darwin":
        print("OS:                  FAILED (This script is made for Linux only)")
        exit()
    elif platform.system() == "Linux":
        print("OS:                  OK")
    else:
        print("OS:                  FAILED (This script is made for Linux only)")
        exit()

    is_dependencies = os.path.isdir(dependencies)
    if is_dependencies:
        print("Dependencies:        OK")
    else:
        print("Dependencies:        FAILED (Creating folder)")
        os.mkdir(dependencies)
        print("Dependencies:        FAILED (Downloading config)")
        response = requests.get(url_config)
        open(dep_config, "wb").write(response.content)
        is_dependencies = os.path.isdir(dependencies)
        is_appimagetool = os.path.isdir(appimagetool)
        if is_appimagetool:
            print("AppImage Tool:       OK (Download successful)")
        else:
            print("Dependencies:        FAILED (Please re-download the dependencies folder)")
            exit()

    is_appimagetool = os.path.isfile(appimagetool)
    if is_appimagetool:
        print("AppImage Tool:       OK")
    else:
        print("AppImage Tool:       FAILED (Starting download)")
        response = requests.get(url_appimagetool)
        open(appimagetool, "wb").write(response.content)
        print("AppImage Tool:       FAILED (Download finished)")
        is_appimagetool = os.path.isfile(appimagetool)
        if is_appimagetool:
            print("AppImage Tool:       OK (Download successful)")
        else:
            print("AppImage Tool:       FAILED (Download failed, please download the file manually)")
            exit()
    is_appimagelint = os.path.isfile(appimagelint)
    if is_appimagelint:
        print("AppImage Lint:       OK")
    else:
        print("AppImage Lint:       FAILED (Starting download)")
        response = requests.get(url_appimagelint)
        open(appimagelint, "wb").write(response.content)
        print("AppImage Lint:       FAILED (Download finished)")
        is_appimagelint = os.path.isfile(appimagelint)
        if is_appimagelint:
            print("AppImage Lint:       OK (Download successful)")
        else:
            print("AppImage Lint:       FAILED (Download failed, please download the file manually)")
            exit()

# creates source folder
def createSource():
    issource = os.path.isdir(source)
    if issource:
        print("Source:              OK")
    else:
        print("Source:              FAILED (Creating source folder)")
        os.system("nativefier " + url + " --name " + name)
        issource = os.path.isdir(source)
        if issource:
            print("\nSource:              OK (Source folder created)")
        else:
            print("\nSource:              FAILED (Source folder could not be created, please create it manually)")
            exit()


# creates AppDir
def createAppDir():
    istemp = os.path.isdir(temp)
    if istemp:
        shutil.rmtree(temp)
        os.mkdir(temp)
    else:
        os.mkdir(temp)
    os.mkdir(AppDir)
    os.mkdir(usr)


# copies files to AppDir
def copy_to_AppDir():
    shutil.copytree(source, var_bin)


def set_icon():
    response = requests.get(url_icon)
    open(icon1, "wb").write(response.content)
    with open(icon1, 'r+b') as f:
        with Image.open(f) as image:
            new_image = image.resize((icon_size, icon_size))
            new_image.save(icon1)
            os.remove(icon2)
            new_image.save(icon2)


def copy_dependencies():
    isdep_app = os.path.isfile(dep)
    if isdep_app:
        os.system("cp " + dep_AppRun + " " + AppRun)
        os.system("cp " + dep_desktop + " " + desktop)
    else:
        os.mkdir(dep)
        response = requests.get(url_AppRun)
        open(dep_AppRun, "wb").write(response.content)
        response = requests.get(url_desktop)
        open(dep_desktop, "wb").write(response.content)
        os.system("cp " + dep_AppRun + " " + AppRun)
        os.system("cp " + dep_desktop + " " + desktop)

def createAppImage():
    permissions = f'chmod +x {appimagetool}'
    run_command_with_sudo(permissions)
    command = f'ARCH=x86_64 {appimagetool} {AppDir}'
    run_command_with_sudo(command)
    permissions2 = f'chmod +x {AppImage}'
    run_command_with_sudo(permissions2)

def clean():
    if args.noclean:
        print("\nCleaning:            SKIPPED")
    else:
        print("\nCleaning:            OK")
        shutil.rmtree(temp)
        shutil.rmtree(source)

def lint():
    if args.lint:
        print("\nLinting:             OK")
        permissions = f'chmod +x {appimagelint}'
        run_command_with_sudo(permissions)
        lint_command = f'{appimagelint} {AppImage}'
        os.system(lint_command)
    else:
        print("\nLinting:             SKIPPED")

def finish():
    print("\nAppImage:            OK (AppImage created)")
    print("\nFinished:            OK (AppImage created successfully)")
    exit()


# run functions
check()
# read json
name, AppImage, url, source, dep, AppDir, usr, var_bin, url_AppRun, url_desktop, dep_AppRun, dep_desktop, AppRun , desktop, url_icon, icon1, icon2 = read_json(dep_config)
createSource()
createAppDir()
copy_to_AppDir()
set_icon()
copy_dependencies()
createAppImage()
clean()
lint()
finish()
