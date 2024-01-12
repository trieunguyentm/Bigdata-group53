SPARK_VERSION="3.3.0"
JUPYTERLAB_VERSION="2.1.5"


docker build \
  -f cluster-base-ver.Dockerfile \
  -t cluster-base-ver .

docker build \
  --build-arg spark_version="${SPARK_VERSION}" \
  --build-arg jupyterlab_version="${JUPYTERLAB_VERSION}" \
  -f jupyterlab-ver.Dockerfile \
  -t jupyterlab-ver .