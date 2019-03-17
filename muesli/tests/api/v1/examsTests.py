# -*- coding: utf-8 -*-
#
# muesli/tests/api/v1/examTests.py
#
# This file is part of MUESLI.
#
# Copyright (C) 2018, Philipp Göldner  <goeldner (at) stud.uni-heidelberg.de>
#                     Christian Heusel <christian (at) heusel.eu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from muesli.tests import functionalTests
from muesli.tests.api.v1 import URL, TESTUSERS, STATIC_HEADERS
from muesli.tests.api.v1.utilities import authenticate_testapp

import muesli.models


class BaseTests(functionalTests.BaseTests):
    def test_exam_get(self):
        self.testapp.get(URL+'/exams/13415', headers=STATIC_HEADERS, status=403)

class UserLoggedInTests(functionalTests.PopulatedTests):
    def setUp(self):
        functionalTests.PopulatedTests.setUp(self)
        self.api_token = authenticate_testapp(
            self.testapp, TESTUSERS["tutor@muesli.org"]
        )

    def test_tutorial_get(self):
        self.testapp.get(URL+'/exams/13415', headers=self.api_token, status=200)