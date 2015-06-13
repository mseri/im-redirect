from bottle import route, redirect, run
import json

with open("redirect.json", "r", encoding="utf-8", errors="ignore") as f:
  raw_data = json.loads(f.read())
  failback_url = raw_data["otherwise"]
  redirect_dict = raw_data["redirects"]

@route("/<full_route:re:.+>")
def go_away(full_route):
    redirect_url = redirect_dict.get(full_route, failback_url)
    redirect(redirect_url)

run(host="0.0.0.0", port=8000, debug=False)
