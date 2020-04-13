# -*- coding: utf-8 -*-

import os
import sys

from configparser import ConfigParser


class ApplicationSettings(object):
    _organization_name = 'Organization'
    _config_file_name = 'Application.conf'

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        self._config = ConfigParser()

        if not os.path.exists(self._local_config_path()):
            self._create_default_local_config()

        self._config.read(self._local_config_path())

    @property
    def mail_server_host(self):
        return self._get_value('Email', 'server_host')

    @property
    def mail_server_port(self):
        return self._get_value('Email', 'server_port')

    @property
    def email_login(self):
        return self._get_value('Email', 'login')

    @property
    def email_password(self):
        return self._get_value('Email', 'password')

    @property
    def vk_login(self):
        return self._get_value('VK', 'login')

    @property
    def vk_password(self):
        return self._get_value('VK', 'password')

    @property
    def senders(self):
        return self._get_value('Application', 'senders')

    def _create_default_local_config(self):
        self._config['Email'] = {}
        self._config['Email']['server_host'] = str()
        self._config['Email']['server_port'] = str()
        self._config['Email']['login'] = str()
        self._config['Email']['password'] = str()

        self._config['VK'] = {}
        self._config['VK']['login'] = str()
        self._config['VK']['password'] = str()

        self._config['Application'] = {}
        self._config['Application']['senders'] = str()

        path = self._local_config_path()
        basedir = os.path.dirname(path)

        if not os.path.exists(basedir):
            os.makedirs(basedir)

        with open(path, 'w') as config_file:
            self._config.write(config_file)

    def _get_value(self, section, key):
        try:
            return self._config[section][key]
        except KeyError:
            print('Invalid application settings file')
            sys.exit(1)

    @staticmethod
    def _home_directory():
        return os.path.expanduser('~')

    @classmethod
    def _local_config_path(cls):
        return os.path.join(
            cls._home_directory(),
            '.config',
            cls._organization_name,
            cls._config_file_name
        )


application_settings = ApplicationSettings()
