set -e

cd "$(dirname "$0")"

../.venv_my_proj/bin/mlflow server \
    --backend-store-uri sqlite:///mlruns.db \
    --default-artifact-root ./mlartifacts \
    --host 127.0.0.1 \
    --port 5000