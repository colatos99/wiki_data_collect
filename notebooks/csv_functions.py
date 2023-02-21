import pandas as pd
import numpy as np


#creates inititial dataframe for wiki pages

def create_main_df():
   data = {"page": [], "section_num": [], "word_num": []}
   main_df_csv = pd.DataFrame(data)
   return main_df_csv

def save_csv_file(data_df):
   data_df.to_csv("E:\python_projects\wiki_data_collect\data\\)" + "main_csv_file.csv")
   

def count_words(wiki_page_text):
   temp_num_list  = []
   total_num = 0
   num_counter = 0
   for text in wiki_page_text:
     temp_num = text.count(" ")
     temp_num_list.append(temp_num)
     temp_num = 0
   total_num = np.sum(temp_num_list)
   return total_num

def count_sections(wiki_page_text):
   section_total = 0
   section_num_list = []
  
   for text in wiki_page_text:
      temp_text = str.lower(text)
      temp_num = temp_text.count("section")
      section_num_list.append(temp_num)
      temp_num = 0
   section_total = np.sum(section_num_list)
   
   
   return section_total


def update_main_csv(df, page_name, word_count, section_count):
    new_df = df[len(df)] = [page_name,word_count,section_count]
   