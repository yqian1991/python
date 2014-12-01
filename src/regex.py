import re
 
numbers = [ "123 555 6789",
            "1-(123)-555-6789",
            "(123-555-6789",
            "(123).555.6789",
            "123 55 6789" ]
 
for number in numbers:
    pattern = re.match(r'^'
                    r'(1[-\s.])?'        # optional '1-', '1.' or '1'
                    r'(<span class="MathJax_Preview">\()?'             # optional opening parenthesis
                    r'\d{3}'             # the area code
                    r'(?(2)\)</span><script type="math/tex">)?'             # optional opening parenthesis
                    r'\d{3}'             # the area code
                    r'(?(2)</script>)'          # if there was opening parenthesis, close it
                    r'[-\s.]?'           # followed by '-' or '.' or space
                    r'\d{3}'             # first 3 digits
                    r'[-\s.]?'           # followed by '-' or '.' or space
                    r'\d{4}$', number, re.DEBUG)  # last 4 digits
 
    if pattern:
        print '{0} is valid'.format(number)
    else:
        print '{0} is not valid'.format(number)