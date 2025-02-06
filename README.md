# FastAPI Boilerplate

A boilerplate project for FastAPI applications.

## Getting Started

### Clone the Repository

First, clone the repository to your local machine:

```sh
git clone https://github.com/kimsengduong/fastapi-boilerplate.git
cd fastapi-boilerplate
```

### Setup Environment

You can set up the environment using either Conda or a virtual environment.

#### Using Conda

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) if you don't have it installed.
2. Create a new Conda environment:

   ```sh
   conda create --name aiser-authentication python=3.8
   ```

3. Activate the Conda environment:

   ```sh
   conda activate aiser-authentication
   ```

4. Install dependencies:

   ```sh
   pip install -e .
   pip install -r requirements.txt
   ```

#### Using Virtual Environment

1. Create a virtual environment:

   ```sh
   python -m venv venv
   ```

2. Activate the virtual environment:

   ```sh
   # On Linux or macOS
   source venv/bin/activate

   # On Windows
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```sh
   pip install -e .
   pip install -r requirements.txt
   ```

### Start the Server

To start the FastAPI server, run:

```sh
fastrun start
```

### Database Migrations

#### Create a New Migration

To create a new database migration, run:

```sh
fastrun db revision -m "message"
```

#### Apply Migrations

To apply the migrations, run:

```sh
fastrun db upgrade
```

#### Rollback Migrations

To rollback migrations, run:

```sh
fastrun db downgrade "revision_id"
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
