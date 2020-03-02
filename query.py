from franz.openrdf.sail.allegrographserver import AllegroGraphServer
from franz.openrdf.repository.repository import Repository
from franz.openrdf.query.query import QueryLanguage
from franz.openrdf.vocabulary.xmlschema import XMLSchema
from franz.openrdf.rio.rdfformat import RDFFormat
import os

CURRENT_DIRECTORY = os.getcwd() 

AG_HOST = os.environ.get('AGRAPH_HOST')
AG_PORT = int(os.environ.get('AGRAPH_PORT', '10035'))
AG_CATALOG = ''
MAIN_TARGET_REPO = 'destinations'
AG_USER = os.environ.get('AGRAPH_USER', 'student')
AG_PASSWORD = os.environ.get('AGRAPH_PWD')


def getConn(repo=MAIN_TARGET_REPO, accessMode=Repository.OPEN):

    server = AllegroGraphServer(AG_HOST, AG_PORT, AG_USER, AG_PASSWORD)
    catalog = server.openCatalog()
    myRepository = catalog.getRepository(repo, accessMode)
    myRepository.initialize()
    conn = myRepository.getConnection()
    return conn

def __getTypedLiteral(conn, namespace, subjectLocalName, predicateLocalName, objLiteral=None, datatype="STRING"):
    exns = "http://%s/" % namespace
    subject_ = conn.createURI(namespace=exns, localname=subjectLocalName)
    predicate_ = conn.createURI(namespace=exns, localname=predicateLocalName)

    object_ = None
    if(objLiteral!=None):
        object_ = conn.createLiteral(objLiteral,__getDatatype(datatype))

    return subject_, predicate_, object_

def __getUU(conn, namespace, subjectLocalName, predicateLocalName):
    exns = "http://%s/" % namespace
    subject_ = conn.createURI(namespace=exns, localname=subjectLocalName)
    predicate_ = conn.createURI(namespace=exns, localname=predicateLocalName)
    return subject_, predicate_

def __getLU(conn, namespace, subjectLocalName, predicateLocalName):
    exns = "http://%s/" % namespace
    subject_ = conn.createLiteral(subjectLocalName,__getDatatype("STRING"))
    predicate_ = conn.createURI(namespace=exns, localname=predicateLocalName)
    return subject_, predicate_

def __getLUL(conn, namespace, subjectLocalName, predicateLocalName,
             objLiteral=None, datatype="STRING"):
    exns = "http://%s/" % namespace
    subject_ = conn.createLiteral(subjectLocalName,__getDatatype("STRING"))
    predicate_ = conn.createURI(namespace=exns, localname=predicateLocalName)

    object_ = None
    if(objLiteral!=None):
        object_ = conn.createLiteral(objLiteral,__getDatatype(datatype))

    return subject_, predicate_, object_
def __getLUU(conn, namespace, subjectLocalName, predicateLocalName, objectLocalName):
    exns = "http://%s/" % namespace
    subject_ = conn.createLiteral(subjectLocalName,__getDatatype("STRING"))
    predicate_ = conn.createURI(namespace=exns, localname=predicateLocalName)
    object_ = conn.createURI(objectLocalName)

    return subject_, predicate_, object_

def __getUUU(conn, namespace, subjectLocalName, predicateLocalName, objectLocalName):
    exns = "http://%s/" % namespace
    subject_ = conn.createURI(namespace=exns, localname=subjectLocalName)
    predicate_ = conn.createURI(namespace=exns, localname=predicateLocalName)
    object_ = conn.createURI(namespace=exns, localname=objectLocalName)

    return subject_, predicate_, object_


def addTripleUUU(targetRepo, subjectURI, predicateURI, objectURI):
    conn = getConn(targetRepo)

    subject_ = conn.createURI(subjectURI)
    predicate_ = conn.createURI(predicateURI)
    object_ = conn.createURI(objectURI)

    beforeCount = conn.size()
    conn.add(subject_,predicate_,object_)
    afterCount = conn.size()

    return afterCount-beforeCount


