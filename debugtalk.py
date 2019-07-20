
import time

def sleep(n_secs):
    time.sleep(n_secs)

def get_timestamp():
    return str(int(time.time() * 1000))

def print_documentId(doc_id):
    print("documentId = {}".format(doc_id))
