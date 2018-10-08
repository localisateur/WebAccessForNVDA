# globalPlugins/webAccess/store/addons.py
# -*- coding: utf-8 -*-

# This file is part of Web Access for NVDA.
# Copyright (C) 2015-2018 Accessolutions (http://accessolutions.fr)
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
#
# See the file COPYING.txt at the root of this distribution for more details.

"""Web Access addons data store."""

__version__ = "2017.12.06"

__author__ = "Julien Cochuyt <j.cochuyt@accessolutions.fr>"


import addonHandler

from . import DispatchStore
from . import Store


class AddonsStore(DispatchStore):
	
	def __init__(self, *args, **kwargs):
		if not "name" in kwargs:
			kwargs["name"] = "addons"
		self.addonStoreFactory = kwargs["addonStoreFactory"]
		super(AddonsStore, self).__init__(*args, **kwargs)

	def __getStores(self):
		for addon in addonHandler.getAvailableAddons():
			# Introduced in NVDA 2016.3
			if hasattr(addon, "isDisabled") and addon.isDisabled:
				continue
			yield self.addonStoreFactory(addon)
	
	stores = property(__getStores)
	
	# Defaults to read-only.
	delete = Store.delete
	supports = Store.supports		
	update = Store.update
	
	