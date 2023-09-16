import setuptools

module_name = input("Enter module name: ")
setuptools.setup(
    name=module_name,
    py_modules=[module_name],
)