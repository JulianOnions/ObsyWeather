#! /bin/sh
# upload data and save it

set -xv
cd /home/nas/ObsyWeather

RAINDATA=/home/nas/RAIN_Guage/Final_Code/rainfall_data.txt
WINDDATA=/home/nas/PZEM017modbus/modbus_data.txt
SAVEDATA=/home/nas/WindRainData

# date stamp
date=$(date +%Y-%m-%d-%H-%M-%S)

RAINSAVE=$SAVEDATA/Rain-$date.csv
WINDSAVE=$SAVEDATA/Wind-$date.csv

# move the files to a save directory
mv $RAINDATA $RAINSAVE.P
mv $WINDDATA $WINDSAVE.P
# pause just in case of mid write
sleep 2

# now uplod these saved files
python /home/nas/ObsyWeather/uploadrain.py $RAINSAVE.P && mv $RAINSAVE.P $RAINSAVE
python /home/nas/ObsyWeather/uploadwind.py $WINDSAVE.P && mv $WINDSAVE.P $WINDSAVE

