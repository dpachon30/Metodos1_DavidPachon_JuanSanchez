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
