# to enhance compatibility with sensitive systems, replace 'c = printable[:90]' with the following snippet, which appends special symbols. Limit the use of these symbols to within base82.
c = ''.join([x for x in string.printable[:90] if x not in '/\\`"\',_']) + '/\\`"\',_'
