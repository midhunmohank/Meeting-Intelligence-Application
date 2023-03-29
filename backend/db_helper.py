import snowflake.connector


# Function to establish connection with snowflake
def create_connection():
    conn = snowflake.connector.connect(
        user='CHATGPT',
        password='Breakingbad@1',
        account='pigjtsl-ed61481',
        warehouse='COMPUTE_WH',
        database='INTEL',
        schema='PUBLIC'
    )
    return conn


def processed_files():
    
    conn = create_connection()
    cursor = conn.cursor()

    # Execute the SQL query
    cursor.execute("SELECT AUDIO_FILE FROM QUERY_RESULTS")

    # Fetch all the results into a list
    results = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    return [result[0] for result in results]


def processed_files():
    
    conn = create_connection()
    cursor = conn.cursor()

    # Execute the SQL query
    cursor.execute("SELECT AUDIO_FILE FROM QUERY_RESULTS")

    # Fetch all the results into a list
    results = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    return [result[0] for result in results]


# print(processed_files())

def processed_query(file, query):
    
    conn = create_connection()
    cursor = conn.cursor()

    # Execute the SQL query
    cursor.execute(f"SELECT {query} FROM QUERY_RESULTS WHERE FILE = {file}")

    # Fetch all the results into a list
    results = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    return results 


processed_query("1680036452.mp3", "SUMMARY")