JAR_PATH        = "/home/bdata/monk/monk.jar"
CLASSNAME       = "App"
APPNAME         = "frank-monk"
DRIVER_CORES    = 6
DRIVER_MEMORY   = "2g"
EXECUTOR_CORES  = 6
EXECUTOR_MEMORY = "4g"
PROXY_USER      = "bdata"
NUM_EXECUTORS   = 6




SQL_DRIVER      = "org.postgresql.Driver"
SQL_URL         = "jdbc:postgresql://52.80.50.148:5432/"

LIVY_SERVER     = "http://52.80.50.148:8998"

"""
@param    file      File containing the application to execute	path (required)
@param    proxyUser User to impersonate when running the job
@param    className Application Java/Spark main class
@param    args      Command line arguments for the application
@param    jars      jars to be used in this session	list of strings
@param    pyFiles	Python files to be used in this session	list of strings
@param    files     files to be used in this session	list of strings
@param    driverMemory	    Amount of memory to use for the driver process	string
@param    driverCores	    Number of cores to use for the driver process	int
@param    executorMemory	Amount of memory to use per executor process	string
@param    executorCores	    Number of cores to use for each executor	int
@param    numExecutors	    Number of executors to launch for this session	int
@param    archives	        Archives to be used in this session	List of string
@param    queue	            The name of the YARN queue to which submitted	string
@param    name	            The name of this session	string
@param    conf	            Spark configuration properties	Map of key=val
"""
BATCH_PAYLOAD={
    "file":JAR_PATH,
    "proxyUser":PROXY_USER,
    "className":CLASSNAME,
    "name":APPNAME,
    "driverCores":DRIVER_CORES,
    "driverMemory":DRIVER_MEMORY,
    "executorCores":EXECUTOR_CORES,
    "executorMemory":EXECUTOR_MEMORY,
    "numExecutors":NUM_EXECUTORS,
    "conf": {
        "spark.executor.cores":2, 
        "spark.cores.max":4
    },
    "args":[]
}



"""
@param kind	The session kind[1]	session kind
@param proxyUser	User to impersonate when starting the session	string
@param jars	jars to be used in this session	List of string
@param pyFiles	Python files to be used in this session	List of string
@param files	files to be used in this session	List of string
@param driverMemory	Amount of memory to use for the driver process	string
@param driverCores	Number of cores to use for the driver process	int
@param executorMemory	Amount of memory to use per executor process	string
@param executorCores	Number of cores to use for each executor	int
@param numExecutors	Number of executors to launch for this session	int
@param archives	Archives to be used in this session	List of string
@param queue	The name of the YARN queue to which submitted	string
@param name	The name of this session	string
@param conf	Spark configuration properties	Map of key=val
@param heartbeatTimeoutInSecond	Timeout in second to which session be orphaned	int
"""
SESSION_PAYLOAD={
    "kind":"spark",
    "proxyUser":PROXY_USER,
    "className":CLASSNAME,
    "name":APPNAME,
    "driverCores":DRIVER_CORES,
    "driverMemory":DRIVER_MEMORY,
    "executorCores":EXECUTOR_CORES,
    "executorMemory":EXECUTOR_MEMORY,
    "numExecutors":NUM_EXECUTORS
}


class TestTableSchema:
    def __init__(self):
        self.keys = "position_time,speed,direction,position_mode,position_mode_desc,alarm_props,status_props,longitude,latitude,altitude,device_id"
        self.types= "string,string,double,integer,string,string,string,double,double,integer,string" 