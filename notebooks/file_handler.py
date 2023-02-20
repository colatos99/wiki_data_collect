import os
import io
import pandas as pd


data_path_full = "E:\python_projects\wiki_data_collect\data\\"

page_path_full = "E:\python_projects\wiki_data_collect\wiki_pages\\"
print(data_path_full)

def get_page_path_full():
    return page_path_full
def get_data_path_full():
    return data_path_full

def  write_page_text(page_name=str, page=str):
    with open( page_path_full + str(page_name) + ".txt", 'x', encoding= 'utf-8' ) as page_file:
        if page_file.readlines() != None:
            print("File Already exists!")
        else:
            page_file.write(page)

def create_init_main_csv():
    csv_num = 1
    csv_info = {"csv_copy_num : [1]"}
    csv_info_df = pd.DataFrame(csv_info)
    csv_info_df.to_pickle(data_path_full + "csv_copy_num_store.pickle")
    
def show_csv_copy_info():
    info = pd.read_pickle(data_path_full + "csv_copy_num_store.pickle")
    return info