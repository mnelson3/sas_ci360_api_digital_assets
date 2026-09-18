#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Properties File Module
Contains operations to upload standard properties and custom properties for digital assets.
	1. create_properties_file(self, payload: dict) -> requests.Response
	2. get_properties_file(self, attribute_file_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apidigitalassets import properties_file


class TestPropertiesFile(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingDigitalAssets"
		encoding = "UTF-8"
		host = os.environ.get("SASCI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ["SASCI360_SECRET_KEY"]
		tenant_id = os.environ["SASCI360_TENANT_ID"]

		self.properties_file = properties_file.PropertiesFile(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_create_properties_file(self):
		payload = ["string"]
		result = self.properties_file.create_properties_file(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_properties_file(self):
		attribute_file_id = "0"
		result = self.properties_file.get_properties_file(attribute_file_id=attribute_file_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
