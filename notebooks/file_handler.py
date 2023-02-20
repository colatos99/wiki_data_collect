import os
import io
home_dir =".wiki_data_collect"
data_dir = "data"
data_path_full = "E:\python_projects\wiki_data_collect\wiki_pages\\"
page_text_dir = "wiki_pages/"
page_path_full = "E:\python_projects\wiki_data_collect\wiki_pages\\"
print(data_path_full)

def get_page_path_full():
    return page_path_full
def get_data_path_full():
    return data_path_full

def  write_page_text(page_name=str, page=str):
    with open( page_path_full + str(page_name) + ".txt", 'w', encoding= 'utf-8' ) as f:
        f.write(page)
