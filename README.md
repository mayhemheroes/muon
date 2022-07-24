# muon
A compact and **simple** object notation. µ[mju:] stands for "micro".

---

Muon has some interesting  properties (see [**presentation**](https://docs.google.com/presentation/d/1MosK6LTy_Rr32eF6HKej6UEtf9vBzdbeSF6YPb1_e4A/present) for more details):
- Every `UTF8` string is a valid `muon` object
- Uses gaps in the `UTF8` encoding space to encode things like `[` `]` `{` `}` etc.
- More compact than `JSON` (approx. 25%, depends on the object). On par/outperforms `CBOR`, `MsgPack`, `UBJSON`
- Unlimited size of objects and values
- Data is ready to be used in-place without pre-processing
- Supports raw binary values and typed arrays
- Mostly covers features of JSON and XML to minimize information loss during conversion to MUON

Future goals:
- Well-specified (little or no room for implementation-specific behavior / vendor-specific extensions)

## Muon structure

![alt tag](docs/muon.png?raw=true)

## Muon types

- Primitive:
  - **String**
  - **Typed**: integer and float numbers
  - **Special**: `True`, `False`, `Null`, `NaN`, `-Inf`, `+Inf`
- Composite:
  - **TypedArray** (a bunch of elements of the same type, possibly chunked)
  - **List** (sequence of arbitrary elements)
  - **Dict** (associative container of key-value pairs)
  - **Attr** (an dictionary that contains meta-information)

If you have any ideas or comments, please feel free to [post them here](https://github.com/vshymanskyy/muon/issues).
