#-*- coding: utf-8 -*-
'''
Exceptions for {{ cookiecutter.project_name }}.

'''


class ConfigurationError(Exception):
    pass


# not used in the template - delete if not required.
class ApplicationError(Exception):
    '''Base class for errors in the application logic.'''
    pass
