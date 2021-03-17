import fastapi
import whoosh.index
import whoosh.qparser

app = fastapi.FastAPI(title="CIE-O-3-M Search Engine", description="API for searching in CIE-O-3-M", version="1.0")

ix = whoosh.index.open_dir("index")
parser = whoosh.qparser.MultifieldParser(["description","description_additional"], ix.schema, group=whoosh.qparser.OrGroup.factory(0.9))
searcher = ix.searcher()

@app.get("/cie-o-m")
async def search_cieom(q: str):  
    myquery = parser.parse(q)
    results = searcher.search(myquery, limit=10, terms=True)
    response = []
    for result in results:
        response.append(result.fields())
    return response

@app.on_event('shutdown')
def shutdown():
    searcher.close()