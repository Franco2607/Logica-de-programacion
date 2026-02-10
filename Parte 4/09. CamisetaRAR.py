# "zipfile" Aprende a trabajar con ficheros comprimidos
import zipfile
import os


def archivo_zip(path: str, archivo: str) -> str:

    archivo_path = os.path.join(path, archivo)

    if os.path.exists(archivo_path):

        archivo_zip = f"{archivo}.zip"
        zip_path = os.path.join(path, archivo_zip)

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(archivo_path, archivo)
            print(f"Archivo {archivo} comprimido como {archivo_zip}.")
            return archivo_zip

    else:
        print(f"El archivo {archivo} no existe el directorio {path}.")

    return None


def unzip_archivo(path: str, archivo: str):

    archivo_path = os.path.join(path, archivo)

    if os.path.exists(archivo_path):

        zip_path = os.path.join(path, archivo)

        with zipfile.ZipFile(zip_path) as zipf:
            zipf.extractall(path)
            print(f"Archivo {archivo} descomprimido en {path}.")

    else:
        print(f"El archivo {archivo} no existe el directorio {path}.")


path = os.path.dirname(os.path.abspath(__file__))  # Directorio actual
archivo = "IA.pdf"

zip = archivo_zip(path, archivo)

if zip != None:

    # Borro el fichero original antes de descomprimir el zip
    os.remove(os.path.join(path, archivo))

    unzip_archivo(path, zip)