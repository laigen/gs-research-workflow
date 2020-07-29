1) mkdir /tmp/laigen
2) upload gs-framework / gs-research-workflow to /tmp/laigen
3) apt-get install -y python3 python3-venv python3-pip
4) mkdir ~/.pyenv
5) python3 -m venv ~/.pyenv/gs-laigen
6) source ~/.pyenv/gs-laigen/bin/activate
7) pip install pip --upgrade -i https://mirrors.aliyun.com/pypi/simple/
8) cd /tmp/laigen
9) pip install -e gs-framework -i https://mirrors.aliyun.com/pypi/simple/
10) pip install -e gs-research-workflow -i https://mirrors.aliyun.com/pypi/simple/
11) cd ~/.cache
    rm -r pip