#! /bin/bash

case "$1" in
	debug) DEBUG=echo ;;
esac
SAVEDATA=/home/nas/Documents/Data/Upload_data

cd /home/nas/Documents/Code/Upload_code
source bin/activate

for i in $SAVEDATA/Rain*.P
do
echo $i
[ ! -f "$i" ] && continue
b=$(echo $i | sed 's/\.P//' )
$DEBUG python ./uploadrain.py $i && mv $i $b || exit 1
done


for i in $SAVEDATA/Wind*.P
do
echo $i
[ ! -f "$i" ] && continue
b=$(echo $i | sed 's/\.P//' )
$DEBUG python ./uploadwind.py $i && mv $i $b || exit 1
done
