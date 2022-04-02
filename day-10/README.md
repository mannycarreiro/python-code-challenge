## Section 10 - Function with Outputs
<hr>

#### Simple Function
```python
def my_function(parameters):
# Do this
# Do that
# Do this with parameters
```
<br />

#### Function with Outputs
```python
def my_function():
    result = 3*2
    return result

# WHEN YOU CALL THE FUNCTION YOU CAN STORE THE RESULT VARIABLE TO ANOTHER VARIABLE
a = my_function()
# THE VALUE OF 'A' WILL BE 6
```
<br />

#### Docstrings
It's to specify what the function does and needs to be provided after the function is declared.

```python
def format_name(f_name, l_name):
    """ Take the first and last name and format it 
     to return the title case version of the name""" #DOC STRING
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}" # AFTER THIS LINE THIS IS THE END OF THE FUNCTION

```
