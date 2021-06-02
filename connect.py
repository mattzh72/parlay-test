import mysql.connector
import sqlalchemy as db
import pandas as pd
import numpy as np

engine = db.create_engine('mysql+mysqlconnector://admin:c12888d88c@parlay-scraped-1.cye7mkifplef.us-east-2.rds.amazonaws.com:3306/Test', echo=False)

# Example for writing data in
# df = pd.DataFrame(np.random.randint(0,10,size=(1, 4)), columns=list('ABCD'))
# df.to_sql(name='random', con=engine, if_exists = 'append', index=False)

connection = engine.connect()
metadata = db.MetaData()
random = db.Table('random', metadata, autoload=True, autoload_with=engine)
query = db.select([random])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet[:3])


