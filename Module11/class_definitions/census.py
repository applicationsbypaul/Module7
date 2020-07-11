"""
Program: census.py
Author: Paul Ford
Last date modified: 07/8/2020
Purpose: practice using svc files
"""

import csv


def get_data():
    """
    Opens the census files and places them in a dictionary
    the key is represented by rank
    :return: a dictionary of county census data
    """
    with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        # initialize empty dictionary
        county = {}
        for row in csv_reader:
            # skip the first line in the file because it is the header
            if line_count == 0:
                line_count += 1
                continue
            # create an item in dictionary county with a key of the county name and a value of the object
            county[str(row[1])] = Census(row[0], row[2], row[3], row[4], row[5], row[6], )
    return county


def delete_county(county1, county2, dict):
    """
    deletes a county from the dictionary list
    for the assignment just passing in the right names
    :param dict: dictionary of counties
    :param county2: str value of county wish to be deleted
    :param county1: str value of county wish to be deleted
    :return:
    """
    if county1 in dict:
        dict.pop(county1)
        print(county1 + ' has been removed.')
    else:
        print('cannot find')
    if county2 in dict:
        dict.pop(county2)
        print(county2 + 'removed from database')
    else:
        print('cannot find')


def find_population_per_household(county, dict):
    """
    finds the population per household
    :param county: the county we are searching for
    :param dict: dictionary of counites
    Prints the population per houseold
    """
    population = int(dict[county]._population.replace(',', ''))
    household = int(dict[county]._num_households.replace(',', ''))
    print(str(round(population / household, 0)) + ' persons per household')


def find_total_population(dict):
    """
    prints the total population
    :param dict: counties dictionary
    """
    pop_sum = 0
    for county in dict:
        pop_sum += int(dict[county]._population.replace(',', ''))
    print(str(pop_sum) + ' is the total population in Iowa')


class Census:
    """Census class"""

    def __init__(self, rank, cap_income, m_h_income, m_f_income, pop, num_house):
        """
        creates an object with data of the census
        :param county: County of the census
        :param cap_income: Per capita income
        :param m_h_income: Median household income
        :param m_f_income: Median family Income
        :param pop: population
        :param num_house: number of households
        """
        self._rank = rank
        self._per_cap_income = cap_income
        self._med_house_income = m_h_income
        self._med_family_income = m_f_income
        self._population = pop
        self._num_households = num_house


# Driver methods
counties = get_data()
delete_county('Iowa State', 'United States', counties)
find_population_per_household('Dallas', counties)
find_total_population(counties)
