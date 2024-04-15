from database import client

def delete_index():

    print("Deleting employees index...")
    es = client.get_es_client()
    es.indices.delete(index='employees')
    
    print("Deleting companies index...")
    es = client.get_es_client()
    es.indices.delete(index='companies')

def delete_row():

    es = client.get_es_client()
    es.delete(index="employees", id="2500")

if __name__ == '__main__':
    delete_index()
    # delete_row()