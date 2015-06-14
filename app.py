from bottle import Bottle, redirect
import json

app = Bottle()

with open("redirect.json", "r", encoding="utf-8", errors="ignore") as f:
  raw_data = json.loads(f.read())
  fallback_url = raw_data["otherwise"]
  redirect_dict = raw_data["redirects"]

@app.route("/")
def root():
    redirect(fallbcak_url)

@app.route("/<full_route:re:.+>")
def go_away(full_route):
  redirect_url = redirect_dict.get(full_route, fallback_url)
  redirect(redirect_url)

if __name__=="__main__":
  app.run(host="0.0.0.0", port=8090, debug=True)
