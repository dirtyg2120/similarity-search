#!/bin/bash

echo "Enter your query"
read query

output_dir="output-$(hdfs dfs -ls | wc -l)"
# run similarity search
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
        -Dmapreduce.map.env="q_from_user=$query" \
	-Dmapreduce.map.memory.mb=4096 \
	-Dmapreduce.reduce.memory.mb=4096 \
        -files /root/similarity_mapper.py,/root/similarity_reducer.py,  \
        -mapper similarity_mapper.py \
        -reducer similarity_reducer.py \
        -input output-inverted-index \
        -output $output_dir

# print the output of wordcount
echo -e "\nSimilairty Result"
hdfs dfs -cat $output_dir/part-*
