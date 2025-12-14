# Sorter
The project serves as a learning platform for mastering: PostgreSQL + Alembic (migration), authentication (JWT), file processing, query optimization (N+1, indexes), containerization (Docker), automated testing, CI/CD with non-warming protection without tests.


We need to enter a command without a space for Ubuntu (24) with the Docker Engine installed.
  docker compose up -d
  docker compose down -v or docker compose down

  uvicorn src.main:app --reload
