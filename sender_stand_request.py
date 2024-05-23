import configuration
import requests
import data


# Agregamos un nuevo usuario para generar el token de autenticación


def post_new_user(body):  # aplicamos la función con la variabla post_new_user para generar el nuevo usuario
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# Nos muestra como resultado, el codigo 201 de confirmacion y el token.
# Ahora vamos a generar el token de autenticación para crear un kit


def get_user_new_token():
    token_new = post_new_user(data.user_body)
    response_json = token_new.json()
    auth_token_new_user = response_json['authToken']  # aqui nos busca la clave de confirmación "authorization"
    # en el directorio seleccionado para el usuario registrado
    return auth_token_new_user  # Nos devuelve el vlor del token que llamamos a la función


# llamamos el valor del token "authtoken" para la creación del nuevo kit
# Ahora generamos la creación del nuevo kit


def post_new_client_kit(kits):  # Realizamos una solicitud POST para crear kits por productos.
    token = get_user_new_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"  # Agrega el token de autorización al encabezado
    }
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_MAIN_KITS,
                             json=kits,
                             headers=headers)
    return response