#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/





import os,sys,inspect
filename = os.path.abspath(inspect.getfile(inspect.currentframe()))
filename = filename.split("\\")[-1]
filename = filename.split('.')[0]
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import re
import pandas as pd




"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

from bs4 import BeautifulSoup
import re


def extract_names(filename):
    #Return year and names in Alphabetical order
    file=open(filename, 'r')
    soup = BeautifulSoup(file,"html.parser")      
        
    Table= soup.find('table', {'summary':"Popularity for top 1000"} ) 
    Rows = Table.find_all('tr',recursive = False)
    for row in Rows:
        data = row.find_all('td')
        names = []
        for td in data:
            names.append(td.text)
        
            
    FinalList = []       
    for i in range(0,len(names),3):
        # print(i)
        FinalList.append(names[i:i+3])
        
    FinalList = FinalList[0:999]   
    def Extract(FinalList , ind): 
        return [item[ind] for item in FinalList]
    
          
    BoyNames = pd.Series(Extract(FinalList,1))
    GirlsNames = pd.Series(Extract(FinalList,2))
    
    BoyGirlNames = pd.concat([BoyNames,GirlsNames])
    BoyGirlNames.sort_values(inplace=True) 
    # BoyGirlNames.reset_index(inplace=True)
    # BoyGirlNames.index
    
    BoyGirlNames = pd.DataFrame(list(zip(BoyGirlNames.values,BoyGirlNames.index)),columns=['name' , 'rank'])     
    BoyGirlNames['rank'] =BoyGirlNames['rank']+1
    NamesList =[] 
    # year = ''.join([i for i in filename if i.isdigit()])
    import re
    year = re.findall('\d+',filename)
    NamesList.extend(year)
    for i in range(BoyGirlNames.shape[0]):
        NamesList.extend([BoyGirlNames.loc[i,'name']+" "+str(BoyGirlNames.loc[i,'rank'])])
        
    return NamesList


def main():
    filename = str(input('Please enter Filename : '))
     
    # text = ','.join(NamesList)
    return extract_names(filename)
    
    
main()



# def main():
#   # This command-line parsing code is provided.
#   # Make a list of command line arguments, omitting the [0] element
#   # which is the script itself.
#   args = sys.argv[1:]

#   if not args:
#     print 'usage: [--summaryfile] file [file ...]'
#     sys.exit(1)

#   # Notice the summary flag and remove it from args if it is present.
#   summary = False
#   if args[0] == '--summaryfile':
#     summary = True
#     del args[0]

#   # +++your code here+++
#   # For each filename, get the names, then either print the text output
#   # or write it to a summary file
  
# if __name__ == '__main__':
#   main()
