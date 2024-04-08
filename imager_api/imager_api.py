# api that will be used to connect the imager_django backend to the imager model {??if that's how this works}
from fastapi import FastAPI, Path
from pydantic import BaseModel

class ImagerItems(BaseModel):
    pass

api = FastAPI()

@api.post()
def post_whatever():
    pass