echo "Enter your query"
read query

mkdir input 2> /dev/null

total_map=$(ls input | wc -l)
unique_idx=$(expr $(hdfs dfs -ls | wc -l) / 2)
inverted_index_dir="output-inverted-index"

echo "Total map is $total_map"
echo "Results will be output to $inverted_index_dir"

# create input directory on HDFS
hadoop fs -mkdir -p input 2> /dev/null

# put input files to HDFS
hdfs dfs -put ./input/* input 2> /dev/null

# run wordcount
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
        -Dmapreduce.task.timeout=0 \
        -Dmapreduce.reduce.env="total_map_tasks=$total_map" \
	-Dmapreduce.map.memory.mb=4096 \
	-Dmapreduce.reduce.memory.mb=4096 \
        -files /root/inverted_index_mapper.py,/root/inverted_index_reducer.py \
        -mapper inverted_index_mapper.py \
        -reducer inverted_index_reducer.py \
        -input input \
        -output $inverted_index_dir

# print the output of wordcount
echo -e "\nInverted Index Output"
hdfs dfs -cat $inverted_index_dir/part-*



output_dir="output-$(hdfs dfs -ls | wc -l)"
# run similarity search
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
        -Dmapreduce.task.timeout=0 \
        -Dmapreduce.map.env="q_from_user=$query" \
	-Dmapreduce.map.memory.mb=4096 \
	-Dmapreduce.reduce.memory.mb=4096 \
        -files /root/jpii_mapper.py,/root/jpii_reducer.py,  \
        -mapper jpii_mapper.py \
        -reducer jpii_reducer.py \
        -input output-inverted-index \
        -output $output_dir

# print the output of wordcount
echo -e "\nSimilairty Result"
hdfs dfs -cat $output_dir/part-*