def existsTripleUUnsTyped(targetRepo, namespace,
                   subjectLocalName,
                   predicateLocalName,conn=None):

        if conn==None:
            conn = getConn(targetRepo)

        subject_, predicate_,object_ = __getTypedLiteral(conn,namespace,
                                                 subjectLocalName,
                                                 predicateLocalName)

        statements = conn.getStatements(subject_,predicate_,object_)

        numStatements = len(statements.string_tuples)
        #statements.enableDuplicateFilter() ## there are no duplicates, but this exercises the code that checks

        counter = 0
        for s in statements:
            print( s )
            counter = counter + 1


        if counter != numStatements:
            msg = "Error counter [{}] and numstatements [{}] out of sync".format( counter, numStatements)
            raise Exception(msg)

        statements.close()
        conn.close()

        return numStatements

def existsTripleUULnsTyped(targetRepo, namespace,
                   subjectLocalName,
                   predicateLocalName,
                   objLiteral,conn=None, datatype="STRING"):

        if conn==None:
            conn = getConn(targetRepo)

        subject_, predicate_,object_ = __getTypedLiteral(conn,namespace,
                                                 subjectLocalName,
                                                 predicateLocalName,
                                                 objLiteral,datatype)

        statements = conn.getStatements(subject_,predicate_,object_)

        numStatements = len(statements.string_tuples)
        #statements.enableDuplicateFilter() ## there are no duplicates, but this exercises the code that checks

        counter = 0
        for s in statements:
            print( s )
            counter = counter + 1

        if counter != numStatements:
            msg = "Error counter [{}] and numstatements [{}] out of sync".format( counter, numStatements)
            raise Exception(msg)

        statements.close()
        conn.close()

        return numStatements


def getTripleUU(targetRepo, namespace,
                   subjectLiteral,
                   predicateLocalName):


        conn = getConn(targetRepo)

        subject_, predicate_ = __getUU(conn,
                                       namespace,
                                       subjectLiteral,
                                       predicateLocalName)

        statements = conn.getStatements(subject_,predicate_, None)

        numStatements = len(statements.string_tuples)

        counter = 0
        for s in statements:
            print( type(s) )
            print( s )
            counter = counter + 1


        statements.close()
        conn.close()

        return numStatements


def existsTripleLULnsTyped(targetRepo, namespace,
                   subjectLiteral,
                   predicateLocalName,
                   objLiteral,conn=None, datatype="STRING"):

        if conn==None:
            conn = getConn(targetRepo)

        subject_, predicate_,object_ = __getLUL(conn,namespace,
                                                 subjectLiteral,
                                                 predicateLocalName,
                                                 objLiteral,datatype)

        statements = conn.getStatements(subject_,predicate_,object_)

        numStatements = len(statements.string_tuples)
        #statements.enableDuplicateFilter() ## there are no duplicates, but this exercises the code that checks

        counter = 0
        for s in statements:
            print( s )
            counter = counter + 1

        if counter != numStatements:
            msg = "Error counter [{}] and numstatements [{}] out of sync".format( counter, numStatements)
            raise Exception(msg)

        statements.close()
        conn.close()

        return numStatements


def existsTripleUUU(targetRepo, namespace,
                   subjectLocalName,
                   predicateLocalName,
                   objectLocalName,conn=None):

        if conn==None:
            conn = getConn(targetRepo)

        subject_, predicate_,object_ = __getUUU(conn,namespace,
                                                 subjectLocalName,
                                                 predicateLocalName,
                                                 objectLocalName)

        statements = conn.getStatements(subject_, predicate_, object_)

        numStatements = len(statements.string_tuples)
        #statements.enableDuplicateFilter() ## there are no duplicates, but this exercises the code that checks

        counter = 0
        for s in statements:
            print( s )
            counter = counter + 1

        if counter != numStatements:
            msg = "Error counter [{}] and numstatements [{}] out of sync".format( counter, numStatements)
            raise Exception(msg)

        statements.close()
        conn.close()

        return numStatements

def addTripleUUUns(targetRepo, namespace,
                   subjectLocalName,
                   predicateLocalName,
                   objectLocalName, preventDuplicates = True):
    conn = getConn(targetRepo)

    subject_, predicate_,object_ = __getUUU(conn,namespace,
                                                 subjectLocalName,
                                                 predicateLocalName,
                                                 objectLocalName)

    if(preventDuplicates):
        if(existsTripleUUU(targetRepo,namespace,subjectLocalName,predicateLocalName,objectLocalName,conn)):
            print( "exists, ignoring save" )
        else:
            print ("adding new ... %s" % conn.size())
            conn.add(subject_, predicate_, object_)

    else:
        print ("grok why allowing duplicate UUU triples is a good idea??")
    return conn.size()



