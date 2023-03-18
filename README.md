# dash-plotly-traning

Ce projet est un projet de training sur l'apprentissage de `dash Plotly` 

## Structuration du projet

Ce projet adopte une structure en module .

## Les modules du projet

Vous avez ici une liste des modules actuel du projet:

`modules/maestros`
`modules/morritz`
`modules/rushclin`

## le dossier de deployment
Ici vous avez la description de toute l'architecture de deployment adopee

# Les docker-compose file de chaque modules

`deployment/docker/docker-compose.maestros.yml`
`deployment/docker/docker-compose.morritz.yml`
`deployment/docker/docker-compose.rushclin.yml`

# les fichier d'execution de chaque conteneur associes
`deployment/docker/maestros.run.sh`
`deployment/docker/morritz.run.sh`
`deployment/docker/rushclin.run.sh`

## Les pre-requis

Vous devez avoir les elements suvant installes sur votre system:
    `docker` `docker-compose` et c'est tout !
    
## Démarrer le projet
Tout le projet en entierement dockerize, et chaque module possede sont conteneur docker qui tourne sur un port
definit dans de .yml correspondant.

Veuillez suivre les étapes suivantes pour démarrer ce projet en local

[1] Vous souhaitez demarrer uniquement le projet du module `maestros`:
    A la racine du projet executer la commande:
    `sh maestros-docker-run.sh`
[2] Vous souhaitez demarrer uniquement le projet du module `morritz`:
    A la racine du projet executer la commande:
    `sh morritz-docker-run.sh`

[3] Vous souhaitez demarrer uniquement le projet du module `rushclin`:
    A la racine du projet executer la commande:
    `sh rushclin-docker-run.sh`





