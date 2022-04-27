from os import environ

environ.setdefault("PYTHON_DEFAULT", "Python Default")

print(f"Value of 'MUST_BE_SET': '{environ['MUST_BE_SET']}'")
print(f"Value of 'PYTHON_DEFAULT': '{environ['PYTHON_DEFAULT']}'")

try:
    print(f"Value of 'ALWAYS_OVERRIDDEN' before override: '{environ['ALWAYS_OVERRIDDEN']}'")
except KeyError:
    print("'ALWAYS_OVERRIDDEN' was not set.")

environ["ALWAYS_OVERRIDDEN"] = "Always Overridden In Python"

print(f"Value of 'ALWAYS_OVERRIDDEN' after override: '{environ['ALWAYS_OVERRIDDEN']}'")
print(f"Value of 'OPTIONAL': '{environ.get('OPTIONAL')}'")