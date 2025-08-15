# SysAcad

Proyecto Django listo para desarrollo rápido. Funciona **con SQLite por defecto** y **opcionalmente con PostgreSQL**.

---

## Requisitos

- Python 3.10+
- PostgreSQL (opcional, solo si querés usarla)
- Git

---

## Pasos rápidos de instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPO>
cd <NOMBRE_DEL_REPO>
```

### 2. Crear y activar entorno virtual

```bash
python -m venv env
# Linux / Mac
source env/bin/activate
# Windows
env\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Migrar la base de datos

- **Con SQLite** (desarrollo rápido, por defecto):

```bash
python manage.py migrate
```

- **Con PostgreSQL** (opcional):

```bash
export USE_POSTGRES=1
export DB_NAME=sysacad_db
export DB_USER=tu_usuario
export DB_PASSWORD=tu_contraseña
export DB_HOST=localhost
export DJANGO_SECRET_KEY=una_clave_random
export DJANGO_DEBUG=True

python manage.py migrate
```

> En Windows: usar `set` (cmd) o `$env:` (PowerShell) en lugar de `export`.

### 5. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 6. Levantar servidor

```bash
python manage.py runserver
```

### 7. Abrir navegador

```
http://127.0.0.1:8000/
```

---

## Notas

- **SQLite** es suficiente para desarrollo y pruebas rápidas.
- **PostgreSQL** es opcional y útil si querés trabajar con la misma DB que usarías en producción.
- No hay que tocar `settings.py` para desarrollo con SQLite.
- `.gitignore` evita subir entornos virtuales y archivos sensibles.
- Cada vez que cambies de base de datos (nueva SQLite o PostgreSQL) hay que correr `migrate`.

---

## Flujo completo desde cero

```bash
git clone https://github.com/Kurse12/Sysacad.git
cd Sysacad
python -m venv env
source env/bin/activate  # o env\Scripts\activate en Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # opcional
python manage.py runserver
```

> Solo SQLite por defecto, listo para usar. Para PostgreSQL, definir variables de entorno antes de `migrate` y `runserver`.

