import fastapi
import whoosh.index
import whoosh.qparser

app = fastapi.FastAPI(title="CIE-O-3 Search Engine", description="API for searching in CIE-O-3", version="1.0")

ix_m = whoosh.index.open_dir("index_m")
parser_m = whoosh.qparser.MultifieldParser(["description","description_additional"], ix_m.schema, group=whoosh.qparser.OrGroup.factory(0.9))
searcher_m = ix_m.searcher()

@app.get("/cie-o-m")
async def search_cieom(q: str):  
    myquery = parser_m.parse(q)
    results = searcher_m.search(myquery, limit=10, terms=True)
    response = []
    for result in results:
        hit = {
            "code":result["code"],
            "description":result["description"],
            "score":result.score,
        }
        response.append(hit)
    return response

ix_t = whoosh.index.open_dir("index_t")
parser_t = whoosh.qparser.MultifieldParser(["description","description_additional"], ix_t.schema, group=whoosh.qparser.OrGroup.factory(0.9))
searcher_t = ix_t.searcher()

@app.get("/cie-o-t")
async def search_cieot(q: str):  
    myquery = parser_t.parse(q)
    results = searcher_t.search(myquery, limit=10, terms=True)
    response = []
    for result in results:
        hit = {
            "code":result["code"],
            "description":result["description"],
            "score":result.score,
        }
        response.append(hit)
    return response

@app.on_event('shutdown')
def shutdown():
    searcher_m.close()
    searcher_t.close()