# -*- mode: python -*-

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
---
module: remove_host
short_description: remove a host from the ansible-playbook in-memory inventory
description:
  - Remove a host by name in from inventory (and groups), it will be completely
    absent in later plays of the same playbook.
version_added: "2.3"
options:
  name:
    description:
    - The hostname of the host to remove from the inventory.
    required: true
notes:
    - This module bypasses the play host loop and only runs once for all the hosts in the play, if you need it
      to iterate use a with\_ directive.
author:
    - "James Pic"
'''

EXAMPLES = '''
# remove host 'foo'
- add_host:
    name: foo
'''
