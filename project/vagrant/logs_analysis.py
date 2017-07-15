#! /usr/bin/env python2.7

import psycopg2

DBNAME = "news"


def get_most_popular_articles():
    """Returns top 3 popular articles of all time, with most popular
       being on top."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select a.title, count(*) " +
              "from log l, articles a " +
              "where l.path like concat('%', a.slug) " +
              "group by a.title " +
              "order by count(*) desc limit 3;")
    result = c.fetchall()
    db.close()

    return result


def get_most_popular_authors():
    """Returns authors sorted by popularity, with most popular being on top."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select au.name, count(*) "
              "from log l, articles a, authors au " +
              "where au.id = a.author and l.path like concat('%', a.slug) " +
              "group by au.name " +
              "order by count(*) desc;")
    result = c.fetchall()
    db.close()

    return result


def get_days_with_high_error_rates():
    """Returns days on which users experienced more than 1% error rates."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select al.date, ROUND((el.count::decimal/al.count) * 100, 1) " +
              "as percent_errors " +
              "from aggregated_all_logs al, aggregated_error_logs el " +
              "where al.date = el.date " +
              "and ROUND((el.count::decimal/al.count) * 100, 1) > 1;")
    result = c.fetchall()
    db.close()

    return result

print "1. What are the most popular three articles of all time?"
for element in get_most_popular_articles():
    print "   " + element[0] + " -- " + str(element[1]) + " views"

print

print "2. Who are the most popular article authors of all time?"
for element in get_most_popular_authors():
    print "   " + element[0] + " -- " + str(element[1]) + " views"

print

print "3. On which days did more than 1% of requests lead to errors?"
for element in get_days_with_high_error_rates():
    print ("   " + element[0].strftime("%B %d, %Y") + " -- " +
           str(element[1]) + "% errors")
