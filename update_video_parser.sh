#!/bin/sh
python2.7 setup.py build
python3.7 setup.py build
cp -R ./build/lib.macosx-10.13-x86_64-2.7 ~/Projects/realscene/video_parser/third-party/pydemux/
cp -R ./build/lib.macosx-10.13-x86_64-3.7 ~/Projects/realscene/video_parser/third-party/pydemux/

