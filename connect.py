import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

engine = create_engine('mysql+mysqlconnector://admin:c12888d88c@parlay-scraped-1.cye7mkifplef.us-east-2.rds.amazonaws.com:3306/Test', echo=False)

df = pd.DataFrame(np.random.randint(0,10,size=(1, 4)), columns=list('ABCD'))
df.to_sql(name='random', con=engine, if_exists = 'append', index=False)

