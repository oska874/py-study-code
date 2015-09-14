import mod2
import package_import_test.pm0
x=33
print(mod2.mod1.x)
print(mod2.x)
print(x)
mod2.mod1.x=3

print(mod2.mod1.x)
print(mod2.x)
print(x)

reload( mod2)
print(mod2.mod1.x)
print(mod2.x)
print(x)

print(package_import_test.pm0.mod_p0)
package_import_test.pm0.mod_p0=12
print(package_import_test.pm0.mod_p0)