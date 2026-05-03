from flask import Flask, request, redirect, render_template, jsonify, abort
from database import init_db, create_short_link, get_link, record_click, get_all_links

print("Starting URL Shortener App...")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shorten", methods=["POST"])
def shorten():
    data = request.get_json()
    original_url = data.get("url").strip()
    if not original_url:
        return jsonify({"error": "URL is required"}), 400
    
    if not original_url.startswith(("http://", "https://")):
        original_url = "https://" + original_url

    code = create_short_link(original_url)
    short_url = f"{request.host_url}{code}"

    return jsonify({
        "short_url": short_url,
        "code": code,
        "original_url": original_url
    })

@app.route("/<code>")
def redirect_to_original(code):
    link = get_link(code)
    if link:
        record_click(code)
        return redirect(link["original"])
    else:
        abort(404)

@app.route("/analytics")
def analytics():
    links = get_all_links()
    return render_template("analytics.html", links=links)


if __name__ == "__main__":
    init_db()
    app.run(debug=True , host="0.0.0.0", port=5000)