def addTripleLULnsTyped(targetRepo, namespace,
                   subjectLocalName,
                   predicateLocalName,
                   objLiteral, datatype="STRING", preventDuplicates = True):
    conn = getConn(targetRepo)
    subject_, predicate_,object_ = __getLUL(conn,namespace,
                                                 subjectLocalName,
                                                 predicateLocalName,
                                                 objLiteral,datatype)

    if(preventDuplicates):
        if( existsTripleLULnsTyped(targetRepo,namespace,subjectLocalName,predicateLocalName,objLiteral,conn,datatype)):
            print( "existed, no update" )
        else:
            print ("adding new ... %s" % conn.size())
            conn.add(subject_, predicate_, object_)
    else:
        print ("must still grok why dups should be allowed???")
    return conn.size()

def addTripleLUUns(targetRepo, namespace,
                   subjectLocalName,
                   predicateLocalName,
                   objLiteral,  preventDuplicates = True):
    conn = getConn(targetRepo)
    subject_, predicate_,object_ = __getLUU(conn,namespace,
                                                 subjectLocalName,
                                                 predicateLocalName,
                                                 objLiteral)

    conn.add(subject_, predicate_, object_)
    afterCount = conn.size()

    return afterCount


def addTripleUULnsTyped(targetRepo, namespace,
                   subjectLocalName,
                   predicateLocalName,
                   objLiteral, datatype="STRING", preventDuplicates = True):
    conn = getConn(targetRepo)
    subject_, predicate_,object_ = __getTypedLiteral(conn,namespace,
                                                 subjectLocalName,
                                                 predicateLocalName,
                                                 objLiteral,datatype)



    if(preventDuplicates):
        print ("check exists")
        if( existsTripleUULnsTyped(targetRepo,namespace,subjectLocalName,predicateLocalName,objLiteral,conn,datatype)):
            print( "existed, no update" )
        else:
            print ("adding new ... %s" % conn.size())

            conn.add(subject_, predicate_, object_)

    else:
        print ("must still grok why dups should be allowed???")
    return conn.size()


def addTripleUUL(targetRepo, subjectURI, predicateURI, objLiteral):
    conn = getConn(targetRepo)
    subject_ = conn.createURI(subjectURI)
    predicate_ = conn.createURI(predicateURI)
    object_ = conn.createLiteral(objLiteral)
    conn.add(subject_,predicate_,object_)
    return conn.size()



def addTripleTypedObj(targetRepo, subjectURI, predicateURI, objLiteral, datatype="INT"):
    conn = getConn(targetRepo)
    datatype_ = __getDatatype(datatype)

    subject_ = conn.createURI(subjectURI)
    predicate_ = conn.createURI(predicateURI)
    object_ = conn.createLiteral(objLiteral, datatype_)

    conn.add(subject_,predicate_,object_)

    return conn.size()




def loadRDF(targetRepo, path1 = "./rdfUpload/python-lesmis.rdf" ):
    conn = getConn(targetRepo)
    conn.addFile(path1, None, format=RDFFormat.RDFXML);


def getTriples(targetRepo):
    conn = getConn(targetRepo)
    rez = []
    try:
        queryString = "SELECT ?s ?p ?o  WHERE {?s ?p ?o .}"
        tupleQuery = conn.prepareTupleQuery(QueryLanguage.SPARQL, queryString)
        result = tupleQuery.evaluate();
        try:
            for bindingSet in result:
                s = bindingSet.getValue("s")
                p = bindingSet.getValue("p")
                o = bindingSet.getValue("o")
                rez.append([s.getValue(), p.getValue(), o.getValue()])
        finally:
            result.close()
    finally:
        conn.close();
        return rez



def addPerson(targetRepo, fullName, age):

    ret = existsTripleUULnsTyped(targetRepo,
                     'rdf.agentidea.com',
                     'agents/{}'.format(fullName),
                     'spec/people/#term_age',
                     age,
                     datatype="INT")


