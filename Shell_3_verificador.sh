#verificador de entradas

pass=0

Verificador () {
	echo "$VALOR"
	if [ $1 == 0 ]
	then 
		pass=1
	else
		echo "Por favor intente de nuevo"
	fi
}


while [ $pass -eq 0 ]
do
	echo "Ingrese un valor: "
	read VALOR
	Verificador VALOR
done


