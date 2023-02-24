import pandas as pd
import numpy as np
import file_handler as fh


#creates inititial dataframe for wiki pages

def create_main_df():
   #data = [None, None, None]
   main_df_csv = pd.DataFrame( columns=["page", "section_num", "word_num"])
   fh.write_csv_main(main_df_csv)
   return main_df_csv

#def save_csv_file(data_df):
  # data_df.to_csv("E:\python_projects\wiki_data_collect\data\\)" + "main_csv_file.csv")
   

def count_words(page_text):
   word_list = ""
   for word in range(0, len(page_text)):
      word_list = str(page_text[word]) + word_list
   word_count = word_list.count(" ")
   return word_count
   
     
def count_sections(wiki_page_text):
   section_total = 0
   section_num_list = []
  
   for text in wiki_page_text:
      temp_text = str.lower(text)
      temp_num = temp_text.count("/n/n")
      section_num_list.append(temp_num)
      temp_num = 0
   section_total = np.sum(section_num_list)
   
   
   return section_total


def update_main_csv(df, page_name, section_num, word_num):
   #data = { "page": page_name, "section_num": section_num, "word_num": word_num }
   new_page = [page_name, section_num, word_num]
   main_df = fh.get_csv_main()
   main_df.loc[len(main_df.index)] = new_page
   fh.write_csv_main(main_df)


def drop_row(df, row_to_drop):
   
   new_df= pd.DataFrame.drop(df,index = [row_to_drop])
   return new_df
   
def count_key_word(page_text, key_word):
   word_list = ""
   for word in range(0, len(page_text)):
      word_list = str(page_text[word]) + word_list
   word_count = word_list.count(key_word)
   return word_count

def add_key_result(page_name, key_word, key_result):
   df = fh.get_csv_main()
   counter = 0
   for i in range(0,df[len(df)-1]):
      if df[i][0]  == page_name:
         row_num = i
   pd.DataFrame.insert(df,row_num, key_word, key_result, allow_duplicates=False)
   fh.write_csv_main(df)
   return(df)