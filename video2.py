#! /usr/bin/python3
# Building an Android APK:)
# http://inclem.net/2014/01/12/kivy-crash-course/2_building_an_android_apk/
# pip install buildozer
# cd ~/PycharmProjects/kivy_crash_course
# buildozer init
# vi buildozer.spec
# I made log_level = 2; the highest, most detailed. Where is the log? Where is the log file?
#   It appears the console is the log output.
# buildozer android debug
# ... errors ... They appear in red. (Green if not an error.) My problem was that in my buildozer.spec I'd commented a
# line though they are command line options and the comment became garbage.
# got bin/?.apk, emailed and tried to install on my Android and got "package appears to be corrupt" which MIGHT BE
# that the package is not compatible or does not include everything that's necessary. There is a requirements, somewhere,
# that will include required packages.


def main():
    print("main() function.")

if __name__ == "main":
    print("main.")
    main()
else:
    print("Not main.")

# - - -
lastRun = """
dalem@Mercury2:~/PycharmProjects/kivy_crash_course⟫ buildozer android debug
# Check configuration tokens
# Ensure build layout
# Check configuration tokens
# Preparing build
# Check requirements for android
# Run 'dpkg --version'
# Cwd None
Debian 'dpkg' package management program version 1.18.4 (amd64).
This is free software; see the GNU General Public License version 2 or
later for copying conditions. There is NO warranty.
# Search for Git (git)
#  -> found at /usr/bin/git
# Search for Cython (cython)
#  -> found at /usr/local/bin/cython
# Search for Java compiler (javac)
#  -> found at /usr/lib/jvm/java-8-oracle/bin/javac
# Search for Java keytool (keytool)
#  -> found at /usr/lib/jvm/java-8-oracle/jre/bin/keytool
# Install platform
# Apache ANT found at /home/dalem/.buildozer/android/platform/apache-ant-1.9.4
# Android SDK found at /home/dalem/.buildozer/android/platform/android-sdk-20
# Android NDK found at /home/dalem/.buildozer/android/platform/android-ndk-r9c
# Check application requirements
# Run './distribute.sh -l'
# Cwd /home/dalem/PycharmProjects/kivy_crash_course/.buildozer/android/platform/python-for-android
Available modules: android apsw audiostream bidi boost cherrypy c_igraph click cprotobuf cymunk django docutils ecdsa enum34 evdev ffmpeg ffmpeg2 ffpyplayer ffpyplayer_tito flask freetype gevent greenlet harfbuzz hostpython igraph itsdangerous jinja2 jpeg kivent_core kivent_cymunk kivy leveldb libevent libpq libsodium libswift libtorrent libxml2 libxslt libyaml lxml m2crypto markupsafe midistream msgpack mysql_connector netifaces numpy opencv openssl paramiko pil plyer plyvel png polygon protobuf psutil psycopg2 pyasn1 pycrypto pygame pyjnius pylibpd pyopenssl pyparsing pyqrcode python pyyaml sdl setuptools six sqlalchemy sqlite3 storm swift thrift twisted txws werkzeug wokkel zeroconf zope
# Application requirements already installed, pass
# Check garden requirements
# Compile platform
# Run './distribute.sh -l'
# Cwd /home/dalem/PycharmProjects/kivy_crash_course/.buildozer/android/platform/python-for-android
Available modules: android apsw audiostream bidi boost cherrypy c_igraph click cprotobuf cymunk django docutils ecdsa enum34 evdev ffmpeg ffmpeg2 ffpyplayer ffpyplayer_tito flask freetype gevent greenlet harfbuzz hostpython igraph itsdangerous jinja2 jpeg kivent_core kivent_cymunk kivy leveldb libevent libpq libsodium libswift libtorrent libxml2 libxslt libyaml lxml m2crypto markupsafe midistream msgpack mysql_connector netifaces numpy opencv openssl paramiko pil plyer plyvel png polygon protobuf psutil psycopg2 pyasn1 pycrypto pygame pyjnius pylibpd pyopenssl pyparsing pyqrcode python pyyaml sdl setuptools six sqlalchemy sqlite3 storm swift thrift twisted txws werkzeug wokkel zeroconf zope
# Distribution already compiled, pass.
# Build the application #2
# Copy application source from /home/dalem/PycharmProjects/kivy_crash_course
# Create directory /home/dalem/PycharmProjects/kivy_crash_course/.buildozer/android/app
# Copy /home/dalem/PycharmProjects/kivy_crash_course/video1.py
# Copy /home/dalem/PycharmProjects/kivy_crash_course/video2.py
# Copy /home/dalem/PycharmProjects/kivy_crash_course/main.py
# Package the application
# project.properties updated
# Run "python build.py --name 'Kivy Crash Course 2' --version 0.1 --package org.test # might be net.mooreworks.kivycrash2 --sdk 19 --minsdk 9 --private /home/dalem/PycharmProjects/kivy_crash_course/.buildozer/android/app --orientation sensor debug"
# Cwd /home/dalem/PycharmProjects/kivy_crash_course/.buildozer/android/platform/python-for-android/dist/kivycrash2
usage: build.py [-h] --package PACKAGE --name NAME --version VERSION
                [--numeric-version NUMERIC_VERSION] [--dir DIR]
                [--private PRIVATE] [--launcher] [--icon-name ICON_NAME]
                [--orientation ORIENTATION] [--permission PERMISSIONS]
                [--ignore-path IGNORE_PATH] [--icon ICON]
                [--presplash PRESPLASH] [--ouya-category OUYA_CATEGORY]
                [--ouya-icon OUYA_ICON] [--install-location INSTALL_LOCATION]
                [--compile-pyo] [--intent-filters INTENT_FILTERS]
                [--with-billing BILLING_PUBKEY] [--blacklist BLACKLIST]
                [--whitelist WHITELIST] [--sdk SDK_VERSION]
                [--minsdk MIN_SDK_VERSION] [--window] [--wakelock]
                [--add-jar ADD_JAR] [--meta-data META_DATA]
                [--resource RESOURCE] [--manifest-extra MANIFEST_EXTRA]
                [command [command ...]]
build.py: error: One of --dir, --private, or --launcher must be supplied.
# Command failed: python build.py --name 'Kivy Crash Course 2' --version 0.1 --package org.test # might be net.mooreworks.kivycrash2 --sdk 19 --minsdk 9 --private /home/dalem/PycharmProjects/kivy_crash_course/.buildozer/android/app --orientation sensor debug
# 
# Buildozer failed to execute the last command
# The error might be hidden in the log above this error
# Please read the full log, and search for it before
# raising an issue with buildozer itself.
# In case of a bug report, please add a full log with log_level = 2
"""