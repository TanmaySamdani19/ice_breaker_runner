from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from ice_breaker import ice_break_with
from email_generator import generate_email

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_pic_url = ice_break_with(name=name)
    return jsonify(
        {
            "summary_and_facts": summary.to_dict(),
            "picture_url": profile_pic_url,
        }
    )


@app.route("/generate_email", methods=["POST"])
def generate_email_route():
    data = request.json
    name = data.get("name")
    summary = data.get("summary")
    facts = data.get("facts")
    length = data.get("length", "medium")  # short, medium, long
    tone = data.get("tone", "professional")  # professional, friendly, casual
    purpose = data.get(
        "purpose", "networking"
    )  # networking, job_inquiry, collaboration

    email_content = generate_email(
        name=name,
        summary=summary,
        facts=facts,
        length=length,
        tone=tone,
        purpose=purpose,
    )

    return jsonify({"email": email_content.to_dict()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
