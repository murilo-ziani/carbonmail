# Operações Gerais do Banco de Dados.

import sqlite3

def create(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print('Ops... Deu erro criando uma tabela do banco de dados:', error)

def insert(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    except sqlite3.Error as error:
        print('Ops... Deu erro inserindo um dado:', error)

def delete(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    except sqlite3.Error as error:
        print('Ops... Deu erro deletando um dado:', error)

def select(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    except sqlite3.Error as error:
        print('Ops... Deu erro buscando um dado:', error)
    finally:
        return result