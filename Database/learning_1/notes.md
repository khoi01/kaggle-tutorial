
### run scipt to create table 
docker-compose exec flask_app python scripts/init_db.py
### Seed User Data into Table User
docker-compose exec flask_app python scripts/seed_user.py
### enter database postgres on container
docker-compose exec db bash
### Login to database
psql -U myuser -d mydb
### Command
\dt              -- list tables
SELECT * FROM users;
\q               -- quit

