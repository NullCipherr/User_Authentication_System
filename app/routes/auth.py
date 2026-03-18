from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from app.services.auth_service import (
    authenticate_user,
    register_user,
    validate_registration_form,
)

auth_bp = Blueprint("auth", __name__)


@auth_bp.get("/")
def index():
    return render_template("index.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        cpf = request.form.get("cpf", "").strip()
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        repeat_password = request.form.get("repeat_password", "")

        error = validate_registration_form(name, cpf, username, password, repeat_password)
        if error:
            flash(error, "error")
            return render_template("register.html")

        user_id = register_user(name, cpf, username, password)
        session["user_id"] = user_id
        session["username"] = username
        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for("auth.dashboard"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            flash("Preencha usuário e senha.", "error")
            return render_template("login.html")

        user = authenticate_user(username, password)
        if user is None:
            flash("Usuário ou senha inválidos.", "error")
            return render_template("login.html")

        session["user_id"] = user["id"]
        session["username"] = user["username"]
        flash("Login realizado com sucesso!", "success")
        return redirect(url_for("auth.dashboard"))

    return render_template("login.html")


@auth_bp.get("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Faça login para continuar.", "error")
        return redirect(url_for("auth.login"))

    return render_template("dashboard.html", username=session.get("username"))


@auth_bp.post("/logout")
def logout():
    session.clear()
    flash("Logout realizado.", "success")
    return redirect(url_for("auth.index"))
