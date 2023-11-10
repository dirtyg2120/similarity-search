#!/bin/bash

# the default node number is 3
N=$(cat config/slaves | wc -l)


# start hadoop master container
echo "remove old hadoop-master"
sudo docker rm -f hadoop-master &> /dev/null


# start hadoop slave container
echo "remove old hadoop-slave: total $N"
i=1
while [ $i -lt $(($N + 1)) ]
do
	sudo docker rm -f hadoop-slave$i &> /dev/null
	i=$(( $i + 1 ))
done 

