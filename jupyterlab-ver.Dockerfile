FROM cluster-base-ver

# -- Layer: JupyterLab

ARG spark_version=3.4.0
ARG jupyterlab_version=4.0.2

RUN apt-get update -y && \
    apt-get upgrade -y  && \
    apt-get install -y python3-pip && \
    pip3 install wget pyspark==3.3.0 jupyterlab==2.1.5

# -- Runtime

EXPOSE 8888
WORKDIR ${SHARED_WORKSPACE}
CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=