# test

## run 

### general 

```shell script
# run from project root:
python3 -m pip install --user -e .[testing] --no-cache-dir
python3 -m pytest
```

### via docker 
```shell script
# run from project root:
docker run -it --rm --name nichtparasoup -v \
  "$PWD":/usr/src/nichtparasoup -w /usr/src/nichtparasoup \
  python:3.4 bash -c \
  'python --version; pip install -e .[testing] --no-cache-dir && python -m pytest'
```

## contribution 

stick to these rules:

* add your tests somewhere in this dir
* write the test - use `unittest` or simply `assert`
* name the test file `*_test.py`
* name the test functions `test_*`
* name call the test classes `*Test`
