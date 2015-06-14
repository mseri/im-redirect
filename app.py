from bottle import Bottle, redirect
import json, os

REPO = os.environ.get('OPENSHIFT_REPO_DIR','.')

app = Bottle()

with open(REPO + "/redirect.json", "r", encoding="utf-8", errors="ignore") as f:
  raw_data = json.loads(f.read())
  fallback_url = raw_data["otherwise"]
  redirect_dict = raw_data["redirects"]

@app.route("/")
def root():
    redirect(fallback_url)

@app.route("/<full_route:re:.+>")
def go_away(full_route):
  redirect_url = redirect_dict.get(full_route, fallback_url)
  redirect(redirect_url)