def addDestination(targetRepo, continent, city, heritage_site, year_posted):
    '''
    addDesination(MAIN_TARGET_REPO,'South America','Bolivia','City of Potosi' )

    '''

    # Add continent contains city
    ret = addTripleUUU(MAIN_TARGET_REPO, 
                       "http://semantic.vocab.grant/{}".format(continent.strip().replace(' ', '')),
                       "http://semantic.vocab.grant/contains_city",
                       "http://semantic.vocab.grant/{}".format(city))
    
    print (ret)

    # Add city has unesco site x
    ret = addTripleUUU(MAIN_TARGET_REPO, 
                       "http://semantic.vocab.grant/{}".format(city),
                       "http://semantic.vocab.grant/has_unesco_site",
                       "http://semantic.vocab.grant/{}".format(heritage_site.strip().replace(' ', '')))
    
    print (ret)
    # Add heritage site is in continent
    ret = addTripleUUU(MAIN_TARGET_REPO,
                       "http://semantic.vocab.grant/{}".format(heritage_site.strip().replace(' ', '')),
                       "http://dbpedia.org/ontology/Continent",
                       "http://semantic.vocab.grant/{}".format(continent.strip().replace(' ', '')))
                       
                       
    # Add heritage site first posted in year
    ret = addTripleTypedObj(MAIN_TARGET_REPO, 
                       "http://semantic.vocab.grant/{}".format(heritage_site.strip().replace(' ', '')),
                       "https://schema.org/year_posted",
                       year_posted)




def	getDestinations(predicateSuffix='Location'):
    conn = getConn()
    queryString = """
    SELECT ?s ?o
    {
        ?s <http://dbpedia.org/ontology/%s> ?o.
    }
    """ % predicateSuffix

    tupleQuery = conn.prepareTupleQuery(QueryLanguage.SPARQL, queryString)
    result = tupleQuery.evaluate()

    rez = []
    counter = 0
    for bindingSet in result:
       rez.append({'seq': counter,
                   's': bindingSet.getValue('s').getValue().strip(),
                   'o':bindingSet.getValue('o').getValue().strip()
                  })
       counter = counter + 1

    return rez

def getStory(predicateSuffix='headline'):
    conn = getConn("Annie")
    queryString = """
    SELECT ?s ?o ?url
    {
        ?s <http://rdf.agentidea.com/%s> ?o.
        ?s <http://rdf.agentidea.com/url> ?url.
    }
    """ % predicateSuffix

    tupleQuery = conn.prepareTupleQuery(QueryLanguage.SPARQL, queryString)
    result = tupleQuery.evaluate()

    rez = []
    counter = 0
    for bindingSet in result:
       rez.append({'seq': counter,
                   's': bindingSet.getValue('s').getValue().strip(),
                   'url': bindingSet.getValue('url').getValue().strip(),
                   'o':bindingSet.getValue('o').getValue().strip()
                  })
       counter = counter + 1

    return rez


def __getDatatype(stringType):
    if stringType.upper() == "INT":
        return XMLSchema.INT
    if stringType.upper() == "LONG":
        return XMLSchema.LONG
    if stringType.upper() == "DOUBLE":
        return XMLSchema.DOUBLE
    if stringType.upper() == "DECIMAL":
        return XMLSchema.DECIMAL
    if stringType.upper() == "FLOAT":
        return XMLSchema.FLOAT
    if stringType.upper() == "STRING":
        return XMLSchema.STRING
    if stringType.upper() == "BOOLEAN":
        return XMLSchema.BOOLEAN

    raise Exception("Unhandled Type %s" % stringType)




def testA():

    ret = addTripleUUU(MAIN_TARGET_REPO, "http://rdf.agentidea.com/name/GrantShipley",
                       "http://http://xmlns.com/foaf/spec/#term_knows",
                       "http://rdf.agentidea.com/name/LouiseShipley")

    print( ret )


    ret = addTripleUUL(MAIN_TARGET_REPO, "http://rdf.agentidea.com/name/GrantShipley",
                       "http://http://xmlns.com/foaf/spec/#term_knows",
                       "LouiseShipley")

    print( ret )

    ret = addTripleTypedObj(MAIN_TARGET_REPO, "http://rdf.agentidea.com/name/GrantShipley",
                       "http://xmlns.com/foaf/spec/#term_age",
                       42)

    print( ret )

    ret = addTripleTypedObj(MAIN_TARGET_REPO, "http://rdf.agentidea.com/name/GrantShipley",
                       "http://xmlns.com/foaf/spec/#term_status",
                       "Ebullient and Pensive","string")

    print( ret )

