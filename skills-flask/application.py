from flask import Flask, render_template, request

app = Flask(__name__)

# we need two routes here (besides basic index page)
# one to serve the form and collect form data
# the other to render/respond to the data submitted in the form


@app.route("/")
def index_page():
    """Ubermelon's job application system index page."""

    return render_template("index.html")


@app.route("/application-form")
def job_app_form():
    """Render a job application form page."""

    return render_template("application-form.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application", methods=["POST"])
def response_to_form():
    """Render response to job application form submission."""

    # assign variables for form data
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    title = request.form.get("jobtitle")
    salary = request.form.get("salaryreq")

    # return response form with appropriate values plugged in
    return render_template("application-response.html",
                           first_name=first_name,
                           last_name=last_name,
                           title=title,
                           salary=salary)


if __name__ == "__main__":
    app.run(debug=True)
