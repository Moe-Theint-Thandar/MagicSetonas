apibrėžti foo():
    '>>> spausdinti("docstring")'
apibrėžti foo():
    ">>> spausdinti('docstring')"



apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.single.python
>>> spausdinti("docstring") : source.python, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.docstring.single.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
"             : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.single.python
>>> spausdinti('docstring') : source.python, string.quoted.docstring.single.python
"             : punctuation.definition.string.end.python, source.python, string.quoted.docstring.single.python
