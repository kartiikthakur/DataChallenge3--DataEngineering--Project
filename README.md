# Data Engineering Challenge

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

I have tested the program on the dataset with around 1.5 Million data rows and it works perfctly fine without any error. The output for this data with 1.5 million data is uploaded in the "insight_testsuite/tests/myown_test/output/report.csv" location. I couldn't add the input file because of the size restriction from the github.

The program can be executed by directly running the ./src/complaints.py file or using a bash command. The command for the bash is mentioned in the "run.sh" shell script.

## Edge Cases
1. If there are multiple complaints file in the input folder then those files can be iterated and the corresponding output can be written in report1.csv, report2.csv . . 
2. For now, as there is only one input and output file, the names of the files are hard coded but they can also be read during run time by passing as arguments in the bash command.
Example: python3.7 ./src/consumer_complaints.py ./input/consumer_complaints.csv ./output/report.csv


Comments have been added in the complaints.py file where ever required.
