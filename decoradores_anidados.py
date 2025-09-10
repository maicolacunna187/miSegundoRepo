"""
🔹 Ejercicio 1: Validar y medir tiempo

Cree dos decoradores:

validar_positivos → revisa que todos los argumentos sean positivos.

medir_tiempo → mide cuánto tarda la función.

Aplíquelos anidados a una función que calcule el área de un triángulo.

👉 Objetivo: practicar el orden en que se ejecutan los decoradores.

"""

import time

def validar_positivos(func):
    def wrapper(*args, **kwargs):
        for i in list(args) + list(kwargs.values()):
            if isinstance(i, (int,float)) and i < 0:
                raise ValueError("Error: El número es negativo.")
        return func(*args, **kwargs)
    return wrapper 

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        print("Iniciando proceso...")
        star_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Proceso finalizado...")
        print(f"El código tardo: {end_time - star_time} segundos")
        return result
    return wrapper

@medir_tiempo
@validar_positivos
def calcular_area_rectangulo(base,altura):
    if not isinstance(base, (int, float)) or not isinstance(altura, (int,float)):
        raise TypeError("Base y altura deben ser numéricos.")
    return base * altura

# # ✅ Pruebas
# print(calcular_area_rectangulo(10, 5))  # 50
# print(calcular_area_rectangulo(base=3, altura=4))  # 12
# print(calcular_area_rectangulo(-1, 2))  # ❌ Lanza ValueError


"""
🔹 Ejercicio 2: Autenticación y logging

Cree dos decoradores:

verificar_usuario → solo permite ejecutar la función si el usuario está autenticado.

logger → imprime un mensaje en consola indicando la función llamada y sus argumentos.

Aplíquelos a una función transferir(monto, destino) que simule una transferencia bancaria.

👉 Objetivo: ver cómo los decoradores anidados pueden controlar seguridad y registro de acciones al mismo tiempo.

"""

def verificar_usuario(role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("role") == role:
                print("✅ Ingreso exitoso.")
                return func(user, *args, **kwargs)
            else:
                print(f"❌ Acceso denegado. Solo {role} pueden acceder.")
        return wrapper
    return decorator

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"📌 Llamando a la función: {func.__name__}")
        print(f"➡️ Argumentos: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"✔️ Ejecución terminada: {func.__name__}")
        return result
    return wrapper


@logger
@verificar_usuario("admin")
def transferir(user, monto, destino):
    print(f"💸 Transfiriendo ${monto} a la cuenta {destino}...")
    return f"Transferencia de {monto} a {destino} realizada por {user['name']}."


# ✅ Pruebas
admin = {"name": "Nubia", "role": "admin"}
cliente = {"name": "Luis", "role": "cliente"}

print("\n--- Intento con admin ---")
print(transferir(admin, 5000, "Cuenta #12345"))

print("\n--- Intento con cliente ---")
print(transferir(cliente, 2000, "Cuenta #98765"))
