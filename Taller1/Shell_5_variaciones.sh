#Líneas para ejecución bash:
#n=$1
#r=$2

#Líneas para ejecutable en terminal:
#echo "Ingrese el valor para n: "
#read v1
#echo "Ingrese el valor para r: "
#read v2
#n=$v1
#r=$v2


n=20
r=3
dif=`expr $n - $r`

factorial (){
	i=1
	if [ $1 -le 1 ]
	then
		nf=1
	else
		c=$1
		while [ $c -gt 1 ]
		do
			i=`expr $i \* $c`
			c=`expr $c - 1`
		done
		nf=$i
	fi
}

factorial $n
a=$nf

factorial $dif
b=$nf

echo "`expr $a / $b`"
