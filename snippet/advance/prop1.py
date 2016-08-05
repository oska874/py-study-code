
class lazy(object):
  def __init__(self, func):
    self.func = func

  def __get__(self, instance, cls):
    val = self.func(instance)
    setattr(instance, self.func.__name__, val)
    return val

class Circle(object):
  def __init__(self, radius):
    self.radius = radius

  @lazy
#  @property
  def area(self):
    print 'evalute'
    return 3.14 * self.radius ** 2
c = Circle(4)
print c.radius
print c.area
c.radius = 10
print c.radius
print c.area
print c.area

