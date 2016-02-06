# -*- coding: UTF-8 -*-
#
# Copyright 2010-2015 The pygit2 contributors
#
# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2,
# as published by the Free Software Foundation.
#
# In addition to the permissions in the GNU General Public License,
# the authors give you unlimited permission to link the compiled
# version of this file into combinations with other programs,
# and to distribute those combinations without any restriction
# coming from the use of this file.  (The General Public License
# restrictions do apply in other respects; for example, they cover
# modification of the file, and distribution when not linked into
# a combined executable.)
#
# This file is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING.  If not, write to
# the Free Software Foundation, 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301, USA.

"""Tests for revision walk."""

from __future__ import absolute_import
from __future__ import unicode_literals
import unittest

import pygit2
from . import utils


class StatusTest(utils.DirtyRepoTestCase):

    def test_status(self):
        """
        For every file in the status, check that the flags are correct.
        """
        git_status = self.repo.status()
        for filepath, status in git_status.items():
            self.assertTrue(filepath in git_status)
            self.assertEqual(status, git_status[filepath])


if __name__ == '__main__':
    unittest.main()
