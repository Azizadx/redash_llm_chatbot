## Local Redash Setup Using Docker

### Step 1: Create a `.env` File
- Copy the `.env.sample` file.
- Modify the values in the copied file to suit your local environment.
- Save it as `.env`.

### Step 2: Create the Database
Run the following command to create the database:
\```bash
docker-compose run --rm server create_db
\```

### Step 3: Build and Run Docker Compose
Build and run the Redash services using the following command:
\```bash
docker-compose up --build
\```

### Step 4: Access Redash
- Open your web browser.
- Navigate to `localhost:5000`.

### Reference
For more detailed configuration, refer to the official Redash Docker Compose file:
[Redash Docker Compose File on GitHub](https://github.com/getredash/setup/blob/master/data/docker-compose.yml)
