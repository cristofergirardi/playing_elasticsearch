from database import client

es = client.get_es_client()

def add_row():
    documents = [
      { "index": { "_index": "employees"}},
      {"name": "Test name", "email" : "teste_1@gmail", "address" : "Address test", "age" : "40", "phone" : "+55 (83) 23456789", "phrase" : "Hello, I am new here!"}
    ]

    es.bulk(operations=documents)


if __name__ == '__main__': 
    add_row()