# test

## run 

tests are run via tox.

### general 

```shell script
# run from project root:
pip install tox
python -m tox -e py3
```

### via docker 
```shell script
# run from project root:
docker run \
  --name nichtparasoup-testing \
  -v "$PWD":/usr/src/nichtparasoup \
  -w /usr/src/nichtparasoup \
  -it --rm \
  python:3.4 bash -c \
  'pip install tox; python -m tox -e py3'
```

## reports 

* after running, a report will be shown
* for coverage report see `python -m coverage`

## contribution 

stick to these rules:

* add your tests somewhere in this dir
* write the test - use `unittest` or simply `assert`
* name the test file `*_test.py`
* name the test functions `test_*`
* name call the test classes `*Test`
