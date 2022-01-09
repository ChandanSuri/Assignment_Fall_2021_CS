import py2neo
import pandas as pd


_graph = None

_neo4j_connect_info = {
    "user": None,
    "password": None
}


def set_neo4j_connect_info(user, password):

    global _neo4j_connect_info

    _neo4j_connect_info["user"] = user
    _neo4j_connect_info["password"] = password


def get_graph():

    global _graph

    if _graph is None:

        _graph = py2neo.Graph("bolt://localhost:7687",
                              auth = (_neo4j_connect_info["user"], _neo4j_connect_info["password"]))

    return _graph


def get_people_in_matrix():

    q = "match (n)-[:ACTED_IN]->(m) where m.title=\"The Matrix\" return n"
    the_g = get_graph()
    the_res = the_g.run(q)

    result =[]

    for r in the_res:
        t = dict(r)
        t = dict(t["n"])
        result.append(t)

    result = pd.DataFrame(result)
    return result


if __name__ == "__main__":

    set_neo4j_connect_info("neo4j", "dbuserdbuser")
    g = get_graph()

    res = get_people_in_matrix()
    print("Result = ", res)