def testB():
    ret = addTripleUULns(MAIN_TARGET_REPO,
                         'rdf.agentidea.com',
                         'agents/GrantShipley',
                         'spec/people/#term_nick',
                         'Thor')

    print( ret )
    ret = addTripleUULns(MAIN_TARGET_REPO,
                         'rdf.agentidea.com',
                         'agents/GrantShipley',
                         'spec/people/#term_foaf',
                         'agents/Rhada')

    print( ret )
    ret = addTripleUULns(MAIN_TARGET_REPO,
                         'rdf.agentidea.com',
                         'agents/Rhada',
                         'spec/people/#term_foaf',
                         'agents/GrantShipley')
    print( ret )
    ret = addTripleUULns(MAIN_TARGET_REPO,
                         'rdf.agentidea.com',
                         'agents/Rhada',
                         'spec/people/#term_nick',
                         'Snorf')



    print( ret )
    ret = addTripleUULnsTyped(MAIN_TARGET_REPO,
                         'rdf.agentidea.com',
                         'agents/Rhada',
                         'spec/people/#term_age',
                         15,"INT")

    print( ret )

    ret = addTripleUULnsTyped(MAIN_TARGET_REPO,
                         'rdf.agentidea.com',
                         'agents/GrantShipley',
                         'spec/people/#term_age',
                         48,"INT")

    print( ret )



def testD():
    bnode = addTripleBlankNode(MAIN_TARGET_REPO,'http://rdf.agentidea.com/rel/A','foo','NumeroDuo')
    addTripleBlankNode(MAIN_TARGET_REPO,'http://rdf.agentidea.com/rel/B','boo',bnode)
    addTripleBlankNode(MAIN_TARGET_REPO,'http://rdf.agentidea.com/rel/N','noo',bnode)





    print( ret )
    ret = addTripleUULnsTyped(MAIN_TARGET_REPO,
                         'rdf.agentidea.com',
                         'agents/GrantShipley',
                         'spec/people/#term_age',
                         48,datatype="INT")



    print( ret )
    ret = existsTripleUULnsTyped(MAIN_TARGET_REPO,
                     'rdf.agentidea.com',
                     'agents/GrantShipley',
                     'spec/people/#term_age',
                     48,datatype="INT")

    print( ret )

def testG():

    ret = existsTripleUUnsTyped(MAIN_TARGET_REPO,
                     'rdf.agentidea.com',
                     'agents/GrantShipley',
                     'spec/people/#term_age')
    print( ret )

def testH():

    ret = addTripleUULnsTyped(MAIN_TARGET_REPO,
                         'rdf.agentidea.com',
                         'agents/GrantShipley',
                         'spec/people/#term_age',
                         49,datatype="INT", preventDuplicates=True)
    print( ret )



def testJ():
    ret = addTripleLUUns(MAIN_TARGET_REPO,'rdf.agentidea.com','xyzABC',
                         'spec/people/#term_src','http://www.agentidea.com')




if __name__ == '__main__':

    #lets add some UNESCO heritage site infromation related to reqion
    addDestination(MAIN_TARGET_REPO,'North Africa','St Floris','Manovo-Gounda St Floris National Park', 1997)
    addDestination(MAIN_TARGET_REPO,'Southern Africa','Nelspruit, South Africa','Kruger National Park', 2019)
    addDestination(MAIN_TARGET_REPO,'Europe','Paris France','Eifell Tower', 2005) 
    addDestination(MAIN_TARGET_REPO,'Europe','Vienna Austria','Historic Centre of Vienna', 2017)
    addDestination(MAIN_TARGET_REPO,'South America','Bolivia','City of Potosi', 2014)
    addDestination(MAIN_TARGET_REPO,'Central America','Tulum Mexico','Mayan Ruins of Tulum', 2001)
    addDestination(MAIN_TARGET_REPO,'Central America','Cancun Mexico','Chichen Itza', 1985)
    addDestination(MAIN_TARGET_REPO,'Central America','Cancun Mexico','Xichen', 1977)
    addDestination(MAIN_TARGET_REPO,'Central America','Lake Peten Itza Guatemala','Tikal', 1977)
