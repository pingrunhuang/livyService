from constants import LIVY_SERVER
from requests import get, post

def getStatements(sessionId):
    """
    returns all the statements in a session
    """
    url     = "{}/sessions/{}/statements".format(LIVY_SERVER, sessionId)
    result  = get(url)
    if result.ok:
        print(result.text)

def runStatement(sessionId, code="", kind="spark"):
    """
    return statement in a session
    @param code the code to execute
    @param kind the kind of code to execute: spark, pyspark, sparkr, sql
    """
    url     = "{}/sessions/{}/statements".format(LIVY_SERVER, sessionId)
    payload = {"code":code, "kind":kind}
    result  = post(url, data=payload)
    if result.ok:
        print(result.text)

def getStatement(sessionId, statementId):
    """
    return specified statement ins 
    """
    url     = "{}/sessions/{}/statements/{}".format(LIVY_SERVER, sessionId, statementId)
    result  = get(url)
    if result.ok:
        print(result.text)


def cancelStatement(sessionId, statementId):
    """
    Cancel the specified statement in this session
    """
    url     = "{}/sessions/{}/statements/{}/cancel".format(LIVY_SERVER, sessionId, statementId)
    result  = post(url)
    if result.ok:
        print(result.text)



if __name__ == "__main__":
    pass