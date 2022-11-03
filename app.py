import datefinder
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DateInput(BaseModel):
    text: str


@app.post('/convert')

def date_frm_str(dateInput: DateInput):

  string_with_dates = dateInput.text
  matches = datefinder.find_dates(string_with_dates)
  return {"data" : matches}