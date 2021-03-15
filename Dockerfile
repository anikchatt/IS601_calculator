FROM python:3

ADD src tests /src /tests

CMD ["python", "./src/calculator.py", "./tests/test_calculator.py" ]