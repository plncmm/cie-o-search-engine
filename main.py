import fastapi
import whoosh.index
import whoosh.qparser

app = fastapi.FastAPI(title="CIE-O-3-M Search Engine", description="API for searching in CIE-O-3-M", version="1.0")

ix_m = whoosh.index.open_dir("index_m")
parser_m = whoosh.qparser.MultifieldParser(["description","description_additional"], ix_m.schema, group=whoosh.qparser.OrGroup.factory(0.9))
searcher_m = ix_m.searcher()

@app.get("/cie-o-m")
async def search_cieom(q: str):  
    myquery = parser_m.parse(q)
    results = searcher_m.search(myquery, limit=10, terms=True)
    response = []
    for result in results:
        response.append(result.fields())
    return response

@app.on_event('shutdown')
def shutdown():
    searcher_m.close()