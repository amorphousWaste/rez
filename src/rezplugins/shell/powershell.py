"""Windows PowerShell 5"""

from rez.shells import Shell
from rez.utils.platform_ import platform_
from .powershell_common.powershell_base import PowerShellBase


class PowerShell(PowerShellBase):

    @property
    def executable(cls):
        if cls._executable is None:
            cls._executable = Shell.find_executable('powershell')
        return cls._executable

    @classmethod
    def name(cls):
        return 'powershell'

    @classmethod
    def file_extension(cls):
        return 'ps1'


def register_plugin():
    if platform_.name == "windows":
        return PowerShell


# Copyright 2013-2016 Allan Johns.
#
# This library is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library.  If not, see <http://www.gnu.org/licenses/>.
