#!/usr/local/bin/python3
import atheris
import sys
import io
import os
import json
from json import JSONDecodeError

sys.path.append( '../muon_py' )

with atheris.instrument_imports():
    import muon 

@atheris.instrument_func
def TestOneInput(data):
    if len(data) > 1:
        fdp = atheris.FuzzedDataProvider(data)
        try:
            data = json.loads(fdp.ConsumeUnicode(len(data)))
            d = muon.DictBuilder()
            d.add(data)
            t = d.get_dict(512)
            b = bytes()

            with io.BytesIO(b) as f:
                m = muon.Writer(f)
                if len(t) > 128:
                    m.add_lru_list(reversed(t))
                elif len(t):
                    m.add_lru_dynamic(t)
                m.add(d)
                
        except JSONDecodeError:
            pass

atheris.Setup(sys.argv, TestOneInput)
atheris.instrument_all()
atheris.Fuzz()