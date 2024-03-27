from wiki import article_metadata, ask_search, ask_advanced_search
import datetime
import time

# FOR ALL OF THESE FUNCTIONS, READ THE FULL INSTRUCTIONS.

# 1) 
#
# Function: keyword_to_titles
#
# Parameters:
#   metadata - 2D list of article metadata containing 
#              [title, author, timestamp, article length, keywords]
#              for each article
#
# Return: dictionary mapping keyword to list of article titles in which the
#         articles contain keyword
#
# Example return value:
# {
#   'keyword': ['article title', 'article title 2']
#   'another_keyword': ['article title 2', 'article title 3']
# }
def keyword_to_titles(metadata): 
    new_metadata = {}
    for article in metadata:
        for keyword in article[4]:
            if keyword not in new_metadata:
                new_metadata[keyword] = []
            new_metadata[keyword].append(article[0])      
    return new_metadata 
        


# 2) 
#
# Function: title_to_info
#
# Parameters:
#   metadata - 2D list of article metadata containing 
#              [title, author, timestamp, article length, keywords]
#              for each article
#
# Return: dictionary mapping article title to a dictionary with the following
#         keys: author, timestamp, length of article. It may be assumed that
#         the input data has unique article titles.
#
# Example return value:
# {
#   'article title': {'author': 'some author', 'timestamp': 1234567890, 'length': 2491}
#   'article title 2': {'author': 'another author', 'timestamp': 9876543210, 'length': 85761}
# }
def title_to_info(metadata):
    new_metadata = {}
    for article in metadata:
        new_metadata[article[0]] = {}
        new_metadata[article[0]]['author'] = article[1]
        new_metadata[article[0]]['timestamp'] = article[2]
        new_metadata[article[0]]['length'] = article[3]
    return new_metadata  

# 3) 
#
# Function: search
#
# Parameters:
#   keyword - search word to look for
#   keyword_to_titles - dictionary mapping keyword to a list of all article
#                       titles containing that keyword
#
# Return: list of titles with articles containing the keyword, case-sensitive
#         or an empty list if none are found
def search(keyword, keyword_to_titles):
    result = []
    for article_keyword in keyword_to_titles:
        if article_keyword == keyword:
          result.extend(keyword_to_titles[article_keyword])
    return result        

# 4) 
#
# Function: article_length
#
# Parameters:
#   max_length - max character length of articles
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: list of article titles from given titles for articles that do not
#         exceed max_length number of characters
def article_length(max_length, article_titles, title_to_info):
    for article in title_to_info:
        if title_to_info[article]['length'] > max_length and article in article_titles:
             article_titles.remove(article)
    return article_titles  
#print(article_length(1000000, search('used',  keyword_to_titles([['Semaphore (programming)', 'Nihonjoe', 1144850850, 7616, ['semaphore', 'variable', 'used']]])), title_to_info([['Semaphore (programming)', 'Nihonjoe', 1144850850, 7616, ['semaphore', 'variable', 'used']]])))
     

# 5) 
#
# Function: key_by_author
#
# Parameters:
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: dictionary that maps author to a list of all articles titles written
#         by that author
#
# Example return value:
# {
#   'author': ['article title', 'article title 2'],
#   'another author': ['article title 3']
# }
def key_by_author(article_titles, title_to_info):
      author_dict = {}
      for title in article_titles:
        author = title_to_info[title]["author"]
        if author in author_dict:
            author_dict[author].append(title)
        else:
            author_dict[author] = [title]
      return author_dict
# print(key_by_author())      

# 6) 
#
# Function: filter_to_author
#
# Parameters:
#   author - author name to filter results to
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: list of article titles from the initial search written by the author
#         or an empty list if none.
def filter_to_author(author, article_titles, title_to_info):
    result = []
    for title in article_titles:
        if author == title_to_info[title]['author']:
           result.append(title)
    return result    


# 7) 
#
# Function: filter_out
#
# Parameters:
#   keyword - a second keyword to use to filter out results
#   article_titles - list of article titles resulting from basic search
#   keyword_to_titles - dictionary mapping keyword to a list of all article
#                       titles containing that keyword
#
# Return: list of articles from the basic search that do not include the
#         new keyword
def filter_out(keyword, article_titles, keyword_to_titles):
    article_titles_copy = article_titles.copy()    
    if keyword in keyword_to_titles:
        for title in article_titles:
            if title in keyword_to_titles[keyword]:
                article_titles_copy.remove(title)
    return article_titles_copy



# 8) 
#
# Function: articles_from_year
#
# Parameters:
#   year - year (ex: 2009) to filter articles to
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: list of article titles from the basic search that were published
#         during the provided year.
def articles_from_year(year, article_titles, title_to_info):
    result_titles = []
    todays_date1 = datetime.date(year, 1, 1)
    unix_timestamp1 = time.mktime(todays_date1.timetuple())
    todays_date2 = datetime.date(year, 12, 31)
    unix_timestamp2 = time.mktime(todays_date2.timetuple())
    for article in article_titles:
        if title_to_info[article]['timestamp'] >= int(unix_timestamp1) and title_to_info[article]['timestamp'] <= int(unix_timestamp2):
            result_titles.append(article)
    
    return result_titles



# Prints out articles based on searched keyword and advanced options
def display_result():
    # Preprocess all metadata to dictionaries
    keyword_to_titles_dict = keyword_to_titles(article_metadata())
    title_to_info_dict = title_to_info(article_metadata())
    
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search(), keyword_to_titles_dict)

    # advanced stores user's chosen advanced option (1-7)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max length of articles
        # Update articles to contain only ones not exceeding the maximum length
        articles = article_length(value, articles, title_to_info_dict)
    if advanced == 2:
        # Update articles to be a dictionary keyed by author
        articles = key_by_author(articles, title_to_info_dict)
    elif advanced == 3:
        # value stores author name
        # Update article metadata to only contain titles and timestamps
        articles = filter_to_author(value, articles, title_to_info_dict)
    elif advanced == 4:
        # value stores a second keyword
        # Filter articles to exclude those containing the new keyword.
        articles = filter_out(value, articles, keyword_to_titles_dict)
    elif advanced == 5:
        # value stores year as an int
        # Update article metadata to contain only articles from that year
        articles = articles_from_year(value, articles, title_to_info_dict)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

if __name__ == "__main__":
    display_result()
