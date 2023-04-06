FROM alpine:latest AS res

RUN apk -U --no-cache update \
    && apk -U --no-cache --allow-untrusted add dos2unix

COPY ./notebook-entrypoint.sh /workspace/entrypoint.sh

RUN dos2unix /workspace/entrypoint.sh \
    && chmod +x /workspace/entrypoint.sh

FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

ENV XDG_CACHE_HOME=/workspace/.cache \
    HF_DATASETS_CACHE=/workspace/.cache/huggingface/datasets \
    TRANSFORMERS_CACHE=/workspace/.cache/huggingface/transformers \
    JUPYTERLAB_SETTINGS_DIR=/workspace/.jupyter/lab/user-settings

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install curl wget build-essential python3 python3-pip git vim -y \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && curl -fsSL https://install.python-poetry.org | python - \
    && ln -s /$HOME/.local/bin/poetry /usr/bin \
    && poetry config virtualenvs.in-project true

COPY --from=res /workspace/entrypoint.sh /entrypoint.sh

WORKDIR /workspace

ENTRYPOINT ["/entrypoint.sh"]
