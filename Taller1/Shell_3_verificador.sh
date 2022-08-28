#verificador de entradas

pass=0

Verificador () {
	if [ $1 -eq 0 -o $1 -eq 1 ];
	then 
		pass=1
	else
		echo  "Por favor intente de nuevo"
	fi
}


while [ $pass -eq 0 ]
do
	#Líneas para adaptar a leer la variable:
	echo "Ingrese un valor: "
	read VALOR
	c=$VALOR
	Verificador $c
done


