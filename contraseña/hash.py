#pip install bcrypt
import bcrypt


password = "contraseña1029"

salt = bcrypt.gensalt() # Nivel de dificultad

hashed = bcrypt.hashpw(password.encode('utf-8'),salt)

print(hashed)  

