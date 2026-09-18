#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Root Module
The API root.
	1. get_root(self) -> requests.Response
"""

import os
import unittest
from sasci360apidigitalassets import root


class TestRoot(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingDigitalAssets"
		encoding = "UTF-8"
		host = os.environ.get("SASCI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ["SASCI360_SECRET_KEY"]
		tenant_id = os.environ["SASCI360_TENANT_ID"]

		self.root = root.Root(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_root(self):
		"""
		1. get_root(self) -> requests.Response
		"""
		result = self.root.get_root()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
