from requests import post, get
from constants import LIVY_SERVER


def getSessions(f=0, size=100):
    """Returns all the active interactive sessions.
    @param f    The start index to fetch sessions
    @param size Number of sessions to fetch
    """
    url = "{}/sessions".format(LIVY_SERVER)
    # default parameters value
    payload = {"from":f,"size":size}
    result = get(url, params=payload)
    if result.ok:
        print(result.text)



def postSessions(kind="spark"):
    pass

def getSession(sessionId):
    """
    Returns the session information.
    @para sessionId the session id
    TODO: modify to use a session for connection in order to check if it is finished
    """
    url = "{}/sessions/{}/state".format(LIVY_SERVER, sessionId)
    result = get(url)
    if result.ok:
        print(result.text)

def getSessionLog(sessionId):
    """
    kills a session
    """
    url = "{}/sessions/{}/log".format(LIVY_SERVER, sessionId)
    result = get(url)
    if result.ok:
        print(result.text)

def deleteSession(sessionId):
    """
    gets the log lines from the session
    """
    url = "{}/sessions/{}".format(LIVY_SERVER, sessionId)
    result = get(url)
    if result.ok:
        print("Session {} deleted".format(sessionId))


if __name__=="__main__":
    getSessions()
