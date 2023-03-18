import os
import io
#import pandas as pd


data_path_full = "E:\python_projects\wiki_data_collect\data\\"

page_path_full = "E:\python_projects\wiki_data_collect\wiki_pages\\"
print(data_path_full)

def get_page_path_full():
    return page_path_full
def get_data_path_full():
    return data_path_full

def  write_page_text(page_name=str, page=str):
    with open( page_path_full + str(page_name) + ".txt", 'x', encoding= 'utf-8' ) as page_file:
       
            page_file.write(page)
            
'''        
def read_page_text(page_name=str):
    with open(page_path_full + (page_name) + ".txt", 'r', encoding="utf-8") as page_file:
        page = page_file.readlines()
        return page
'''
'''
def create_init_main_csv():
    csv_num = 1
    csv_info = {"csv_copy_num : [1]"}
    csv_info_df = pd.DataFrame(csv_info)
    csv_info_df.to_pickle(data_path_full + "csv_copy_num_store.pickle")

    
def show_csv_copy_info():
    info = pd.read_pickle(data_path_full + "csv_copy_num_store.pickle")
    return info
'''
def write_csv_main(df_to_write):
    df_to_write.to_csv(data_path_full + "csv_main.csv", index=False)
    '''
    copy_info_df = pd.read_pickle(data_path_full  + "csv_copy_num_store.pickle")
    
    copy_num  = int(copy_info_df.iloc[0][0])
    copy_num += 1
    
    copy_info_df[0][0] = copy_num
    copy_info_df.to_pickle(data_path_full + "csv_copy_num_store.pickle")
    '''
def read_page_text(page):
     with open(page_path_full + page + ".txt", "r", encoding="utf-8") as page_file_r:
        page_read = page_file_r.readlines()
     return page_read
'''
def get_csv_main():
    
    csv_read = pd.read_csv(data_path_full + "csv_main.csv")
    return csv_read
'''