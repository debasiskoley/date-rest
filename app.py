import datefinder
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class DateInput(BaseModel):
    text: str


@app.get('/')
def get_date():
  return "date app working.."

@app.get('/date')
def get_todate():
  today = date.today()
  return today

@app.post('/convert')
def date_frm_str(dateInput: DateInput):

  string_with_dates = dateInput.text
  matches = datefinder.find_dates(string_with_dates)
  return {"data" : matches}