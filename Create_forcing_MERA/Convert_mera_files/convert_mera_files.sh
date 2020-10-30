#!/usr/bin/env bash
FN=${1?Error: no directory name given}
rm main.py
file=$PWD/scripts/main.py
ln -s $file .
python3 main.py $FN