# testing annotations split over multiple lines
apibrėžti foo(a:('abc' 'apibrėžti')==123, boo: 'abc'

                         'apibrėžti' == foo(n(m=0)))



#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 testing annotations split over multiple lines : comment.line.number-sign.python, source.python
apibrėžti     : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
a             : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.parenthesis.begin.python, source.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
abc           : meta.function.parameters.python, meta.function.python, source.python, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : meta.function.parameters.python, meta.function.python, source.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
apibrėžti     : meta.function.parameters.python, meta.function.python, source.python, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
)             : meta.function.parameters.python, meta.function.python, punctuation.parenthesis.end.python, source.python
==            : keyword.operator.comparison.python, meta.function.parameters.python, meta.function.python, source.python
123           : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
boo           : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
abc           : meta.function.parameters.python, meta.function.python, source.python, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : meta.function.parameters.python, meta.function.python, source.python
                          : meta.function.parameters.python, meta.function.python, source.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.python, string.quoted.single.python
apibrėžti     : meta.function.parameters.python, meta.function.python, source.python, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.python, string.quoted.single.python
              : meta.function.parameters.python, meta.function.python, source.python
==            : keyword.operator.comparison.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
foo           : meta.function-call.generic.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python
(             : meta.function-call.python, meta.function.parameters.python, meta.function.python, punctuation.definition.arguments.begin.python, source.python
n             : meta.function-call.arguments.python, meta.function-call.generic.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python
(             : meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, punctuation.definition.arguments.begin.python, source.python
m             : meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.python
)             : meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, punctuation.definition.arguments.end.python, source.python
)             : meta.function-call.python, meta.function.parameters.python, meta.function.python, punctuation.definition.arguments.end.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
