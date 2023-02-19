import os
home_dir = "E:\python_projects\wiki_data_collect"
data_dir = "\data"
data_path_full = os.path.join(home_dir, data_dir)
page_text_dir = "\wiki_pages"
page_path_full = os.path.join(home_dir, page_text_dir)
print(data_path_full)

def get_page_path_full():
    return page_path_full
def get_data_path_full():
    return data_path_full

def  write_page_text(page_name):
    