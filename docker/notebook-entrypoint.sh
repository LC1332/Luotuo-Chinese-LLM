#!/usr/bin/env bash
umask 000

WORK_DIR=/workspace
JUPYTER_CONFIG="$WORK_DIR/.jupyter/jupyter_lab_config.py"

cd $WORK_DIR

[[ ! -d "$XDG_CACHE_HOME" ]] && mkdir -p $XDG_CACHE_HOME

if [[ ! -f "$HOME/.pip_env.ok" ]]; then
    set -e
    if [ -z "$http_proxy" ]; then
        if [ -n "$PYPI_MIRROR" ]; then
            pip3 config set global.index-url $PYPI_MIRROR
        else
            pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
        fi
    fi
    pip3 install jupyterlab bitsandbytes datasets loralib sentencepiece gradio
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    pip3 install git+https://github.com/huggingface/transformers.git
    pip3 install git+https://github.com/huggingface/peft.git
    set +e
    touch $HOME/.pip_env.ok
fi

if [[ ! -f "$JUPYTER_CONFIG" ]]; then
    jupyter lab --generate-config
fi

jupyter-lab --allow-root --ip=$JUPYTER_IP --port=$JUPYTER_PORT
