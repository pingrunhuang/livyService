from requests import get, post, delete
import requests
from constants import LIVY_SERVER, BATCH_PAYLOAD
import json

def getBatches(start_index, num_of_sessions):
    """
    Returns all the active batch sessions
    """
    url     = "{}/batches".format(LIVY_SERVER)
    payload = {"from":start_index, "size":num_of_sessions}
    result  = post(url, json=payload)
    if result.ok:
        print(result.text)
    else:
        print(result.status_code)

def createBatch(args):
    """
    Run a batch process
    """
    BATCH_PAYLOAD["args"]=args
    url = "{}/batches".format(LIVY_SERVER)
    print(url)
    print(BATCH_PAYLOAD)
    result = post(url, json=BATCH_PAYLOAD)
    print(result)
    print(result.url)
    if result.ok:
        print("Successfully created a batch")
        print(result.text)
    else:
        print("failed")
        print(result.status_code)
    
def getBatch(batchId):
    """
    Return batch session info
    """
    url     = "{}/batches/{}".format(LIVY_SERVER, batchId)
    result  = get(url)
    if result.ok:
        print(result.text)
    
def killBatch(batchId):
    """
    kills the batch job
    """
    url     = "{}/batches/{}".format(LIVY_SERVER, batchId)
    result  = delete(url)
    if result.ok:
        print("Batch {} deleted".format(batchId))


def getBatchLog(batchId, offset, lines):
    """
    Gets the log lines from this batch.
    @param Offset int
    @param lines Max number of log lines to return	int
    """
    url = "{}/batches/{}/log".format(LIVY_SERVER, batchId)
    params = {"from":offset, "size":lines}
    result  = get(url, params=params)
    if result.ok:
        print(result.text)

