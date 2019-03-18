#!/usr/bin/env python

## How to use:
# utils -i <input-filename> -o <output-filename>
# Example: utils -i input.tsv -o output.csv

import  csv
import argparse


GENDER_MALE = 'male'
GENDER_FEMALE = 'female'

GENDER_POSITION = 1
AGE_POSITION = 2

STATE_POSITION = 4

STATES = [
    'acre', 'ac,',
    'alagoas', 'al',
    'amapá', 'ap',
    'amazonas', 'am',
    'bahia', 'ba',
    'ceará', 'ce',
    'distrito federal', 'df',
    'espírito santo', 'es',
    'goiás', 'go',
    'maranhão', 'ma',
    'mato grosso', 'mt',
    'mato grosso do sul', 'ms',
    'minas gerais', 'mg',
    'pará', 'pa',
    'paraíba', 'pb',
    'paraná', 'pr',
    'pernambuco', 'pe',
    'piauí', 'pi',
    'rio de janeiro', 'rj',
    'rio grande do norte', 'rn',
    'rio grande do sul', 'rs',
    'rondônia', 'ro',
    'roraima', 'rr',
    'santa catarina', 'sc',
    'são paulo', 'sp',
    'sergipe', 'se' ,
    'tocantins', 'to'
]


def csv_to_lowercase(filename, output):
    """This function convert uppercase letters to lowercase."""
    
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        table = list(spamreader)
        for idx, row in enumerate(table):
            table[idx] = [item.lower() for item in row]

    output_file = '{}'.format(output)
    writer = csv.writer(open(output_file, 'w'), delimiter='\t') 
    writer.writerows(table)


def load_file(filename):
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        table = list(spamreader)
    return table


def count_gender(filename):
    male = 0
    female = 0
    for row in load_file(filename):
        gender = row[GENDER_POSITION].strip()
        if gender.lower() == GENDER_MALE:
            male += 1
        elif gender.lower() == GENDER_FEMALE:
            female += 1
        else:
            print('Gender not supported: {}'.format(gender))
    return male, female


def average_age(filename):
    counter = 0
    sum_age = 0
    for row in load_file(filename):
        try:
            age = int(row[AGE_POSITION].strip())
            counter += 1
        except ValueError:
            print('Age not supported: {}'.format(row[AGE_POSITION].strip()))
            continue
        sum_age += age
    return sum_age/counter, counter
        

def count_state(filename):
    l = []
    for row in load_file(filename):
        state = row[STATE_POSITION].strip()
        
            
    return  0

        
            

   


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input filename')
    parser.add_argument('-o', '--output', help='Output filename')
    args = parser.parse_args()

    male, female = count_gender('outtest.tsv')
    print(male, female)
    average, counter = average_age('outtest.tsv')
    print(counter, average)
    state = count_state('outtest.tsv')
    print(l)
    

    #csv_to_lowercase(args.input, args.output)

