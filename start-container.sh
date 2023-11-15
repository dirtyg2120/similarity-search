#!/bin/bash

# the default node number is 3
N=$(cat config/slaves | wc -l)


# start hadoop master container
echo "remove old hadoop-master"
sudo docker rm -f hadoop-master &> /dev/null
echo "start hadoop-master container..."
sudo docker run -itd \
                --net=hadoop \
                -p 24000:24000 \
                -p 8088:8088 \
                --name hadoop-master \
                --hostname hadoop-master \
                abc &> /dev/null


# start hadoop slave container
echo "remove old hadoop-slave: total $N"
i=1
while [ $i -lt $(($N + 1)) ]
do
	sudo docker rm -f hadoop-slave$i &> /dev/null
	echo "start hadoop-slave$i container..."
	sudo docker run -itd \
	                --net=hadoop \
					-p 804$i:804$i \
	                --name hadoop-slave$i \
	                --hostname hadoop-slave$i \
	                abc &> /dev/null
	i=$(( $i + 1 ))
done 

# get into hadoop master container
sudo docker exec -it hadoop-master bash
