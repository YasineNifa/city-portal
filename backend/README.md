# Inside the container backend
Pour se connecter à l'intérieur du container pour executer une commande de type `python manage.py`
```bash
docker exec -it lausanne_backend bash
django@bd6f60187edf:/app$ python manage.py populate_department
```
Pour se connecter à la db
```bash
docker exec -it db psql -h db -d portal_db -U portal_user
```
Pour savoir les containers créés
```bash
docker ps                            
CONTAINER ID   IMAGE                                               COMMAND                  CREATED             STATUS                         PORTS                    NAMES
b4ff3d50da1d   city-portal_frontend                                "/docker-entrypoint.…"   About an hour ago   Up 26 minutes                  0.0.0.0:3001->80/tcp     lausanne_frontend
bd6f60187edf   city-portal_backend                                 "/app/entrypoint.sh"     About an hour ago   Up 26 minutes                  0.0.0.0:8002->8002/tcp   lausanne_backend
d54064b05de0   postgis/postgis:13-3.1                              "docker-entrypoint.s…"   About an hour ago   Up 26 minutes (healthy)        0.0.0.0:5432->5432/tcp   db
```

Il faut regler l'histoire de api, voir les boutons create post