# check pyenv
if ! command -v pyenv &> /dev/null
then
    echo "pyenv could not be found"
    exit 1
fi

# 
poetry config virtualenvs.in-project true

# setup commands
echo "######## start setup ########"

pyenv install $PYVERSION

pyenv local $PYVERSION

poetry env use $PYVERSION

poetry install

call poetry shell

oj login -u $UNAME -p $PASSWD "https://atcoder.jp/"


echo "######## end setup ########"

exit 0