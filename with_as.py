class A:
    def __init__(self, name):
        print('init')
        self._name = name

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'exc_type : {exc_type}\nexc_val : {exc_val}\nexc_tb : {exc_tb}')
        print('exit')
        pass

    @property
    def name(self):
        massege = f'Hello {self._name}'
        return massege


with A('king') as a:
    print(a.age)
