from django.shortcuts import render
import requests

API_BASE = "http://127.0.0.1:8000"
API_USUARIOS = f"{API_BASE}/api/usuarios/"

def formulario_view(request):
    mensaje = error = None
    usuarios = []


    try:
        resp = requests.get(
            API_USUARIOS,
            headers={"Accept": "application/json"},
            timeout=5
        )
        if resp.status_code == 200:
            usuarios = resp.json()
        else:
            error = f"Error al cargar lista: HTTP {resp.status_code}"
    except Exception as e:
        error = f"Error de conexión al cargar lista: {e}"

    # 2) Procesar formulario (crear / actualizar / eliminar)
    if request.method == "POST":
        accion    = request.POST.get("accion")         # crear | actualizar | eliminar
        user_id   = request.POST.get("id")
        nombre    = request.POST.get("nombre")
        apellidos = request.POST.get("apellidos")
        correo    = request.POST.get("correo")
        rol_raw   = request.POST.get("rol")

        # castear rol si tu API lo espera numérico
        try:
            rol = int(rol_raw) if rol_raw not in (None, "") else None
        except ValueError:
            rol = rol_raw

        data = {
            "nombre": nombre,
            "apellidos": apellidos,
            "correo": correo,
            "rol": rol,
        }

        try:
            if accion == "crear":
                resp = requests.post(API_USUARIOS, json=data, timeout=5)
                if resp.status_code == 201:
                    mensaje = "Usuario creado correctamente."
                else:
                    error = f"Error {resp.status_code}: {resp.text}"

            elif accion == "actualizar":
                if not user_id:
                    error = "Debes proporcionar un ID para actualizar."
                else:
                    url = f"{API_USUARIOS}{user_id}/"
                    resp = requests.put(url, json=data, timeout=5)
                    if resp.status_code == 200:
                        mensaje = "Usuario actualizado correctamente."
                    else:
                        error = f"Error {resp.status_code}: {resp.text}"

            elif accion == "eliminar":
                if not user_id:
                    error = "Debes proporcionar un ID para eliminar."
                else:
                    url = f"{API_USUARIOS}{user_id}/"
                    resp = requests.delete(url, timeout=5)
                    if resp.status_code in (200, 204):
                        mensaje = "Usuario eliminado correctamente."
                    else:
                        error = f"Error {resp.status_code}: {resp.text}"

            # 3) Recargar lista después de la operación
            resp = requests.get(API_USUARIOS, headers={"Accept": "application/json"}, timeout=5)
            if resp.status_code == 200:
                usuarios = resp.json()

        except Exception as e:
            error = f"Error de conexión: {e}"

    return render(request, "formulario.html", {
        "mensaje": mensaje,
        "error": error,
        "usuarios": usuarios
    })