"""
Author: Kartik Singh Thakur
Date: 3/27/2020
Data Engineering Challenge
"""

import os
import csv


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


# Get Input file location
def input():
    input_folder = os.path.abspath('../input')
    input_folder2 = os.path.abspath('../consumer_complaints/input')
    try:
        filename, file_extension = os.path.splitext(os.listdir(input_folder)[0])
        return input_folder, filename, file_extension

    except:
        filename, file_extension = os.path.splitext(os.listdir(input_folder2)[0])
        return input_folder2, filename, file_extension


# Extracting Data from Input file location
def extraction(input_file):
    output_list = []
    unique_product_year = []
    all_product_year = []
    with open(input_file, encoding='utf-8', newline="") as csvfile:
        filereader = csv.reader(csvfile)
        firstline = True
        count = 0
        for row in filereader:
            try:
                count += 1
                if firstline:  # skip first line
                    columns = row
                    firstline = False
                    continue

                product = row[1]
                if "," in product:  # Add double quotes if a "," exists in the Product name
                    new_product = "\"" + product + "\""
                    row[1] = listToString(new_product)

                # Creating a dictionary for all the rows in the input file
                each_row = {}
                for key, Column in enumerate(columns):
                    each_row[Column] = row[key]

                # Extracting all combinations of Product and Year match
                each_row['ProductYear'] = (row[1].lower() + "," + row[0].split("-")[0])
                all_product_year.append(each_row['ProductYear'])

                # Extracting Unique combinations of Product and Year match
                if each_row['ProductYear'] not in unique_product_year:
                    unique_product_year.append(each_row['ProductYear'])

                output_list.append(each_row)

            except Exception as e:
                print(e)
                print("Error while pre-processing the row with Complaint ID:" + str(row[-1]) + '\n')

    print("Number of rows extracted: " + str(count))
    print("Finished extracting the data\n")
    return output_list, unique_product_year, all_product_year


# Transforming Data as per the requirements in the problem statement
def transform(data, unique_lists, all_lists):
    unique_lists.sort(key=lambda x: x[1:len(x) - 1] if x[0] == '"' else x[0:len(x) - 1])  # Sorting the Products
    rows = []

    # Calculate Count, Sum, Percentage of Unique Product and Year match
    for unique_list in unique_lists:
        all_companies = [x['Company'] for x in data if x['ProductYear'] == unique_list]
        unique_company = set(all_companies)
        all_complaints = [all_companies.count(x) for x in unique_company]
        maximum_percentage = round((max(all_complaints) / sum(all_complaints)) * 100)
        ProductYear = unique_list.split(",")
        product = ",".join(ProductYear[0:len(ProductYear) - 1])
        year = ProductYear[-1]
        rows.append(
            [product, year, str(all_lists.count(unique_list)), str(len(unique_company)), str(maximum_percentage)])

    print("Finished transforming the data\n")
    return rows


# Writing the final data in a csv file
def load(rows):
    output_folder = os.path.abspath('../output')
    output_folder2 = os.path.abspath('../consumer_complaints/output')
    try:
        output_file = output_folder + '/' + 'report.csv'
    except:
        output_file = output_folder2 + '/' + 'report.csv'

    print(output_file)
    # Writing the final data into the report.csv file
    with open(output_file, 'w') as f:
        for x in rows:
            f.write(','.join(x) + '\n')

    print("Finished writing the report\n")


if __name__ == "__main__":
    input_folder, filename, file_extension = input()
    input_csv = os.path.join(input_folder, filename + file_extension)
    extracted_data, unique_ProductYear, all_ProductYear = extraction(input_csv)
    transformed_data = transform(extracted_data, unique_ProductYear, all_ProductYear)
    load(transformed_data)
