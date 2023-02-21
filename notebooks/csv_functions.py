import pandas as pd


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
   for num in temp_num_list:
      total_num = int(num) + total_num
   return total_num


   