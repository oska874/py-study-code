
class Contact:
    all_contacts = []

    def __init__(self, name='', email='', **kw):
        print("contact ",kw)
        #super().__init__(**kw)
        self.name = name
        self.email = email
        print("con init")


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


class Friend(AddressHolder,Contact):

    def __init__(self, phone='', **kw):
        print("xx", kw['yy'])
        print(kw)
        kw['phone']=phone
        super().__init__(**kw)
        self.phone= phone
        print("fr init ")


if __name__ == "__main__":

    tf1 = Friend( street="astree",phone="123", city="bcity", yy=333,state="cstate", code="zip", name="dname", email="e@f.com")
