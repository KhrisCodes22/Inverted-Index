# Inverted-Index
This code contains two ways to build an inverted index from a set of .txt files, using Hadoops MapReduce, or just using regular python.
Note that this code works with python 2, and hasn't been tested with python 3.

To build the index the python way: run indexRegular.py, then queryRegularIndex.py to do the queries you want.

To build the index the hadoop way:
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar
-file mapper.py -mapper "python mapper.py"
-file reducer.py -reducer "python reducer.py"
-input /user/cloudera/inputAssignment1
-output /user/cloudera/outputAssignment1

Then merge the files into one file finalFile.txt
then run: cat finalFile.txt | indexMapReduce.py to build the index
then run: queryMapReduce.py to do your queries
