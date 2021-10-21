from folder import tree
from fastapi import FastAPI

app = FastAPI()



@app.get('/')
async def root():
   return {'Hello'}

@app.get('/1/{a}')
async def work(a:str):
   a = a.replace('-', '/')
   b = tree('/' + a)
   return b