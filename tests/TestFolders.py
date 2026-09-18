#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Folders Module
Contains operations for a collection of folders.
	1. get_folders(self, **kwargs) -> requests.Response
	2. create_folder(self, payload: dict, **kwargs) -> requests.Response
	3. get_folder(self, folder_id: str) -> requests.Response
	4. get_folder_headers(self, folder_id: str) -> requests.Response
	5. update_folder(self, folder_id: str, payload: dict) -> requests.Response
	6. delete_folder(self, folder_id: str) -> requests.Response
	7. patch_folder(self, folder_id: str, payload: dict) -> requests.Response
"""

import os
import unittest
from sasci360apidigitalassets import folders


class TestFolders(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingDigitalAssets"
		encoding = "UTF-8"
		host = os.environ.get("SASCI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ["SASCI360_SECRET_KEY"]
		tenant_id = os.environ["SASCI360_TENANT_ID"]

		self.folders = folders.Folders(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_folders(self):
		"""
		1. get_folders(self, **kwargs) -> requests.Response
		"""
		result = self.folders.get_folders()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_folder(self):
		"""
		2. create_folder(self, payload: dict, **kwargs) -> requests.Response
		"""
		payload = {
			"id": "string",
			"name": "string",
			"version": 0,
			"description": "string",
			"createdBy": "string",
			"creationTimeStamp": "2019-08-24T14:15:22Z",
			"modifiedBy": "string",
			"modifiedTimeStamp": "2019-08-24T14:15:22Z",
			"folderPath": "string",
			"identityPermissions": [
				{
					"type": "string",
					"name": "string",
					"displayName": "string",
					"permission": "string",
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
			],
			"links": [
				{
					"method": "GET",
					"rel": "self",
					"href": "https://extapigwservice-<server>/<endpoint>/",
					"uri": "/<endpoint>", "type": "application/vnd.sas.collection"
				}
			]
		}
		result = self.folders.create_folder(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_folder(self):
		"""
		3. get_folder(self, folder_id: str) -> requests.Response
		"""
		folder_id = "0"
		result = self.folders.get_folder(folder_id=folder_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_folder_headers(self):
		"""
		4. get_folder_headers(self, folder_id: str) -> requests.Response
		"""
		folder_id = "0"
		result = self.folders.get_folder_headers(folder_id=folder_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_update_folder(self):
		"""
		5. update_folder(self, folder_id: str, payload: dict) -> requests.Response
		"""
		folder_id = "0"
		payload = {
			"id": "string",
			"name": "string",
			"version": 0,
			"description": "string",
			"createdBy": "string",
			"creationTimeStamp": "2019-08-24T14:15:22Z",
			"modifiedBy": "string",
			"modifiedTimeStamp": "2019-08-24T14:15:22Z",
			"folderPath": "string",
			"identityPermissions": [
				{
					"type": "string",
					"name": "string",
					"displayName": "string",
					"permission": "string",
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
			],
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
		result = self.folders.update_folder(folder_id=folder_id, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_delete_folder(self):
		"""
		6. delete_folder(self, folder_id: str) -> requests.Response
		"""
		folder_id = "0"
		result = self.folders.delete_folder(folder_id=folder_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_patch_folder(self):
		"""
		7. patch_folder(self, folder_id: str, payload: dict) -> requests.Response
		"""
		folder_id = "0"
		payload = {
			"operations": [
				{
					"op": "add",
					"path": "string",
					"value": {},
					"from": "string"
				}
			]
		}
		result = self.folders.patch_folder(folder_id=folder_id, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
