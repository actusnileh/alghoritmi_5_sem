DC = docker compose
FRONTEND_FILE = docker_compose/frontend.yaml
BACKEND_FILE = docker_compose/backend.yaml

.PHONY: all
all:
	${DC} -f ${FRONTEND_FILE} up --build -d
	${DC} -f ${BACKEND_FILE} up --build -d

.PHONY: back
back:
	${DC} -f ${BACKEND_FILE} up --build -d

.PHONY: drop-back
drop-back:
	${DC} -f ${BACKEND_FILE} down

.PHONY: logs-back
logs-back:
	${DC} -f ${BACKEND_FILE} logs -f

.PHONY: front
front:
	${DC} -f ${FRONTEND_FILE} up --build -d

.PHONY: drop-front
drop-front:
	${DC} -f ${FRONTEND_FILE} down

.PHONY: logs
logs:
	${DC} -f ${FRONTEND_FILE} -f ${BACKEND_FILE} logs -f

.PHONY: drop-all
drop-all:
	${DC} -f ${FRONTEND_FILE} -f ${BACKEND_FILE} down