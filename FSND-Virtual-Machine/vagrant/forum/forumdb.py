# "Database code" for the DB Forum.

import datetime
import psycopg2

POSTS = [("This is the first post.", datetime.datetime.now())]

def get_connection():
  return psycopg2.connect("dbname=forum")

def get_posts():
  """Return all posts from the 'database', most recent first."""
  conn = get_connection()
  cur  = conn.cursor()
  cur.execute("SELECT content, time from posts order by time desc")
  posts = cur.fetchall()
  conn.close()

  return posts

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  conn = get_connection()
  cur  = conn.cursor()
  cur.execute("INSERT INTO posts (content, time) VALUES (%s, %s)", (content, datetime.datetime.now()))
  conn.commit()
  conn.close()
