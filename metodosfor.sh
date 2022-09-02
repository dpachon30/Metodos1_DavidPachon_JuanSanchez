valor=$1

for (( i=0; i <= $valor; ++i ))
do
	echo "$i"
done

for i in `seq 0 $valor`
do
	echo "es $i"
done
