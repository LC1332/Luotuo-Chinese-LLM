#!/usr/bin/env bash

WORK_DIR=/workspace/

if [ ! -n "$http_proxy" ]; then
    if [ -n "$PYPI_MIRROR" ]; then
        pip3 config set global.index-url $PYPI_MIRROR
    else
        pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
    fi
fi

if [[ ! -f "$HOME/.pip_env.ok" ]]; then
    pip3 install jupyterlab bitsandbytes datasets loralib sentencepiece &&\
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 &&\
    pip3 install git+https://github.com/zphang/transformers@c3dc391 &&\
    pip3 install git+https://github.com/huggingface/peft.git &&\
    touch $HOME/.pip_env.ok
fi

if [[ ! -f "$HOME/.jupyter/jupyter_lab_config.py" ]]; then
    jupyter lab --generate-config
fi

jupyter-lab --allow-root --ip=$JUPYTER_IP --port=$JUPYTER_PORT