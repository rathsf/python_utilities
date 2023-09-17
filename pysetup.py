import setuptools

package_dir = input("Enter package url: ")
module_name = input("Enter module name: ")
#package_dir = input("Enter package dir: ")


setuptools.setup(
    url         = package_dir,
    #package_dir = {'': package_dir},
    name        = module_name, 
    py_modules  = [module_name],
)