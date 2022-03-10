# neo4j-lib

This Python module makes it easy to run Neo4j [Cypher](https://neo4j.com/developer/cypher/) queries in a [Jupyter](https://jupyter.org/) Notebook, which is ideal for students learning the Cypher query language.

**Index**

- [Usage](#usage)
- [Example](#example)
- [License](#license)

---

## Usage

This `neo4j_lib` module is a thin wrapper for the [py2neo](https://pypi.org/project/py2neo/) and [neo4j-driver](https://pypi.org/project/neo4j-driver/) packages. It enables you to write Cypher queries in a Jupyter notebook, which provides many advantages, such as:

- Experimenting with different query variations.
- Saving your work.
- Sharing your work.
- A teacher preparing a workbook with examples and exercises.

The following table suggests when Python developers might want to use the various alternatives for connecting to a [Neo4j](https://neo4j.com/) database.

| Scenario                                                                                                                                       | API to use                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| You want to experiment with Cypher queries and you do not care about saving your work.                                                         | [Neo4j Browser](https://neo4j.com/docs/browser-manual/current/) |
| You are learning the Cypher language _and_ you want to use a Jupyter notebook, so that you can save your work and share your work with others. | [neo4j_lib](./)                                                 |
| You are teaching people to use Cypher, so you want to give instructions and prepare partially completed exercises.                             | [neo4j_lib](./)                                                 |
| You want a Python API for programmatic access to a Neo4j database from your Python code.                                                       | [py2neo](https://pypi.org/project/py2neo/)                      |

## Example

See the [01_EKG_MOV_Database.ipynb](./01_EKG_MOV_Database.ipynb) Jupyter notebook for an example of how to use this module. The essential set-up is:

```python
# Install dependencies
!pip install -qq neo4j-driver
!pip install -qq py2neo pandas

# Install the latest version of the neo4j_lib module.
!rm -rf neo_lib.py
!wget -qq https://raw.githubusercontent.com/tadinve/neo4j-lib/master/neo_lib.py -O neo_lib.py

# Import
from neo_lib import Neo_lib

# Run a Cyper query, returning the results in a Pandas DataFrame.
cq = """
MATCH (c:Person)-[r:REVIEWED]->(m:Movie)<-[:ACTED_IN]-(a:Person)
RETURN
  c.name as reviewer,
  m.title as title,
  m.released as date,
  r.rating as rating,
  collect(a.name) as actors
ORDER BY date DESC, title, rating DESC
"""
df = nl.run_cypher_pd(cq)
df
```

## License

Copyright &#169; 2022 [Venkatesh Tadinada](venkat@solivar.com)

Licensed under the [Apache License, Version 2.0](./LICENSE) (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the [License](./LICENSE) for the specific language governing permissions and limitations under the License.
