# fastapi-boilerplate

FastAPI boilerplate

#### Clone repository

```
git clone https://github.com/kimsengduong/fastapi-boilerplate.git
```

#### Virtual Environment

```
python -m venv venv
```

#### Active virtual environment

```
## Linux
source venv/bin/active

## Windows
venv\Scripts\activate
```

#### Install dependencies

```
pip install -e .
pip install -r requirements.txt
```

#### Start server

```
fastrun start
```

#### DB revision

```
fastrun db revision -m "message"
```

#### DB upgrade

```
fastrun db upgrade
```

#### DB downgrade

```
fastrun db downgrade "revision_id"
```
