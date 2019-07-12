
class Contact:
    all_contacts = []

    def __init__(self, name='', email='', **kw):
        print("contact ",kw)
        #super().__init__(**kw)
        self.name = name
        self.email = email
        print("con init")
    def __del__(self):
        print("del ",self.name)

class AddressHolder:

    def __init__(self, street = '', city='', state='', code='', **kw):
        print(kw)
        kw.update(dict(city=city))
        super().__init__(**kw)
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        print("add init",kw['yy'],kw['phone'])
    def __del__(self):
        print("del ",self.code)

class Friend(AddressHolder,Contact):

    def __init__(self, phone='', **kw):
        print("xx", kw['yy'])
        print(kw)
        kw['phone']=phone
        super().__init__(**kw)
        self.phone= phone
        print("fr init ")
    def __call__(self, phone):
        print("call ",phone)

    def __del__(self):
        super().__del__()
        print("del ",self.phone)


if __name__ == "__main__":

    tf1 = Friend( street="astree",phone="123", city="bcity", yy=333,state="cstate", code="zip", name="dname", email="e@f.com")
    tf1(444)
    del(tf1)
