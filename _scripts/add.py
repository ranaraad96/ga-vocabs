import glob
import rdflib
from rdflib.namespace import RDF, SKOS, DCTERMS
REG = rdflib.Namespace("http://purl.org/linked-data/registry#")

for f in glob.glob("iso/*"):
    print("adding to {}".format(f))
    g = rdflib.Graph().parse(f, format="turtle")
    # extra = """
    # @prefix sdo: <https://schema.org/> .
    #
    # <https://linked.data.gov.au/org/ga/voc-wg>
    #     a sdo:Organization ;
    #     sdo:name "Geoscience Australia Vocabulary Working Group" ;
    #     sdo:url <https://www.ga.gov.au/data-pubs/datastandards> ;
    #     sdo:affiliation <https://linked.data.gov.au/org/ga> ;
    # .
    #
    # <https://linked.data.gov.au/org/ga>
    #     a sdo:Organization ;
    #     sdo:name "Geoscience Australia" ;
    #     sdo:url <https://www.ga.gov.au> ;
    # .
    # """
    # g.parse(data=extra, format="turtle")

    for s, p, o in g.triples((None, RDF.type, SKOS.Concept)):
        # g.remove((s, DCTERMS.dateAccepted, None))
        # g.remove((s, DCTERMS.dateSubmitted, None))
        g.remove((s, REG.register, None))

    # for s, p, o in g.triples((None, RDF.type, SKOS.Concept)):
    #     g.remove(s, DCTERMS.dateAccepted, None)
    #     g.remove(s, DCTERMS.dateSubmitted, None)
    #     # g.remove(s, REG., None)

    g.serialize(f, format="turtle")
