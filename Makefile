up:
	docker compose -f ./docker-compose.yaml up -d

down: 
	docker compose -f ./docker-compose.yaml down

re-build: 
	docker compose -f ./docker/docker-compose.yaml build ${SERVICE}
