#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Renditions Module
Contains operations for collections of renditions.
	1. get_renditions(self, digital_asset_id: str, revision_number: int, **kwargs) -> requests.Response
	2. create_rendition(self, digital_asset_id: str, revision_number: int, payload: dict) -> requests.Response
	3. get_rendition(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response
	4. get_rendition_headers(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response
	5. delete_rendition(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response
	6. patch_rendition(self, digital_asset_id: str, revision_number: int, rendition_id: str, payload: dict) -> requests.Response
	7. get_preview(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response
	8. get_content(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apidigitalassets import renditions


class TestRenditions(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingDigitalAssets"
		encoding = "UTF-8"
		host = os.environ.get("SASCI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ["SASCI360_SECRET_KEY"]
		tenant_id = os.environ["SASCI360_TENANT_ID"]

		self.renditions = renditions.Renditions(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_renditions(self):
		"""
		1. get_renditions(self, digital_asset_id: str, revision_number: int, **kwargs) -> requests.Response
		"""
		digital_asset_id = "0"
		revision_number = 0
		result = self.renditions.get_renditions(digital_asset_id=digital_asset_id, revision_number=revision_number)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_rendition(self):
		"""
		2. create_rendition(self, digital_asset_id: str, revision_number: int, payload: dict) -> requests.Response
		"""
		digital_asset_id = "0"
		revision_number = 0
		payload = {
			"id": "string",
			"name": "string",
			"submittedBy": "string",
			"submittedTimeStamp": "2019-08-24T14:15:22Z",
			"typeCode": "upl",
			"typeCodeDescription": "string",
			"stateCode": "prc",
			"stateCodeDescription": "string",
			"originalState": 0,
			"previewState": 0,
			"thumbnailState": 0,
			"customState": 0,
			"otherState": 0,
			"links": [
				{
					"method": "GET",
					"rel": "self",
					"href": "https://extapigwservice-<server>/<endpoint>/",
					"uri": "/<endpoint>",
					"type": "application/vnd.sas.collection"
				}
			]
		}
		result = self.renditions.create_rendition(digital_asset_id=digital_asset_id, revision_number=revision_number, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_rendition(self):
		"""
		3. get_rendition(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response
		"""
		digital_asset_id = "0"
		revision_number = 0
		rendition_id = "0"
		result = self.renditions.get_rendition(digital_asset_id=digital_asset_id, revision_number=revision_number, rendition_id=rendition_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_rendition_headers(self):
		"""
		4. get_rendition_headers(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response
		"""
		digital_asset_id = "0"
		revision_number = 0
		rendition_id = "0"
		result = self.renditions.get_rendition_headers(digital_asset_id=digital_asset_id, revision_number=revision_number, rendition_id=rendition_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_delete_rendition(self):
		"""
		5. delete_rendition(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response
		"""
		digital_asset_id = "0"
		revision_number = 0
		rendition_id = "0"
		result = self.renditions.delete_rendition(digital_asset_id=digital_asset_id, revision_number=revision_number, rendition_id=rendition_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_patch_rendition(self):
		"""
		6. patch_rendition(self, digital_asset_id: str, revision_number: int, rendition_id: str, payload: dict) -> requests.Response
		"""
		digital_asset_id = "0"
		revision_number = 0
		rendition_id = "0"
		payload = {"operations": [{"op": "add", "path": "string", "value": {}, "from": "string"}]}
		result = self.renditions.patch_rendition(digital_asset_id=digital_asset_id, revision_number=revision_number, rendition_id=rendition_id, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_preview(self):
		"""
		7. get_preview(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response
		"""
		digital_asset_id = "0"
		revision_number = 0
		rendition_id = "0"
		result = self.renditions.get_preview(digital_asset_id=digital_asset_id, revision_number=revision_number, rendition_id=rendition_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_content(self):
		"""
		8. get_content(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response
		"""
		digital_asset_id = "0"
		revision_number = 0
		rendition_id = "0"
		result = self.renditions.get_content(digital_asset_id=digital_asset_id, revision_number=revision_number, rendition_id=rendition_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
