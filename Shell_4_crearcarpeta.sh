
b=0
for x in *;
do
	if [ $x == "data" ]
	then
		b=`expr $b + 1`
	fi
done


if [ $b -eq 0 ]
then
	mkdir data
	echo "Se ha creado la carpeta 'data'"
else
	echo "La carpeta ya se encuentra en el presente directorio"
fi

