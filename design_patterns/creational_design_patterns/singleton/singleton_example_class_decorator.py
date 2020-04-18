"""
Source code comes from - https://medium.com/better-programming/singleton-in-python-5eaa66618e3d

Small modifications where applied.
"""


class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


@Singleton
class FileConnection():

    def __init__(self, file_name):
        """Open a file."""
        self._file_name = file_name
        self._handler = open(self._file_name)
        self._active = True

    def __str__(self):
        return '{0} is active: {1}'.format(self._file_name, self._active)

    def close_file(self):
        self._active = False
        self._handler.close()

    def get_handler(self):
        return self._handler

c1 = FileConnection('test.txt')
print(FileConnection.instance())
c2 = FileConnection('test.txt')
print(FileConnection.instance())

print("Id of c1 : {}".format(str(id(c1))))
print("Id of c2 : {}".format(str(id(c1))))

print("c1 is c2 ? " + str(c1 is c2))


