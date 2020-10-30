#!/usr/bin/env bash
FN=${1?Error: no directory name given}
rm deacumulate.py
file=$PWD/scripts/deacumulate.py
ln -s $file .
python3 deacumulate.py $FN
