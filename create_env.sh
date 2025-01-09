# Creates a python environment with default bindings

python -m venv env
# tensorrt
cp -r /usr/lib/python3.10/dist-packages/tensorrt env/lib/python3.10/site-packages/
cp -r /usr/lib/python3.10/dist-packages/tensorrt-10.3.0.dist-info env/lib/python3.10/site-packages/
cp -r /usr/lib/python3.10/dist-packages/tensorrt_dispatch env/lib/python3.10/site-packages/
cp -r /usr/lib/python3.10/dist-packages/tensorrt_dispatch-10.3.0.dist-info env/lib/python3.10/site-packages/
cp -r /usr/lib/python3.10/dist-packages/tensorrt_lean env/lib/python3.10/site-packages/
cp -r /usr/lib/python3.10/dist-packages/tensorrt_lean-10.3.0.dist-info env/lib/python3.10/site-packages/
# Nvidia Jetson's torch
cp -r ~/.local/lib/python3.10/site-packages/* env/lib/python3.10/site-packages/

# install necessary packages
pip install -U openai-whisper
pip install psutil