#!/usr/bin/env bash
FN=${1?Error: no filename name given}
rm create_forcing_command.py
file=$PWD/scripts/create_forcing_command.py
ln -s $file .
python3 create_forcing_command.py $FN