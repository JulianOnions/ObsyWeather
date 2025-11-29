#! /bin/bash

SAVEDATA=/home/nas/WindRainData

for i in $SAVEDATA/Rain*.P
do
echo $i
[ ! -f "$i" ] && continue
b=$(echo $i | sed 's/\.P//' )
python /home/nas/ObsyWeather/uploadrain.py $i && mv $i $b || exit 1
done


for i in $SAVEDATA/Wind*.P
do
echo $i
[ ! -f "$i" ] && continue
b=$(echo $i | sed 's/\.P//' )
python /home/nas/ObsyWeather/uploadwind.py $i && mv $i $b || exit 1
done

