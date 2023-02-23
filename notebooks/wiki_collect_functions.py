# get Wikipediapage function
import wikipediaapi


def setup_wiki_api():
    wiki_wiki =  wikipediaapi.Wikipedia(
    language = 'en',
    extract_format=wikipediaapi.ExtractFormat.WIKI)
    return wiki_wiki

    
'''
wiki_wiki = wikipediaapi.Wikipedia(
    language = 'en',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)
'''


def get_page_full(wiki_page_name):
    p_wiki = setup_wiki_api()
    full_page = p_wiki.page(wiki_page_name) 
    return full_page
