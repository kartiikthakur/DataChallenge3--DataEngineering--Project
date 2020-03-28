# Insights Data Engineering Challenge

## Consumer Complaints
All the source code is in the src/complaints.py file.
1. Extract function to get the data from the file
2. Transform function to get the count, sum and percentage of unique product/year 
3. Load function to write the data into the final report.csv file

The script written is a simple python3 script which works fine for a million data points. But if the data increases then performance is a drawback. 

To increase the performance for huge datasets, we can:
1. Write a multi threaded version of the current python script
1. Execute the script in a cloud service which has a pre set infrastructure and which can be automatically scalable based on the size of the input. 
1. Dump the input complaints in the Hadoop Distributed File System and can perform the transformation using a Map Reduce, Hive or Pig.
1. Create a Spark version of the same python script using PySpark library which creates the resilient distributed datasets.

I have tested the program on the dataset with around 1.5 Million data rows and it works perfctly fine without any error. 
The program can be executed by directly running the ./src/complaints.py file or using a bash command. The command for the bash is mentioned in the "run.sh" shell script.

Comments have been added in the complaints.py file whereever required.
