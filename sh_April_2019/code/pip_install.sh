python3 -m venv  .venv3
source .venv3/bin/activate
pip install -U pip
pip install sh
pip install ipython jupyter
echo "import sh" >| hw.py
echo "print(sh.echo('Hello, World!'))" >> hw.py
python hw.py
