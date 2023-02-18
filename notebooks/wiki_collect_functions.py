# get Wikipediapage function
import wikipediaapi



wiki_wiki = wikipediaapi.Wikipedia(
    language = 'en',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)



def get_page_full(wiki_page_name):
    p_wiki = wiki_wiki.page(wiki_page_name) 
    return p_wiki