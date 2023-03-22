# Introduction to Graph Databases

## What you will Learn

Explore Semantic data using Franz AllegroGraph DB (AGraph)

For the latest updates on this topic please download and view this PowerPoint deck
[Introduction to Graph databases](https://github.com/Grant-Steinfeld/semantic-db-agraph/blob/master/Intro_to_Graph_Databases-2023.v.3.0.0.pptx)

### Classification of Data - Ontologies

Data can be stored and classified in many ways. The columnar/row format is familiar, like spreadsheets or relational databases. Limitations here are that these are fixed formats that are `hard` to change and adapt to what happens in the natural world. Enter the idea of Sematic or Graph data. Datapoints are now Connected by relations. Like in a graph, we have vertices (points) and edges ( relationships ). Storing data in a graph is not only flexible, it also models real life events and represents reality as it IS.

Regard this attempt to classify Animals

> Borges’s Celestial Emporium of Benevolent Knowledge In his "The Analytical Language of John Wilkins," Jorge Luis Borges describes "a certain Chinese Encyclopedia," the Celestial Emporium of Benevolent Knowledge, in which it is written that animals are divided into:

1. those that belong to the Emperor
2. embalmed ones
3. those that are trained
4. suckling pigs
5. mermaids
6. fabulous ones
7. stray dogs
8. those included in the present classification
9. those that tremble as if they were mad
10. innumerable ones
11. those drawn with a very fine camelhair brush
12. others
13. those that have just broken a flower vase
14. those that from a long way off look like flies

Source: Jorge Luis Borges, Other Inquisitions: **_1937–1952_** (Austin: University of Texas Press, 2000), 101.

[Building Ontologies with Basic Formal Ontology p. 16
](https://mitpress.mit.edu/books/building-ontologies-basic-formal-ontology) - By [Robert Arp](https://mitpress.mit.edu/contributors/robert-arp), [Barry Smith](https://mitpress.mit.edu/contributors/barry-smith) and [Andrew D. Spear](https://mitpress.mit.edu/contributors/andrew-d-spear) MIT Press

The above can be taken with a grain a salt :)

However some serious applications of semanitc graph that interested me are:

Recommendations:

- Friend of a friend (FOAF e.g Social networks like LinkedIn and Facebook )
- Movie or Music

Research & Discovery

- Medical trends and attempts to share data amongst researchers
- Knowledge (e.g. IBM Watson - used Graph as a component to win Jeopardy)
- Facts (e.g. Wikipedia is backed by Mediawiki.org and Commons.Wikimedia.org )
- Reuters ( PermID.org - Connecting Linked Data to the World )

Recognitions of:

- Fraud
- Money Laundering
- Human trafficking

## Semantic Datastores

There are few in existence, a very good solid triple store we use to demonstrate semantic data is `AllegroGraph`

AllegroGraph is:

> Industry Leading Graph Database for Knowledge Graph Solutions and Common Lisp Technologies

> Franz Inc. is an early innovator in Artificial Intelligence and leading supplier of Semantic Graph Database technology with expert knowledge in developing and deploying Knowledge Graph solutions.

> AllegroGraph is an ultra scalable, high-performance, and transactional Semantic Graph Database which turns complex data into actionable business insights.

> Has a full featured free edition with `5 million triple` limit, which is plenty to get started, evaluate and have fun with it!

[Download options AGraph](https://franz.com/agraph/downloads/)
Not only can you install AGraph on Linux, but also in Docker or Virtual Machine optons are availible as well.

### Workshop Lab Notes

#### Step 1. Query data

> e.g. DBPedia - discover movies where actress `Shailene Woodley` acted in.

```sql
SELECT ?movie ?title ?name
WHERE {
  ?movie dbpedia-owl:starring [ rdfs:label "Shailene Woodley"@en ];
         rdfs:label ?title;
         dbpedia-owl:director [ rdfs:label ?name ].
  FILTER LANGMATCHES(LANG(?title), "EN")
  FILTER LANGMATCHES(LANG(?name),  "EN")
}
```

Try out a real-time SPARQL query in your browser right now:
Try this [DBPedia - hyperlink](https://bit.ly/39eQd1q), then click on the `Execute query` button:

### 2. Run Python3 queries to targeted RedHat Linux AGraph server

```sh
python3 Query.py
```

Lets explore how we can link UNESCO heritage sites with Geographic / Regional data in service of potential destination travel
options targeted for enthusiasts who want a vacation itenerary that highlights Ancient and Modern wonders of the world!

take a look a the [main program entry point ](https://github.com/Grant-Steinfeld/semantic-db-agraph/blob/master/query.py#L632)

```python

""" example calls to add continent node linked with city-country linked with UNESCO heritage site with year posted """
    addDestination(MAIN_TARGET_REPO,'North Africa','St Floris','Manovo-Gounda St Floris National Park', 1997)
    addDestination(MAIN_TARGET_REPO,'Southern Africa','Nelspruit, South Africa','Kruger National Park', 2019)
    addDestination(MAIN_TARGET_REPO,'Europe','Paris France','Eifell Tower', 2005)
    addDestination(MAIN_TARGET_REPO,'Europe','Vienna Austria','Historic Centre of Vienna', 2017)
    addDestination(MAIN_TARGET_REPO,'South America','Bolivia','City of Potosi', 2014)
    addDestination(MAIN_TARGET_REPO,'Central America','Tulum Mexico','Mayan Ruins of Tulum', 2001)
    addDestination(MAIN_TARGET_REPO,'Central America','Cancun Mexico','Chichen Itza', 1985)
    addDestination(MAIN_TARGET_REPO,'Central America','Cancun Mexico','Xichen', 1977)
    addDestination(MAIN_TARGET_REPO,'Central America','Lake Peten Itza Guatemala','Tikal', 1977)
```

and regard the [addDestination Function](https://github.com/Grant-Steinfeld/semantic-db-agraph/blob/master/query.py#L397-L429)

### requirements

python3

pip3

AllegroGraph instance / [docker version](https://franz.com/agraph/docker/)

### setup Agraph Client in Python

We recomment a python virtual environment. Venv.

```sh
pip3 install -r requirements.txt
```

#### Resources

[Programming the Semantic Web: Build Flexible Applications with Graph Data](http://shop.oreilly.com/product/9780596153823.do) by Segaran, Toby ; Evans, Colin ; Taylor, Jamie. O'Reilly Media.

[Semantic Graph Technologies and download AllegroGraph DB](https://franz.com/)

### Dataset Sources: RDF / triple / linked data

[World Heritage Sites](http://live.dbpedia.org/ontology/WorldHeritageSite)

[DBPedia datasets](https://wiki.dbpedia.org/develop/datasets)

https://www.w3.org/wiki/DataSetRDFDumps

https://query.wikidata.org/

[N-TRIPLES spec](http://www.w3.org/TR/rdf-testcases/#ntriples)

[Entities Wikimedia](https://dumps.wikimedia.org/wikidatawiki/entities/)

### Query options

#### SPARQL

Comunica: a Modular SPARQL Query Engine for the Web
https://comunica.github.io/Article-ISWC2018-Resource/

#### query by S P O

http://fragments.dbpedia.org/2016-04/en?subject=http%3A%2F%2Fdbpedia.org%2Fontology%2FWorldHeritageSite&predicate=&object=

2016

### IBM Watson and Linked Data

http://iswc2011.semanticweb.org/tutorials/semantic-web-technology-in-watson/index.html

### Other links

https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual

[Semantic natural language understanding with Spark Streaming, UIMA, and machine-learned ontologies](https://conferences.oreilly.com/strata/strata-ny-2016/public/schedule/detail/51498) - Strata+Hadoop World conference (2016)

[Semantic natural language understanding with Spark, UIMA & machine-learned ontologies ](https://bit.ly/39i9PBZ) - Powerpoint slide deck - by David Talby and Claudiu Branzan
