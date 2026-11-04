# REST GUI API

A desktop purchase form built with Tkinter that collects purchase data, validates it locally, and POSTs it as JSON to a small Flask API.

## What it does

- `app.py` — Tkinter form: Product ID, Description, Customer Name, Email, Price, and an Online checkbox (checked = online, unchecked = in-store)
- `api.py` — Flask API with one endpoint: `POST /submit`
- The form validates before sending: every field filled in, email contains an @, price is a number no greater than $1,000.00
- The API checks the same rules and returns the received data as JSON, which the form shows in a popup

## Run it

```sh
python -m venv venv
.\venv\Scripts\activate
pip install Flask
