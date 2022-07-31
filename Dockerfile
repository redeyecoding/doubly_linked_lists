FROM python

WORKDIR /python_apps

COPY ./dll_constructor.py /python_apps

CMD ["python", "dll_constructor.py"]