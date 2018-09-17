
class BasicFormatItem(object):
    """docstring for BasicFormatItem."""

    FORMATS = ['plain', 'short']

    def __init__(self, **kwargs):
        self.values = {}
        self._format = kwargs.get('format', self.FORMATS[0])

        if hasattr(self, 'KEYS'):
            for key, value in kwargs.items():
                if key in self.KEYS:
                    self.values[key] = value

    def __getitem__(self, key):
        return self.values.get(key, False)

    def __str__(self):
        return self.show()

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        if value in self.FORMATS:
            self._format = value

    def show(self):
        return '!Not implemented!'


class Person(BasicFormatItem):
    """docstring for Person."""

    KEYS = ['name', 'lastname', 'email', 'description']

    def show(self):
        if self.format == 'table':
            return 'name: {} {}'.format(self['name'], self['lastname'])
        return 'name: {} {}\nemail: {}'.format(self['name'], self['lastname'], self['email'])


class Project(BasicFormatItem):
    """docstring for Project."""

    KEYS = ['name', 'description', 'url']

    def show(self):
        text = 'name: {}\n{}\n'.format(self['name'],self['description'])
        if self['url']:
            text += 'url: {}\n'.format(self['url'])
        text += '\n'
        return text


class Resume(BasicFormatItem):
    """The bases for your resume"""

    def __init__(self, **kwargs):
        super(Resume, self).__init__(**kwargs)
        self.__update_format(self.format)

    @BasicFormatItem.format.setter
    def format(self, value):
        if value in self.FORMATS:
            self._format = value
        self.__update_format(value)

    def __update_format(self, format):
        for key, value in dict(self.__class__.__dict__).items():
            if issubclass(value.__class__, BasicFormatItem):
                value.format = format

    def __get_attr(self, cls, as_list=False):
        """Return all attributes with the class cls. If as_listist true, it
        returns a list. On false it returns the first item.
        """
        items = []
        for key, value in dict(self.__class__.__dict__).items():
            if type(value) == cls:
                items.append(value)
                if not as_list: return value
        if as_list:
            return items
        return None

    def show(self):
        if self.format == 'table':
            pass

        person = self.__get_attr(Person)
        projects = self.__get_attr(Project, True)

        text = 'About the person\n\n{}\n\n'.format(person)

        if projects:
            text += '\nMy projects:\n\n'
        for project in projects:
            text += str(project)

        return text
