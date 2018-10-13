#!/usr/bin/env python3

import psycopg2


# Connect to database and create cursor
def dbcontext():
    # print("Connecting to database...")
    try:
        db = psycopg2.connect("dbname=news")
        cursor = db.cursor()

        # print("Established connection")
        return cursor, db
    except Exception as e:
        print("An error occurred connecting to the database. {0}", e)
        quit()


# 1. What are the most popular three articles of all time?
def top_three_articles():
    print("What are the most popular three articles of all time?")

    cursor, db = dbcontext()

    cursor.execute("""
    SELECT title, COUNT(*) as searches
    FROM articles
    JOIN log ON log.path LIKE '/article/%' || articles.slug
    GROUP BY articles.title
    ORDER BY searches desc
    LIMIT 3;
    """)
    results = cursor.fetchall()
    db.close()

    print(''.join(["{0} - {1} views\n".format(result[0], result[1])
                   for result in results]))
    print("___\n")


# 2. Who are the most popular article authors of all time?
def top_authors():
    print("Who are the most popular article authors of all time?")

    cursor, db = dbcontext()

    cursor.execute("""
    SELECT authors.name, COUNT(*) as searches
    FROM authors
    JOIN articles
      ON authors.id = articles.author
    JOIN log
      ON log.path LIKE '/article/' || articles.slug
    GROUP BY authors.name
    ORDER BY searches desc;
    """)
    results = cursor.fetchall()
    db.close()

    print(''.join(["{0} - {1} views\n".format(result[0], result[1])
                   for result in results]))
    print("___\n")


# 3. On which days did more than 1% of requests lead to errors?
def percent_of_reqs_to_errors():
    print("On which days did more than 1% of requests lead to errors?")

    cursor, db = dbcontext()

    cursor.execute("""
    WITH request_total AS (
        SELECT time::date AS day, COUNT(*)
        FROM log
        GROUP BY time::date
        ORDER BY time::date
    ), error_total AS (
        SELECT time::date AS day, COUNT(*)
        FROM log where status != '200 OK'
        GROUP BY time::date
        ORDER BY time::date
    ), error_rate AS (
        SELECT request_total.day,
        error_total.count::float / request_total.count::float * 100
            AS error_percentage
        FROM request_total, error_total
        WHERE request_total.day = error_total.day
    )
    SELECT * FROM error_rate WHERE error_percentage > 1;
    """)
    results = cursor.fetchall()
    db.close

    print(''.join(["{0} - {1} errors\n".format(result[0], result[1])
                   for result in results]))
    print("___\n")


if __name__ == '__main__':
    print("\nGenerating report...\n")
    print("___\n")

    top_three_articles()
    top_authors()
    percent_of_reqs_to_errors()
