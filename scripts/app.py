# app.py
from flask import Flask, flash, redirect, render_template, request, session, url_for

from . import auth, core, feature

app = Flask(__name__)
app.secret_key = "topsecretpassword"


# Route for the login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if auth.authenticate(username, password):
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password", "error")

    return render_template("login.html")


# Route for creating a new user
@app.route("/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        new_username = request.form["new_username"]
        new_password = request.form["new_password"]

        if auth.create_new_user(new_username, new_password):
            flash("User created successfully!", "success")
            return redirect(url_for("login"))
        else:
            flash("Username already exists.", "error")

    return render_template("create_user.html")


# Route for the firewall dashboard
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", username=session["username"])


# Route for handling filtering and block/unblock actions
@app.route("/filter", methods=["POST"])
def filter_action():
    if "username" not in session:
        return redirect(url_for("login"))

    ip = request.form.get("ip")
    mac = request.form.get("mac")
    port = request.form.get("port")
    protocol = request.form.get("protocol")
    action = request.form.get("action")

    # Check what action to take
    if action == "block":
        if ip:
            core.block_ip(ip)
        if mac:
            core.block_mac(mac)
        if port:
            core.block_port(port)
        if protocol:
            core.block_protocol(protocol)
        flash("Blocking action executed", "success")
        feature.make_rules_persistent()

    elif action == "unblock":
        if ip:
            core.unblock_ip(ip)
        if mac:
            core.unblock_mac(mac)
        if port:
            core.unblock_port(port)
        if protocol:
            core.unblock_protocol(protocol)
        flash("Unblocking action executed", "success")
        feature.make_rules_persistent()

    return redirect(url_for("dashboard"))


# Route for logging out
@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


@app.route("/logs")
def logs():
    with open("firewall_actions.log", "r") as log_file:
        log_entries = log_file.readlines()
    return render_template("logs.html", log_entries=log_entries)


@app.route("/reset")
def reset():
    core.reset_rule()
    feature.make_rules_persistent()
    return render_template("reset.html")
