from elasticsearch import Elasticsearch
from common.user import User

def get_es_client():
    host = "https://localhost:9200"

    user = User()

    # client = Elasticsearch([host], http_auth=(user, password), verify_certs=False)
    client = client = Elasticsearch([host],
                                    ca_certs="./files/http_ca.crt",
                                    basic_auth=(user.get_user(), user.get_password())
                                  )
    return client

    # API key should have cluster monitor rights
    # print(client.info())

    # documents = [
    #   { "index": { "_index": "index_name", "_id": "9780553351927"}},
    #   {"name": "Snow Crash", "author": "Neal Stephenson", "release_date": "1992-06-01", "page_count": 470},
    #   { "index": { "_index": "index_name", "_id": "9780441017225"}},
    #   {"name": "Revelation Space", "author": "Alastair Reynolds", "release_date": "2000-03-15", "page_count": 585},
    #   { "index": { "_index": "index_name", "_id": "9780451524935"}},
    #   {"name": "1984", "author": "George Orwell", "release_date": "1985-06-01", "page_count": 328},
    #   { "index": { "_index": "index_name", "_id": "9781451673319"}},
    #   {"name": "Fahrenheit 451", "author": "Ray Bradbury", "release_date": "1953-10-15", "page_count": 227},
    #   { "index": { "_index": "index_name", "_id": "9780060850524"}},
    #   {"name": "Brave New World", "author": "Aldous Huxley", "release_date": "1932-06-01", "page_count": 268},
    #   { "index": { "_index": "index_name", "_id": "9780385490818"}},
    #   {"name": "The Handmaid's Tale", "author": "Margaret Atwood", "release_date": "1985-06-01", "page_count": 311},
    # ]

    # client.bulk(operations=documents)

    # print(client.search(index="index_name", q="snow"))

    # resp = client.indices.delete(index="index_name")
    # print(resp)
