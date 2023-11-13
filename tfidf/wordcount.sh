#!/bin/bash

# create input files
mkdir input 2> /dev/null
# total_map=$(expr $(hdfs dfs -ls $input_phase1_dir | wc -l) - 2)
# unique_idx=$(expr $(hdfs dfs -ls -d output-phase1* | wc -l))
inverted_index_dir="outputput"

echo "Results will be output to $inverted_index_dir"

# create input directory on HDFS
hadoop fs -mkdir -p input 2> /dev/null

# put input files to HDFS
hdfs dfs -put ./input/* input 2> /dev/null

# run wordcount
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
        -Dmapreduce.task.timeout=0 \
	-Dmapreduce.map.memory.mb=4096 \
	-Dmapreduce.reduce.memory.mb=4096 \
        -files /root/tfidf/1_wordcount_mapper.py,/root/tfidf/1_wordcount_reducer.py \
        -mapper 1_wordcount_mapper.py \
        -reducer 1_wordcount_reducer.py \
        -input input/* \
        -output $inverted_index_dir

# print the output of wordcount
echo -e "\nInverted Index Output"
hdfs dfs -cat $inverted_index_dir/part-*