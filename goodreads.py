#!/usr/bin/env python3
import urllib.parse
import json
import requests
import xmltodict

#Video Link:
#https://www.youtube.com/watch?v=TDQ2jVtqM6Q&feature=youtu.be&ab_channel=Zyraix

while True:
    #Show text and ask for input of the a book to look for.
    print("Find your book by title, author or ISBN")
    print("Type q or quit to stop.")
    book = input('What book are you looking for?: ')
    if book == 'q' or book =='quit':
        break

    #Build URL for the equest to the goodreads directions API
    #Main Url
    main_api = "https://www.goodreads.com/search/index.xml?" #Main Url
    #Input (book name)
    q = book
    #Developer key
    key = "iezVgrfCrMNhvoFY2fSlgg" 

    #API url samenbrengen
    url = main_api + urllib.parse.urlencode({"key":key,"q":book}) 
 
    #Save XML file from URL
    response = requests.get(url)
    with open('books.xml','wb') as file: 
        file.write(response.content)
        
    #Convert XML to Json
    with open('books.xml') as xml_file: 
        data_dict = xmltodict.parse(xml_file.read()) 
        xml_file.close() 
       
        #Corresponding to json data 
        json_data = json.dumps(data_dict) 
      
        #Make json file 
        with open("books.json", "w") as json_file: 
            json_file.write(json_data) 
            json_file.close() 

        #Print Data from Json file
        with open('books.json') as json_file:
            data = json.load(json_file)
        
            #print(data['GoodreadsResponse']['search']['results']['work'])
            print("=========================Results Found=========================")
            for x in range(10):
                if data != "":
                    print(data['GoodreadsResponse']['search']['results']['work'][x]['best_book']['title'])
                else:     
                    print("Sorry couldn't find it :(")
            print("===============================================================")
            