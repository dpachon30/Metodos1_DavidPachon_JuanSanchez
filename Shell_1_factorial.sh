echo "Bienvenido a la calculadora de número factorial\n"
echo "Ingresa el número factorial que deseas conocer"

read VALOR

i=1
num=$VALOR

if [ $VALOR -le 1 ]
then
	echo "Factorial de $VALOR es 1"
else
	while [ $VALOR -gt 1 ]
	do
		i=`expr $i \* $VALOR`
		VALOR=`expr $VALOR - 1`

	done
	
	echo "Factorial de $num es $i"
fi


