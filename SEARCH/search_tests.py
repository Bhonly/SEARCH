from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)
   
    def test_keyword_to_titles_basic(self):
        result1 = keyword_to_titles([['Python Basics', 'John Doe', 1638051200, 1200, ['python', 'programming', 'basics']],
                                    ['Data Science with Python', 'Jane Smith', 1638105600, 2500, ['data science', 'python', 'tutorial']],
                                    ['Healthy Eating Tips', 'Alice Johnson', 1638153600, 800, ['healthy', 'eating', 'nutrition']]])
        assert result1 == {'python': ['Python Basics', 'Data Science with Python'],
                        'programming': ['Python Basics'],
                        'basics': ['Python Basics'],
                        'data science': ['Data Science with Python'],
                        'tutorial': ['Data Science with Python'],
                        'healthy': ['Healthy Eating Tips'],
                        'eating': ['Healthy Eating Tips'],
                        'nutrition': ['Healthy Eating Tips']}

        result2 = keyword_to_titles([['Art of Painting', 'Bob Ross', 1638182400, 1500, ['art', 'painting', 'tutorial']],
                                    ['Machine Learning Fundamentals', 'Alice Johnson', 1638225600, 2000, ['machine learning', 'fundamentals', 'python']],
                                    ['Gardening Tips', 'Mary Green', 1638273600, 1200, ['gardening', 'tips', 'plants']]])
        assert result2 == {'art': ['Art of Painting'],
                        'painting': ['Art of Painting'],
                        'tutorial': ['Art of Painting'],
                        'machine learning': ['Machine Learning Fundamentals'],
                        'fundamentals': ['Machine Learning Fundamentals'],
                        'python': ['Machine Learning Fundamentals'],
                        'gardening': ['Gardening Tips'],
                        'tips': ['Gardening Tips'],
                        'plants': ['Gardening Tips']}

        result3 = keyword_to_titles([['Space Exploration', 'Elon Musk', 1638302400, 1800, ['space', 'exploration', 'technology']],
                                    ['Healthy Recipes', 'Alice Johnson', 1638345600, 1200, ['healthy', 'recipes', 'cooking']],
                                    ['History of Jazz', 'Charlie Parker', 1638393600, 2500, ['history', 'jazz', 'music']]])
        assert result3 == {'space': ['Space Exploration'],
                        'exploration': ['Space Exploration'],
                        'technology': ['Space Exploration'],
                        'healthy': ['Healthy Recipes'],
                        'recipes': ['Healthy Recipes'],
                        'cooking': ['Healthy Recipes'],
                        'history': ['History of Jazz'],
                        'jazz': ['History of Jazz'],
                        'music': ['History of Jazz']}


    def test_title_to_info_basic(self):
        result1 = title_to_info([['Python Basics', 'John Doe', 1638051200, 1200, ['python', 'programming', 'basics']],
                                ['Data Science with Python', 'Jane Smith', 1638105600, 2500, ['data science', 'python', 'tutorial']],
                                ['Healthy Eating Tips', 'Alice Johnson', 1638153600, 800, ['healthy', 'eating', 'nutrition']]])
        assert result1 == {'Python Basics': {'author': 'John Doe', 'timestamp': 1638051200, 'length': 1200},
                        'Data Science with Python': {'author': 'Jane Smith', 'timestamp': 1638105600, 'length': 2500},
                        'Healthy Eating Tips': {'author': 'Alice Johnson', 'timestamp': 1638153600, 'length': 800}}

       
        result2 = title_to_info([['Art of Painting', 'Bob Ross', 1638182400, 1500, ['art', 'painting', 'tutorial']],
                                ['Machine Learning Fundamentals', 'Alice Johnson', 1638225600, 2000, ['machine learning', 'fundamentals', 'python']],
                                ['Gardening Tips', 'Mary Green', 1638273600, 1200, ['gardening', 'tips', 'plants']]])
        assert result2 == {'Art of Painting': {'author': 'Bob Ross', 'timestamp': 1638182400, 'length': 1500},
                        'Machine Learning Fundamentals': {'author': 'Alice Johnson', 'timestamp': 1638225600, 'length': 2000},
                        'Gardening Tips': {'author': 'Mary Green', 'timestamp': 1638273600, 'length': 1200}}

        result3 = title_to_info([['Space Exploration', 'Elon Musk', 1638302400, 1800, ['space', 'exploration', 'technology']],
                                ['Healthy Recipes', 'Alice Johnson', 1638345600, 1200, ['healthy', 'recipes', 'cooking']],
                                ['History of Jazz', 'Charlie Parker', 1638393600, 2500, ['history', 'jazz', 'music']]])
        assert result3 == {'Space Exploration': {'author': 'Elon Musk', 'timestamp': 1638302400, 'length': 1800},
                        'Healthy Recipes': {'author': 'Alice Johnson', 'timestamp': 1638345600, 'length': 1200},
                        'History of Jazz': {'author': 'Charlie Parker', 'timestamp': 1638393600, 'length': 2500}}


    def test_search_basic(self):
        result1 = search('python', {'python': ['Python Basics', 'Data Science with Python'],
                                    'programming': ['Python Basics'],
                                    'basics': ['Python Basics'],
                                    'data science': ['Data Science with Python'],
                                    'tutorial': ['Data Science with Python'],
                                    'healthy': ['Healthy Eating Tips'],
                                    'eating': ['Healthy Eating Tips'],
                                    'nutrition': ['Healthy Eating Tips']})
        assert result1 == ['Python Basics', 'Data Science with Python']

        
        result2 = search('art', {'art': ['Art of Painting'],
                                'painting': ['Art of Painting'],
                                'tutorial': ['Art of Painting'],
                                'machine learning': ['Machine Learning Fundamentals'],
                                'fundamentals': ['Machine Learning Fundamentals'],
                                'python': ['Machine Learning Fundamentals'],
                                'gardening': ['Gardening Tips'],
                                'tips': ['Gardening Tips'],
                                'plants': ['Gardening Tips']})
        assert result2 == ['Art of Painting']

        result3 = search('history', {'space': ['Space Exploration'],
                                    'exploration': ['Space Exploration'],
                                    'technology': ['Space Exploration'],
                                    'healthy': ['Healthy Recipes'],
                                    'recipes': ['Healthy Recipes'],
                                    'cooking': ['Healthy Recipes'],
                                    'history': ['History of Jazz'],
                                    'jazz': ['History of Jazz'],
                                    'music': ['History of Jazz']})
        assert result3 == ['History of Jazz']

    def test_article_length(self):
        result1 = article_length(1500, ['Python Basics', 'Data Science with Python', 'Machine Learning Fundamentals'],
                                {'Python Basics': {'author': 'John Doe', 'timestamp': 1638051200, 'length': 1200},
                                'Data Science with Python': {'author': 'Jane Smith', 'timestamp': 1638105600, 'length': 2500},
                                'Machine Learning Fundamentals': {'author': 'Alice Johnson', 'timestamp': 1638225600, 'length': 2000}})
        assert result1 == ['Python Basics']

       
        result2 = article_length(1500, [], {'Python Basics': {'author': 'John Doe', 'timestamp': 1638051200, 'length': 1200}})
        assert result2 == []

        
        result3 = article_length(0, ['Python Basics', 'Data Science with Python'],
                                {'Python Basics': {'author': 'John Doe', 'timestamp': 1638051200, 'length': 1200},
                                'Data Science with Python': {'author': 'Jane Smith', 'timestamp': 1638105600, 'length': 2500}})
        assert result3 == []
    def test_key_by_author_basic(self):
        result1 = key_by_author(['Python Basics', 'Data Science with Python'],
                                {'Python Basics': {'author': 'John Doe', 'timestamp': 1638051200, 'length': 1200},
                                'Data Science with Python': {'author': 'Jane Smith', 'timestamp': 1638105600, 'length': 2500}})
        assert result1 == {'John Doe': ['Python Basics'], 'Jane Smith': ['Data Science with Python']}

        result2 = key_by_author(['Art of Painting', 'Machine Learning Fundamentals', 'Gardening Tips'],
                                {'Art of Painting': {'author': 'Bob Ross', 'timestamp': 1638182400, 'length': 1500},
                                'Machine Learning Fundamentals': {'author': 'Alice Johnson', 'timestamp': 1638225600, 'length': 2000},
                                'Gardening Tips': {'author': 'Mary Green', 'timestamp': 1638273600, 'length': 1200}})
        assert result2 == {'Bob Ross': ['Art of Painting'], 'Alice Johnson': ['Machine Learning Fundamentals'],
                        'Mary Green': ['Gardening Tips']}

        result3 = key_by_author(['Space Exploration', 'Healthy Recipes', 'History of Jazz'],
                                {'Space Exploration': {'author': 'Elon Musk', 'timestamp': 1638302400, 'length': 1800},
                                'Healthy Recipes': {'author': 'Alice Johnson', 'timestamp': 1638345600, 'length': 1200},
                                'History of Jazz': {'author': 'Charlie Parker', 'timestamp': 1638393600, 'length': 2500}})
        assert result3 == {'Elon Musk': ['Space Exploration'], 'Alice Johnson': ['Healthy Recipes'],
                        'Charlie Parker': ['History of Jazz']}


    def test_filter_to_author_basic(self):
        result1 = filter_to_author('John Doe', ['Python Basics', 'Data Science with Python'],
                                {'Python Basics': {'author': 'John Doe', 'timestamp': 1638051200, 'length': 1200},
                                    'Data Science with Python': {'author': 'Jane Smith', 'timestamp': 1638105600, 'length': 2500}})
        assert result1 == ['Python Basics']


        result2 = filter_to_author('Bob Ross', ['Art of Painting', 'Machine Learning Fundamentals', 'Gardening Tips'],
                                {'Art of Painting': {'author': 'Bob Ross', 'timestamp': 1638182400, 'length': 1500},
                                    'Machine Learning Fundamentals': {'author': 'Alice Johnson', 'timestamp': 1638225600, 'length': 2000},
                                    'Gardening Tips': {'author': 'Mary Green', 'timestamp': 1638273600, 'length': 1200}})
        assert result2 == ['Art of Painting']

        result3 = filter_to_author('Alice Johnson', ['Space Exploration', 'Healthy Recipes', 'History of Jazz'],
                                {'Space Exploration': {'author': 'Elon Musk', 'timestamp': 1638302400, 'length': 1800},
                                    'Healthy Recipes': {'author': 'Alice Johnson', 'timestamp': 1638345600, 'length': 1200},
                                    'History of Jazz': {'author': 'Charlie Parker', 'timestamp': 1638393600, 'length': 2500}})
        assert result3 == ['Healthy Recipes']


    def test_filter_out_basic(self):
        result1 = filter_out('tutorial', ['Python Basics', 'Data Science with Python'],
                            {'python': ['Python Basics', 'Data Science with Python'],
                            'programming': ['Python Basics'],
                            'basics': ['Python Basics'],
                            'data science': ['Data Science with Python'],
                            'tutorial': ['Data Science with Python'],
                            'healthy': ['Healthy Eating Tips'],
                            'eating': ['Healthy Eating Tips'],
                            'nutrition': ['Healthy Eating Tips']})
        assert result1 == ['Python Basics']

        result2 = filter_out('gardening', ['Art of Painting', 'Machine Learning Fundamentals', 'Gardening Tips'],
                            {'art': ['Art of Painting'],
                            'painting': ['Art of Painting'],
                            'tutorial': ['Art of Painting'],
                            'machine learning': ['Machine Learning Fundamentals'],
                            'fundamentals': ['Machine Learning Fundamentals'],
                            'python': ['Machine Learning Fundamentals'],
                            'gardening': ['Gardening Tips'],
                            'tips': ['Gardening Tips'],
                            'plants': ['Gardening Tips']})
        assert result2 == ['Art of Painting', 'Machine Learning Fundamentals']

        result3 = filter_out('music', ['Space Exploration', 'Healthy Recipes', 'History of Jazz'],
                            {'space': ['Space Exploration'],
                            'exploration': ['Space Exploration'],
                            'healthy': ['Healthy Recipes'],
                            'recipes': ['Healthy Recipes'],
                            'history': ['History of Jazz'],
                            'jazz': ['History of Jazz'],
                            'music': ['History of Jazz'],
                            'musical': ['History of Jazz']})
        assert result3 == ['Space Exploration', 'Healthy Recipes']

    def test_articles_from_year(self):
        
        result1 = articles_from_year(2022, ['Python Basics', 'Data Science with Python', 'Machine Learning Fundamentals'],
                                    {'Python Basics': {'author': 'John Doe', 'timestamp': 1641024000, 'length': 1200},
                                    'Data Science with Python': {'author': 'Jane Smith', 'timestamp': 1641100800, 'length': 2500},
                                    'Machine Learning Fundamentals': {'author': 'Alice Johnson', 'timestamp': 1641187200, 'length': 2000}})
        assert result1 == ['Python Basics', 'Data Science with Python', 'Machine Learning Fundamentals']

        result2 = articles_from_year(2023, [], {'Python Basics': {'author': 'John Doe', 'timestamp': 1641024000, 'length': 1200}})
        assert result2 == []

        
        result3 = articles_from_year(2021, ['Python Basics', 'Data Science with Python', 'Machine Learning Fundamentals'],
                                    {'Python Basics': {'author': 'John Doe', 'timestamp': 1641024000, 'length': 1200},
                                    'Data Science with Python': {'author': 'Jane Smith', 'timestamp': 1641100800, 'length': 2500},
                                    'Machine Learning Fundamentals': {'author': 'Alice Johnson', 'timestamp': 1641187200, 'length': 2000}})
        assert result3 == []





    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_1(self, input_mock):
        keyword = 'fisk'
        advanced_option = 6        
   
        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option)  + "\nHere are your articles: ['Fisk University']\n"

        self.assertEqual(output, expected)    
    @patch('builtins.input')    
    def test_integration_test_2(self, input_mock):
        keyword = 'canadian'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'Jack Johnson': ['List of Canadian musicians'], 'RussBot': ['2009 in music'], 'Burna Boy': ['Lights (musician)', 'Will Johnson (soccer)', '2008 in music'], 'Bearcat': ['2007 in music']}\n"

        self.assertEqual(output, expected)  
    @patch('builtins.input')              
    def test_integration_test_3(self, input_mock):
        keyword = 'college'
        advanced_option = 1
        advanced_response = 50000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Fisk University']\n"

        self.assertEqual(output, expected)
    @patch('builtins.input')    
    def test_integration_test_4(self, input_mock):
        keyword = 'french'
        advanced_option = 3
        advanced_response = 'Mack Johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['French pop music']\n"

        self.assertEqual(output, expected)
    @patch('builtins.input')    
    def test_integration_test_5(self, input_mock):
        keyword = 'death'
        advanced_option = 4
        advanced_response = 'has'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['2009 in music', 'Sean Delaney (musician)']\n"

        self.assertEqual(output, expected)                
# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
