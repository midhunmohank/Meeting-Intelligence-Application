import os
import json
import openai
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models.param import Param
from datetime import timedelta, datetime
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import gpt_helper as gpt 



# print(gpt.generate_txt_file("goes-team6", "test-rec.mp3"))




# openai.api_key = "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"
# def create_connection():
#     conn = snowflake.connector.connect(
#         user='SANJAYKASHYAP',
#         password='Bigdata@23',
#         account='iogoldm-vcb38713',
#         warehouse='COMPUTE_WH',
#         database='INTEL_MEETING',
#         schema='PUBLIC'
#     )
#     return conn


# # test_dict = {'message':'dummy', 'response':'also_dummy'}
# # jsonn = json.dumps(test_dict)
# # jsonn = jsonn.replace("'", "\"")
# # print(jsonn)
# # query = f'''INSERT INTO QUERY_RESULTS SELECT PARSE_JSON('{jsonn}')'''
# # conn = create_connection()
# # cur = conn.cursor()
# # cur.execute(query)


# def send_query(message):
    
#     response =  openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo", 
#         messages = [
#             {"role" : "user", "content" : message}
#         ]
#     )
#     print(response)
#     response["choices"][0]["message"]["content"] = response["choices"][0]["message"]["content"].replace("\n", "\\n")
#     response["choices"][0]["message"]["content"] = response["choices"][0]["message"]["content"].replace("'", "sq")
#     response["choices"][0]["message"]["content"] = response["choices"][0]["message"]["content"].replace(",", "comm")
#     print(response)
    
#     my_json = json.dumps(response)
#     #my_json = my_json.replace("'", "\"")
#     print(my_json)
#     query = f"INSERT INTO QUERY_RESULTS SELECT '{message}', PARSE_JSON('{my_json}'), CURRENT_TIMESTAMP"
#     conn = create_connection()
#     cur = conn.cursor()
    
#     cur.execute(query)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return response

# print(send_query('wRITE A RAP SONG'))


# def send_query(message):
    
#     response =  openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo", 
#         messages = [
#             {"role" : "user", "content" : message}
#         ]
#     )
    
#     response =  openai.ChatCompletion.create(
#     model = "gpt-3.5-turbo", 
#     messages = [
#            {"role" : "user", "content" : message}
#         ]  
#     )
    
#     response["choices"][0]["message"]["content"] = response["choices"][0]["message"]["content"].replace("\n", "\\n")
#     response["choices"][0]["message"]["content"] = response["choices"][0]["message"]["content"].replace("'", "sq")
#     response["choices"][0]["message"]["content"] = response["choices"][0]["message"]["content"].replace(",", "comm")
#     my_json = json.dumps(response)
#     query = f"INSERT INTO QUERY_RESULTS SELECT {message}, PARSE_JSON('{my_json}'), CURRENT_TIMESTAMP'"
#     conn = create_connection()
#     cur = conn.cursor()
    
#     cur.execute(query)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return response



