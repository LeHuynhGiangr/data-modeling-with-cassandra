import functools

def build_create_keyspace_cql(keyspace_name='', replication_factor = 1, strategy = "SimpleStrategy"):
    ret = (
        """
        CREATE KEYSPACE IF NOT EXISTS %s
            WITH REPLICATION = { 'class' : %s, 'replication_factor' : %s }
        """
        %(keyspace_name, strategy, replication_factor)
        )

    print(ret)
    return ret

def build_create_table_cql(table_name, columns = [], primary_key = ""):
    ret = """
        CREATE TABLE IF NOT EXISTS %s (%s, primary key(%s))
    """%(table_name, ", ".join(columns), primary_key)
    print(ret)
    return ret
    
def t():
    print("test")