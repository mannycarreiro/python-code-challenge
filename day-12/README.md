## Section 12 - Namespaces: Local vs Global Scope
<hr>

#### Local Scope

```python
def drink_portion():
    potion_strength = 2
    print(potion_strength)

drink_portion()
print(potion_strength) # THIS WILL THROW AN ERROR BECAUSE POTION STRENGTH IS ONLY AVAILABLE INSIDE THE FUNCTION

```
<br />

#### Global Scope
```python
player_health = 10 # This is defined at the top level of the file, hence is a global scope variable

def drink_portion():
    potion_strength = 2
    print(potion_strength)


```
<br />

#### Modifying Global Scope
```python
enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function {enemies}")

increase_enemies() # THIS WILL PRINT 2
print(f"enemies outside function {enemies}") # THIS WILL PRINT 1

# ===== TO ACCESS enemies LOCAL VARIABLE:
enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function {enemies}")

increase_enemies() # THIS WILL PRINT 2 (1 + 1)
print(f"enemies outside function {enemies}") # THIS WILL PRINT 1


```
