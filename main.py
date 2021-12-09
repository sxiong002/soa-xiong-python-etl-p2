from datetime import datetime
from pgsql import query
import sql
import requests
import json


def get_movie_data(title):
    headers = {"Authorization": "9855f49b"}
    request_url = f"https://www.omdbapi.com/?t={title}&apikey=686eed26"
    return requests.get(request_url, headers=headers).json()


if __name__ == '__main__':
    # calls sql.py to create schema
    query(sql.create_schema, [""])

    # calls sql.py to drop table movie_list
    # query(sql.drop_table, [""])

    # calls sql.py to create table
    query(sql.create_table, [""])

    titleList = []
    f = open('datasets/json/movies.json')
    data = json.load(f)
    for i in data:
        # add if statement
        if (i['year'] >= 2018):
            # append titles to titles array
            titleList.append(i['title'])
    # print(titleList)

    titleList2 = []
    # get some movie data from the API
    for x in range(len(titleList)):
        data2 = get_movie_data(titleList[x])
        titleList2.append(data2)
    # print(titlelist2)
    # print(get_movie_data('WarGames'))
    print(len(titleList2))

    englishMovies = []
    for row in titleList2:
        if row['Response'] != 'False' and 'English' in row['Language']:
            englishMovies.append(row)
    # print(englishMovies)
    print(len(englishMovies))

    not_NA = []
    for row in englishMovies:
        if 'N/A' not in row['Title']:
            if 'N/A' not in row['Rated']:
                if 'N/A' not in row['Released']:
                    if 'N/A' not in row['Runtime']:
                        if 'N/A' not in row['Genre']:
                            if 'N/A' not in row['Director']:
                                if 'N/A' not in row['Writer']:
                                    if 'N/A' not in row['Actors']:
                                        if 'N/A' not in row['Plot']:
                                            if 'N/A' not in row['Awards']:
                                                if 'N/A' not in row['Poster']:
                                                    not_NA.append(row)
    print(len(not_NA))

    for row in not_NA:
        if (datetime.strptime(row['Released'], '%d %b %Y').year >= 2018):
            finalMovies = []
            finalMovies.append(row['Title'])
            finalMovies.append(row['Rated'])
            info = row['Released']
            finalMovies.append(datetime.strptime(info, "%d %b %Y"))
            info = row['Runtime']
            finalMovies.append(info.strip(' min'))
            finalMovies.append(row['Genre'].split(', '))
            finalMovies.append(row['Director'])
            finalMovies.append(row['Writer'].split(', '))
            finalMovies.append(row['Actors'].split(', '))
            finalMovies.append(row['Plot'])
            finalMovies.append(row['Awards'])
            finalMovies.append(row['Poster'])
            query(sql.insert_data, finalMovies)
    #print(len(finalMovies))
    #print(finalMovies)

    # not_NA.append(row['Title'])
    # print(len(not_NA))
    # print(not_NA)
    # print(row)
    # dataset = []
    # info = []
    # dataset.append(row['Title'])
    # dataset.append(row['Rated'])
    # info = row['Released']
    # dataset.append(datetime.strptime(info, "%d %b %Y"))
    # print(dataset)
    # info = row['Runtime']
    # convert = info.strip('min')
    # dataset.append(convert)
    # dataset.append(row['Runtime'])
    # dataset.append(row['Genre'])
    # dataset.append(row['Director'])
    # dataset.append(row['Writer'])
    # dataset.append(list(row['Actors']))
    # dataset.append(row['Plot'])
    # dataset.append(row['Awards'])
    # dataset.append(row['Poster'])
    # query(sql.insert_data, dataset)
    # print(dataset)

    # titleList3 = json.dumps(titlelist2)
    # movielist = json.load(titleList3)

    # if dataset['Response'] != 'False' and 'English' in dataset['Language']:
