# Offline-surfex_forcing_mera
This Github contains a direcotry to create forcing files using MERA and offline-surfex-forcing  https://github.com/metno/pysurfex.
It is composed of 3 main sub-direcotry
 * deaccumulate_files deaccumulate data for accumulated MERA files
 * Convert_mera_files convert MERA deaccumulated MERA data on a format accepted by offline surfex forcing 
 * run_forcing create the forcing command and run offline-surfex-forcing 

These files were only tested with the MERA 3 hrs file but could be tested with the 33hrs and was only tested in my configuration

# 1 Install offline-surfex-forcing
Follow instructions from https://github.com/metno/pysurfex

# 2 Download MERA data
https://www.met.ie/climate/available-data/mera
Note the name of the directy where the data are saved for the reminder it will be called $/whereMERAfilesare

# 3 Clone the directory and go to the package files
git clone https://github.com/gbessardon/Offline-surfex_forcing_mera.git
cd /Offline-surfex_forcing_mera/Create_forcing_MERA/

# 4 Deaccumulate files

Offline-surfex-forcing currently (October 2020) do no handle well MERA deaccumulated files 

cd deaccumulate_files/
./deacumulate.sh {$/whereMERAfilesare}

deacumulate.sh will deaccumulate the values in the files however it does not change the timerangeindicator field (i.e the grin message will still say the grb message contained accumulated values). This is due to an issue with pygrib that brings the forecast time to zero once the timerangeindicator is changed.

# 5 Convert the deacumulated files

cd ../
cd /Convert_mera_files/input_files

####### Enter the configuration ##########
vi config_mera_conversion_to_offline_surfex_inputs.txt  
  Define where the MERA input files are stored most of them should be in /data/gbessardon/MERA/YYYY (or wherever you copy/link them to)
  Define where to save the hourly MERA files directory and header
  Define start time and end time
  Define the forecast length (3 or 33 (never been tested with 33 hours)) 
  Define the area filename in json (example /Convert_mera_files/input_files/domain.json is a 2.5 km grid over Ireland, domain_dub_airport.json is a 300m domain of 128*128 points centred on Dublin airport)
 Define the forcing filename
 Define the name of the create_forcing configuration suggestion
 Define the user configuration file (example /Create_forcing_MERA/run_forcing/input_files/user.yml offset the offset from the start of the forecast for MERA 0 fcint is the length of the forecast in seconds here 3*3600=10800)
:wq
cd ..
./convert_mera_files.sh {/$whereConvert_mera_filesis}/Create_forcing_MERA/Convert_mera_files/input_files/config_mera_conversion_to_offline_surfex_inputs.txt
Note than convert_mera_files.sh is found in Create_forcing_MERA/Convert_mera_files

This steps creates hourly MERA files and a suggestion of configuration for offline-surfex-forcing here Create_forcing_MERA/run_forcing/input_files/create_forcing_config.txt

# 6 Create forcing using runforcing_options.sh
/Create_forcing_MERA/run_forcing/
vi input_files/create_forcing_config.txt ## check if you are happy with the proposed configuration
./create_forcing_comand_and_run.sh /data/gbessardon/Create_forcing_MERA/run_forcing/input_files/create_forcing_config.txt
./create_forcing_comand_and_run.sh creates the command to run offline-surfex-forcing and runs it to create a forcing file to be used in SURFEX

# 7 Use the created forcing in SURFEX
How to install SURFEX is described here http://www.umr-cnrm.fr/surfex/


# MERA data references 
Eoin Whelan, Emily Gleeson, John Hanley, “An Evaluation of MÉRA, a High-Resolution Mesoscale Regional Reanalysis“. J. Appl. Meteor. Climatol., 57, 2179–2196, https://doi.org/10.1175/JAMC-D-17-0354.1, 2018.

Gleeson, E., Whelan, E., and Hanley, J.: “Met Éireann high resolution reanalysis for Ireland”, Adv. Sci. Res., 14, 49-61, https://doi.org/10.5194/asr-14-49-2017, 2017.

Eoin Whelan, John Hanley, Emily Gleeson, “The MÉRA Data Archive“. Met Éireann Technical Note No. 65, http://hdl.handle.net/2262/81711, 2017.

Emily Gleeson, Eoin Whelan, “Met Éireann’s contribution to package D6.2 of the JPI Climate INDECIS climate indices project“. Met Éireann Technical Note No. 67, http://hdl.handle.net/2262/91470, 2020.
