def lazy_property(func):
    attr_name = "_lazy_" + func.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self))
        return getattr(self, attr_name)

    return _lazy_property

class Circle(object):
  def __init__(self, radius):
    self.radius = radius

  @lazy_property
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

