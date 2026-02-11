from datetime import datetime


class SocialNetwork:

    def __init__(self):
        self.post_id = 0
        self.usuarios = {}
        self.post = {}

    def registrar_usuario(self, user_id: str, name: str):

        if user_id in self.usuarios:
            print(f"El usuario con el ID {user_id} ya existe.")
            return

        self.usuarios[user_id] = {
            "name": name,
            "seguidos": set(),
            "seguidores": set(),
            "post": []
        }
        print(
            f"Usuario con ID '{user_id}' y nombre '{
                name}' registrado correctamente."
        )

    def seguir_usuario(self, user_id: str, follow_id: str):

        if user_id not in self.usuarios or follow_id not in self.usuarios:
            print("Alguno de los usuarios no existe. No se puede realizar el follow.")
            return

        self.usuarios[user_id]["seguidos"].add(follow_id)
        self.usuarios[follow_id]["seguidores"].add(user_id)
        print(
            f"{self.usuarios[user_id]["name"]} ahora sigue a {
                self.usuarios[follow_id]["name"]}."
        )

    def dejar_seguir_usuario(self, user_id: str, unfollow_id: str):

        if user_id not in self.usuarios or unfollow_id not in self.usuarios:
            print("Alguno de los usuarios no existe. No se puede realizar el unfollow.")
            return

        self.usuarios[user_id]["seguidos"].discard(unfollow_id)
        self.usuarios[unfollow_id]["seguidores"].discard(user_id)
        print(
            f"{self.usuarios[user_id]["name"]} ha dejado de seguir a {
                self.usuarios[unfollow_id]["name"]}."
        )

    def crear_post(self, user_id: str, text: str):

        if user_id not in self.usuarios:
            print(f"El usuario '{user_id}' no existe.")
            return

        if len(text) > 200:
            print("El post no puede tener más de 200 caracteres.")
            return

        self.post_id += 1

        post_id = self.post_id

        self.post[post_id] = {
            "user_id": user_id,
            "text": text,
            "created_at": datetime.now(),
            "likes": set()
        }

        self.usuarios[user_id]["post"].append(post_id)

        print("Post creado correctamente.")

    def eliminar_post(self, post_id: int):

        if post_id not in self.post:
            print(f"El post con ID {post_id} no existe.")
            return

        user_id = self.post[post_id]["user_id"]
        self.usuarios[user_id]["post"].remove(post_id)
        del self.post[post_id]
        print("Post eliminado correctamente.")

    def like_post(self, user_id: str, post_id: int):

        if user_id not in self.usuarios:
            print(f"El usuario '{user_id}' no existe.")
            return

        if post_id not in self.post:
            print(f"El post '{post_id}' no existe.")
            return

        self.post[post_id]["likes"].add(user_id)
        print(f"Nuevo like en post '{post_id}'.")

    def unlike_post(self, user_id: str, post_id: int):

        if user_id not in self.usuarios:
            print(f"El usuario '{user_id}' no existe.")
            return

        if post_id not in self.post:
            print(f"El post '{post_id}' no existe.")
            return

        self.post[post_id]["likes"].discard(user_id)
        print(f"Like eliminado en post '{post_id}'.")

    def ver_feed_usuario(self, user_id: str):

        if user_id not in self.usuarios:
            print(f"El usuario '{user_id}' no existe.")
            return

        feed = sorted(
            (self.post[post_id] for post_id in self.usuarios[user_id]["post"]),
            key=lambda x: x["created_at"],
            reverse=True
        )[:10]

        for post in feed:
            print(f"""
ID usuario: {post["user_id"]}
Usuario: {self.usuarios[post["user_id"]]["name"]}
Texto: {post["text"]}
Fecha: {post["created_at"]}
Likes: {len(post["likes"])}
                    """)

    def ver_seguidos(self, user_id: str):

        if user_id not in self.usuarios:
            print(f"El usuario '{user_id}' no existe.")
            return

        following_post_ids = []

        for following_id in self.usuarios[user_id]["seguidos"]:
            following_post_ids.extend(self.usuarios[following_id]["post"])

        feed = sorted(
            (self.post[post_id] for post_id in following_post_ids),
            key=lambda x: x["created_at"],
            reverse=True
        )[:10]

        for post in feed:
            print(f"""
ID usuario: {post["user_id"]}
Usuario: {self.usuarios[post["user_id"]]["name"]}
Texto: {post["text"]}
Fecha: {post["created_at"]}
Likes: {len(post["likes"])}
                    """)


social_network = SocialNetwork()
social_network.registrar_usuario("andres", "franco mesa")
social_network.registrar_usuario("yeison", "yeison 87")

social_network.crear_post("andres", "Hola mundo!")
social_network.crear_post("andres", "Hola mundo 2!")
social_network.crear_post("andres", "Hola mundo 3!")

social_network.crear_post("yeison", "Hola mundo!")
social_network.crear_post("yeison", "Hola mundo 2!")
social_network.crear_post("yeison", "Hola mundo 3!")

social_network.seguir_usuario("yeison", "andres")

social_network.like_post("yeison", 1)

social_network.ver_feed_usuario("andres")
social_network.ver_seguidos("yeison")

social_network.unlike_post("yeison", 1)

social_network.ver_seguidos("yeison")