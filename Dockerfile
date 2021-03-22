FROM python:3

ADD . .

CMD ["python", "-m", "unittest", "discover", "-s","tests", "tests/test_data"]