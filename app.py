from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["get", "post"])
def home():
    info_formulario = ""
    if request.method == "post":
        info_formulario = request.form.get("contenido")
        print(f"Hola {info_formulario}")
    return render_template( template_name_or_list = "formulario.html", nombre=info_formulario)

if __name__ == "__main__":
    app.run()