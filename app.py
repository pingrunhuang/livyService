from constants import TestTableSchema
import batchUtils
import flask

def modifyType():
    schema = TestTableSchema()
    args = ["modify", "jdbc:postgresql://52.80.50.148:5432/", "org.postgresql.Driver", "testdb", "test", schema.keys, schema.types]
    batchUtils.createBatch(args)

if __name__ == "__main__":
    modifyType()
