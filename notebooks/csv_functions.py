import pandas as pd


#creates inititial dataframe for wiki pages

def create_main_df():
   data = {"page": [], "section_num": [], "word_num": []}
   main_df_csv = pd.DataFrame(data)
   return main_df_csv

def save_csv_filie(data_df):
   data_df.to_csv("E:\python_projects\wiki_data_collect\data\\)" + "main_csv_file.csv")
   
   