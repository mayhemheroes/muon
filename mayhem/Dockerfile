FROM --platform=amd64 python:3.10-bullseye
RUN pip3 install atheris

COPY . /muon
WORKDIR /muon
RUN chmod +x fuzz/muon-fuzz.py

ENTRYPOINT [ ]
CMD ["/muon/fuzz/muon-fuzz.py"]