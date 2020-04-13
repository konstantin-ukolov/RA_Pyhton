import os
import re
import subprocess

from abc import abstractmethod


class AbstractPackageProcessor(object):
    def __init__(self):
        self._packages = list()

    def append_packages_from_path(self, path):
        for name in os.listdir(path):
            package = os.path.join(path, name)

            if name.endswith(self._extension()) and os.path.isfile(package):
                self._packages.append(package)

    def process_all(self):
        for package in self._packages:
            self._rename_package_file(package)

    def _rename_package_file(self, original):
        info = self._package_info(original)

        result = os.path.join(
            os.path.dirname(original),
            self._name_format().format(**info)
        )

        os.rename(original, result)

        print('Package {} renamed to {}').format(
            os.path.basename(original),
            os.path.basename(result)
        )

    @abstractmethod
    def _extension(self):
        pass

    @abstractmethod
    def _name_format(self):
        pass

    @abstractmethod
    def _package_info(self, package):
        pass


class DebianPackageProcessor(AbstractPackageProcessor):
    def __init__(self):
        super(DebianPackageProcessor, self).__init__()

    def _extension(self):
        return 'deb'

    def _name_format(self):
        return '{Package}-{Version}-{Architecture}.deb'

    def _package_info(self, package):
        info_string = subprocess.check_output(['dpkg', '--info', package])
        return dict(re.findall(r' (\w+): (.+)\n', info_string))


class RedhatPackageProcessor(AbstractPackageProcessor):
    def __init__(self):
        super(RedhatPackageProcessor, self).__init__()

    def _extension(self):
        return 'rpm'

    def _name_format(self):
        return '{Name}-{Version}-{Architecture}.rpm'

    def _package_info(self, package):
        info_string = subprocess.check_output(['rpm', '-qip', package])
        return dict(re.findall(r'(\w+\s*\w+)\s*: (.+)\n', info_string))


PLATFORM = 'debian'
INSTALL_PATH = '~/install/path/'

if __name__ == '__main__':
    platform_processors = {
        'debian': DebianPackageProcessor,
        'redhat': RedhatPackageProcessor,
    }

    package_processor = platform_processors[PLATFORM]()
    package_processor.append_packages_from_path(INSTALL_PATH)
    package_processor.process_all()

