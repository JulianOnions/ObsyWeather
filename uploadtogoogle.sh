#! /bin/sh
# upload data and save it

DEBUG=
case "$1" in 
	debug) DEBUG=echo;;
esac
set -xv
cd /home/nas/Documents/Code/Upload_code

source bin/activate

RAINDATA=/home/nas/Documents/Data/Rain/rainfall_data.txt
WINDDATA=/home/nas/Documents/Modbus/modbus_data.txt
SAVEDATA=/home/nas/Documents/Data/Upload_data

# date stamp
date=$(date +%Y-%m-%d-%H-%M-%S)

RAINSAVE=$SAVEDATA/Rain-$date.csv
WINDSAVE=$SAVEDATA/Wind-$date.csv

# move the files to a save directory
$DEBUG mv $RAINDATA $RAINSAVE.P
$DEBUG mv $WINDDATA $WINDSAVE.P
# pause just in case of mid write
sleep 2

# now upload these saved files
if [ -f $RAINSAVE.P ]
then
$DEBUG python ./uploadrain.py $RAINSAVE.P && mv $RAINSAVE.P $RAINSAVE
fi
if [ -f $WINDSAVE.P ]
then
$DEBUG python ./uploadwind.py $WINDSAVE.P && mv $WINDSAVE.P $WINDSAVE
fi
