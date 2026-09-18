#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Digital Assets Module
Contains operations to manage collection of digital assets.
	1. get_digital_assets(self, **kwargs) -> requests.Response
	2. get_digital_asset_headers(self, digital_asset_id: str) -> requests.Response
	3. get_digital_asset(self, digital_asset_id: str) -> requests.Response
	4. create_digital_asset(self, payload: dict) -> requests.Response
	5. update_digital_asset(self, digital_asset_id: str, payload: dict) -> requests.Response
	6. patch_digital_asset(self, digital_asset_id: str, payload: dict) -> requests.Response
	7. get_digital_asset_current(self, digital_asset_id: str) -> requests.Response
	8. get_digital_asset_by_revision(self, digital_asset_id: str, revision_number: int) -> requests.Response
"""

import os
import unittest
from sasci360apidigitalassets import digital_assets


class TestDigitalAssets(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingDigitalAssets"
		encoding = "UTF-8"
		host = os.environ.get("SASCI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ["SASCI360_SECRET_KEY"]
		tenant_id = os.environ["SASCI360_TENANT_ID"]

		self.digital_assets = digital_assets.DigitalAssets(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_digital_assets(self):
		"""
		1. get_digital_assets(self, **kwargs) -> requests.Response
		"""
		parent = "0"  # required
		# start = 0   # optional
		# limit = 0   # optional
		result = self.digital_assets.get_digital_assets(parent=parent)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_digital_asset_headers(self):
		"""
		2. get_digital_asset_headers(self, digital_asset_id: str) -> requests.Response
		"""
		digital_asset_id = "0"
		result = self.digital_assets.get_digital_asset_headers(digital_asset_id=digital_asset_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_digital_asset(self):
		"""
		3. get_digital_asset(self, digital_asset_id: str) -> requests.Response
		"""
		digital_asset_id = "0"
		result = self.digital_assets.get_digital_asset(digital_asset_id=digital_asset_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_digital_asset(self):
		"""
		4. create_digital_asset(self, payload: dict) -> requests.Response
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
			"state": "act",
			"locked": True,
			"lockedBy": "string",
			"lockedTimeStamp": "2019-08-24T14:15:22Z",
			"downloadDisabled": True,
			"downloadDisabledBy": "string",
			"downloadDisabledTimeStamp": "2019-08-24T14:15:22Z",
			"expired": True,
			"expiredTimeStamp": "2019-08-24T14:15:22Z",
			"subType": "defaultAsset",
			"parentFolderId": "string",
			"parentFolderPath": "string",
			"downloadCount": 0,
			"ratingCount": 0,
			"ratingTotal": 0,
			"ratingAverage": "string",
			"missingMetadata": True,
			"active": True,
			"permission": "string",
			"publicUrlAvailable": "string",
			"localizedPublicUrlAvailable": "string",
			"publicUrl": "string",
			"localizedExternalProcessError": "string",
			"revisionNumber": 0,
			"revisionComment": "string",
			"revisionId": "string",
			"currentRevision": True,
			"domainObjectTypeCode": "string",
			"attributeGroups": [None],
			"customAttributes": [
				{
					"groupId": "string",
					"label": "string",
					"visible": True,
					"obsolete": True,
					"fields": [
						{
							"label": "string",
							"value": [
								{
									"label": "string"
								}
							],
							"attributeCode": "string",
							"type": "string",
							"visible": True,
							"obsolete": True,
							"adHoc": True,
							"dynamic": True,
							"validator": [
								{
									"required": True
								}
							],
							"dataProvider": [
								{
									"key": "string",
									"text": "string"
								}
							]
						}
					]
				}
			],
			"tags": [
				{
					"id": "string",
					"name": "string",
					"version": 0,
					"modifiedStatusCode": "string",
					"createdBy": "string",
					"creationTimeStamp": "2019-08-24T14:15:22Z",
					"modifiedBy": "string",
					"modifiedTimeStamp": "2019-08-24T14:15:22Z",
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
			"relatedSource": {
				"sourceSolutionName": "string",
				"sourceType": "string",
				"urlInfo": [
					{
						"title": "string",
						"relationship": "string",
						"mediaType": "string",
						"url": "string",
						"uri": "string",
						"configurationKey": "string",
						"urlParameters": [
							{
								"key": "string",
								"value": "string"
							}
						]
					}
				]
			},
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
		result = self.digital_assets.create_digital_asset(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_update_digital_asset(self):
		"""
		5. update_digital_asset(self, digital_asset_id: str, payload: dict) -> requests.Response
		"""
		digital_asset_id = "0"
		payload = {
			"id": "string",
			"name": "string",
			"version": 0,
			"description": "string",
			"createdBy": "string",
			"creationTimeStamp": "2019-08-24T14:15:22Z",
			"modifiedBy": "string",
			"modifiedTimeStamp": "2019-08-24T14:15:22Z",
			"state": "act",
			"locked": True,
			"lockedBy": "string",
			"lockedTimeStamp": "2019-08-24T14:15:22Z",
			"downloadDisabled": True,
			"downloadDisabledBy": "string",
			"downloadDisabledTimeStamp": "2019-08-24T14:15:22Z",
			"expired": True,
			"expiredTimeStamp": "2019-08-24T14:15:22Z",
			"subType": "defaultAsset",
			"parentFolderId": "string",
			"parentFolderPath": "string",
			"downloadCount": 0,
			"ratingCount": 0,
			"ratingTotal": 0,
			"ratingAverage": "string",
			"missingMetadata": True,
			"active": True,
			"permission": "string",
			"publicUrlAvailable": "string",
			"localizedPublicUrlAvailable": "string",
			"publicUrl": "string",
			"localizedExternalProcessError": "string",
			"revisionNumber": 0,
			"revisionComment": "string",
			"revisionId": "string",
			"currentRevision": True,
			"domainObjectTypeCode": "string",
			"attributeGroups": [None],
			"customAttributes": [
				{
					"groupId": "string",
					"label": "string",
					"visible": True,
					"obsolete": True,
					"fields": [
						{
							"label": "string",
							"value": [
								{
									"label": "string"
								}
							],
							"attributeCode": "string",
							"type": "string",
							"visible": True,
							"obsolete": True,
							"adHoc": True,
							"dynamic": True,
							"validator": [
								{
									"required": True
								}
							],
							"dataProvider": [
								{
									"key": "string",
									"text": "string"
								}
							]
						}
					]
				}
			],
			"tags": [
				{
					"id": "string",
					"name": "string",
					"version": 0,
					"modifiedStatusCode": "string",
					"createdBy": "string",
					"creationTimeStamp": "2019-08-24T14:15:22Z",
					"modifiedBy": "string",
					"modifiedTimeStamp": "2019-08-24T14:15:22Z",
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
			"relatedSource": {
				"sourceSolutionName": "string",
				"sourceType": "string",
				"urlInfo": [
					{
						"title": "string",
						"relationship": "string",
						"mediaType": "string",
						"url": "string",
						"uri": "string",
						"configurationKey": "string",
						"urlParameters": [
							{
								"key": "string",
								"value": "string"
							}
						]
					}
				]
			},
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
		result = self.digital_assets.update_digital_asset(digital_asset_id=digital_asset_id, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_patch_digital_asset(self):
		"""
		6. patch_digital_asset(self, digital_asset_id: str, payload: dict) -> requests.Response
		"""
		digital_asset_id = "0"
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
		result = self.digital_assets.patch_digital_asset(digital_asset_id=digital_asset_id, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_digital_asset_current(self):
		"""
		7. get_digital_asset_current(self, digital_asset_id: str) -> requests.Response
		"""
		digital_asset_id = "0"
		result = self.digital_assets.get_digital_asset_current(digital_asset_id=digital_asset_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_digital_asset_by_revision(self):
		"""
		8. get_digital_asset_by_revision(self, digital_asset_id: str, revision_number: int) -> requests.Response
		"""
		digital_asset_id = "0"
		revision_number = 0
		result = self.digital_assets.get_digital_asset_by_revision(digital_asset_id=digital_asset_id, revision_number=revision_number)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
