import mysql.connector
import sys
import boto3
import os

ENDPOINT="parlay-scraped-1.cye7mkifplef.us-east-2.rds.amazonaws.com"
PORT="3306"
USR="admin"
REGION="us-east-2c"
DBNAME="parlay-scraped-1"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
session = boto3.Session(profile_name='default')
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USR, Region=REGION)

try:
    conn =  mysql.connector.connect(host=ENDPOINT, user=USR, passwd=token, port=PORT, database=DBNAME)
    print("Database connection success.")
except Exception as e:
    print("Database connection failed due to {}".format(e))       