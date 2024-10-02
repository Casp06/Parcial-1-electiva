import redis
import time

# Configuración de Redis
redis_host = 'redis-18867.c15.us-east-1-4.ec2.redns.redis-cloud.com'
redis_port = 18867  # Cambia al puerto correspondiente a este
redis_password = 'XvBJXr5IfOwd3705NANCgAQ7ClvsX1lx'

# Conexión a Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Publicador
def publisher():
    while True:
        message = input("Introduce un mensaje para publicar: ")
        redis_client.publish('canal_prueba', message)
        print(f"Publicado: {message}")

if __name__ == "__main__":
    publisher()
