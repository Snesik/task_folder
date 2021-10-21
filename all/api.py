from folder import tree
from fastapi import FastAPI

app = FastAPI()



@app.get('/')
async def root():
   return {'Hello'}

@app.get('/{a}')
async def work(a:str):
   return tree('/' + a.replace('-', '/'))