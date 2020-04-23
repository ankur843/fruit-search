
# coding: utf-8

# In[ ]:


import aiohttp
import asyncio
import uvicorn
from fastai import *
from fastai.vision import *
from io import BytesIO
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.routing import Route
import mapgraphdata

export_file_url = 'https://drive.google.com/uc?export=download&id=1fYtwrNO6AtksAzpqHo7oNpx3yJ_KEZkR'
export_file_name = 'only-fruits-classifier.pkl'

# classes = ['perfect', 'imperfect', 'rotten']
classes=['acerolas', 'apples', 'apricots', 'avocados', 'bananas', 'blackberries', 'blueberries', 'cantaloupes', 'cherries', 'coconuts', 'figs', 'grapefruits', 'grapes', 'guava', 'kiwifruit', 'lemons', 'limes', 'mangos', 'olives', 'oranges', 'passionfruit', 'peaches', 'pears', 'pineapples', 'plums', 'pomegranates', 'raspberries', 'strawberries', 'tomatoes', 'watermelons']
path = Path(__file__).parent
templates = Jinja2Templates(directory='')





async def homepage(request):
    template = "keywords.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)


async def graph_nodes(request):
    param=dict(request.query_params)
    return JSONResponse(mapgraphdata.graph_ideas(param['keyword']))

async def map_data(request):
    param=dict(request.query_params)
    return JSONResponse(mapgraphdata.map_data(param['keyword']))

async def cluster_data(request):
    param=dict(request.query_params)
    return JSONResponse(mapgraphdata.cluster_data(param['keyword']))


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/graph_nodes', graph_nodes),
    Route('/map_data', map_data),
    Route('/cluster', cluster_data)
   
])

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory='static'))

#if __name__ == '__main__':
#if 'serve' in sys.argv:
uvicorn.run(app=app, host='0.0.0.0', port=8080, log_level="info")

