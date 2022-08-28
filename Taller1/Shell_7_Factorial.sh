#NOTA: Se toma como los n primeros números incluyendo al 0

#Líneas para ejecutable en terminal:
#echo "Ingrese la cantidad de números factoriales que desea conocer: \n:" 
#read v1
#valor=v1

#Líneas para ejecución bash (incluyendo el parámetro n)
#n=$1
#valor=$n


valor=20


factorial (){
	i=1
	b=$1
	if [ $b -le 1 ]
	then
		nf=1
	else
		while [ $b -gt 1 ]
		do
			i=`expr $i \* $b`
			b=`expr $b - 1`
		done
		nf=$i
	fi
}

for i in `seq 0 $valor`
do
	c=$i
	factorial $i
	echo "$c! = $nf"
done
