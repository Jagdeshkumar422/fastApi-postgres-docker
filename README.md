# FastAPI CRUD with PostgreSQL & Docker

## How to Run

1. Clone the repo and navigate into the directory:
   ```sh
   git clone <repo-url>
   cd fastapi-crud
   ```

2. Start the services using Docker:
   ```sh
   docker-compose up --build
   ```
For run the code->   uvicorn app.main:app --reload

3. Access the API at: [http://localhost:8000](http://localhost:8000)

4. Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

Access the graphql api's on port: [http://127.0.0.1:8000/graphql]
