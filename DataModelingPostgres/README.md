Purposes:
"The analytics team is particularly interested in understanding what songs users are listening to." (c)

So, the main goal is to understand what songs users are listening to. That is why we made the song play table. Here it is possible to find the information about songs played by users without requests to other tables. What the song, when played, at which user and user account level (paid/free) and etc.

The side purpose of the DB is to save the data structured and minimize used space. So we can add other tables for analytics easily later.

Running Python Scripts:
1. > python create_tables.py
2. > python etl.py

Repository:
- the folder 'data' include 'sond_data' and 'log_data'. The data, which we've got from the Sparkify team.
- 'create_tables.py' is a python script for creating DB.
- 'etl.ipynb' is a notebook used to check and visualize the parts of the code. Only for development.
- 'etl.py' is a python script to process the data to the DB.
- 'test.ipynb' is a notebook to test the DB.