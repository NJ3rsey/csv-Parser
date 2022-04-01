#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql


def sql():
    try:
        connection = pymysql.connect(host='localhost',
                                     database='test',
                                     user='root',
                                     password='1qaz2wsx')

        q = """ SELECT * FROM one """

        cursor = connection.cursor()
        cursor.execute(q)
        connection.commit()

        rec = cursor.fetchall()
        for row in rec:
            print("number: ", row[0])

        cursor.close()

    except pymysql.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))

    finally:
        connection.close()
        print("MySQL connection is closed")


sql()
