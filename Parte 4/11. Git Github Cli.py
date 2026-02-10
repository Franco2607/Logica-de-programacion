import os
# Importa run del depurador de python (pdb)
from pdb import run
# Sirve para ejecutar comandos de consola (git, pwd, etc) desde python
import subprocess


def correr_comando(comando: str):

    try:
        resultado = subprocess.run(
            comando,
            shell=True,
            check=True,
            text=True,
            capture_output=True
        )
        print(resultado.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.strip()}")


def establecer_directorio_trabajo():

    path = input("Introduce el directorio completo de trabajo: ")
    if os.path.isdir(path):
        os.chdir(path)
        print(f"El directorio de trabajo ha cambiado a: {path}")
    else:
        print("El directorio introducido no existe.")


def crear_repositorio():
    if os.path.isdir(".git"):
        print("Ya existe un repositorio en este directorio.")
    else:
        correr_comando("git init")
        correr_comando("git branch -M main")
        print("Repositorio inicializado.")


def crear_new_rama():
    branch_name = input("Nombre de la nueva rama: ")
    correr_comando(f"git branch {branch_name}")


def cambiar_rama():
    branch_name = input("Nombre de la rama a la que quieres cambiar: ")
    correr_comando(f"git checkout {branch_name}")


def mostrar_ficheros_pendientes():
    correr_comando("git status -s")


def hacer_commit():
    message = input("Mensaje para el commit: ")
    correr_comando("git add .")
    correr_comando(f"git commit -m \"{message}\"")


def mostrar_hitorial_commits():
    correr_comando("git log --oneline")


def Eliminar_brach():
    branch_name = input("Nombre de la rama a eliminar: ")
    correr_comando(f"git branch -d {branch_name}")


def establecer_repositorio_remoto():
    remote_url = input("URL del repositorio remoto: ")
    correr_comando(f"git remote add origin {remote_url}")
    correr_comando("git push -u origin main")


def hacer_pull():
    correr_comando("git pull")


def hacer_push():
    correr_comando("git push")


while True:

    print("\nDirectorio actual de trabajo:")
    print(os.getcwd())

    print("\nGit y GitHub CLI - Opciones:")
    print("1. Establecer el directorio de trabajo")
    print("2. Crear un nuevo repositorio")
    print("3. Crear una nueva rama")
    print("4. Cambiar de rama(Branch)")
    print("5. Mostrar ficheros pendientes de hacer commit")
    print("6. Hacer commit (+add)")
    print("7. Mostrar el historial de commits")
    print("8. Eliminar rama(branch)")
    print("9. Establecer repositorio remoto")
    print("10. Hacer pull")
    print("11. Hacer push")
    print("12. Salir")

    choice = input("Selecciona una opción (1 al 12): ")

    match choice:
        case "1":
            establecer_directorio_trabajo()
        case "2":
            crear_repositorio()
        case "3":
            crear_new_rama()
        case "4":
            cambiar_rama()
        case "5":
            mostrar_ficheros_pendientes()
        case "6":
            hacer_commit()
        case "7":
            mostrar_hitorial_commits()
        case "8":
            Eliminar_brach()
        case "9":
            establecer_repositorio_remoto()
        case "10":
            hacer_pull()
        case "11":
            hacer_push()
        case "12":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida.")