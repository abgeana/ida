# alegen-ida

My collection of IDA Pro plugins and scripts.

## IDA API snippets

These are some generic snippets to avoid me Googling all the time.

### Get references to address

```python
import idautils

for xref in idautils.XrefsTo(ScreenEA(), 0):
    print hex(xref.frm)
```

### Insert comments

* comments are made repeatable using the third argument

```python
import idc

idc.set_cmt(ScreenEA(), 'comment goes here', rptble=1) -> bool
```
