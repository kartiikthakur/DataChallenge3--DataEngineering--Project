# Insights Data Engineering Challenge

## Consumer Complaints
All the source code is in the src/complaints.py file.
Extract function to get the data from the file
Transform function to get the count, sum and percentage of unique product/year 
Load function to write the data into the final report.csv file

The script written is a simple python3 script which works fine for a million data points. But if the data increases then performance is a drawback. 

To increase the performance for huge datasets, we can:
1. Write a multi threaded version of the current python script
2. Execute the script in a cloud service which has an pre set infrastructure and which can be automatically scalable based on the size of the input
3. Dump the input complaints in the Hadoop Distributed File System and can perform the transformation using a Map Reduce, Hive or Pig.
4. Create a Spark version of the same python script using PySpark library which creates the resilient distributed datasets.
