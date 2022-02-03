
from lib2to3.pgen2 import driver


def run_cypher(cq,limit=10):
    tran = lambda tx: tx.run(cq,limit=limit).data()
    global driver
    global neo_database
    with driver.session(database=neo_database) as session:
        results = session.write_transaction(tran)
    return results

def reset_db():
    cq = "match (n) detach delete n"
    return run_cypher(cq)

def get_stats():
    cq = """
    call apoc.meta.stats() yield labelCount, relTypeCount, propertyKeyCount, nodeCount, relCount
    with labelCount, relTypeCount, propertyKeyCount, nodeCount, relCount
    return labelCount, relTypeCount,propertyKeyCount, nodeCount,relCount
    """
    res = run_cypher(cq)
    for rec in res:
        print (rec)

def checksum():
    cq = """
    call apoc.meta.stats() yield labelCount, relTypeCount, propertyKeyCount, nodeCount, relCount
    with labelCount, relTypeCount, propertyKeyCount, nodeCount, relCount
    return labelCount+relTypeCount+propertyKeyCount+nodeCount+relCount as checksum
    """
    res = run_cypher(cq)
    return res[0]['checksum']

def nodeCount():
    cq = """
    match (n) return count(n) as count
    """
    res = run_cypher(cq)
    return res[0]['count']

from pprint import pprint
def get_stats_all():
    cq = """
        call apoc.meta.stats()
        """
    res = run_cypher(cq)
    pprint(res[0]['stats'])

def schema_view():
    cq = "CALL db.schema.visualization()"
    print ("Run {} in Neo4j Browser to see a graphical view".format(cq))
    res  = run_cypher(cq)
    pprint(res)

def print_label_count():
    result = {"Label": [], "Count": []}
    for label in graph.run("CALL db.labels()").to_series():
        query = f"MATCH (:`{label}`) RETURN count(*) AS count"
        count = graph.run(query).to_data_frame().iloc[0]['count']
        result["Label"].append(label)
        result["Count"].append(count)
    nodes_df = pd.DataFrame(data=result)
    return nodes_df

