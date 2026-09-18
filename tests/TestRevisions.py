#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Revisions Module
Contains operations for collections of revisions.
	1. get_revisions(self, digital_asset_id: str, **kwargs) -> requests.Response
	2. create_revision(self, digital_asset_id: str, payload: dict) -> requests.Response
	3. get_revision_headers(self, digital_asset_id: str, revision_number: int) -> requests.Response
	4. create_revision_from_revision(self, digital_asset_id: str, revision_number: int, **kwargs) -> requests.Response
	5. delete_revision(self, digital_asset_id: str, revision_number: int) -> requests.Response
"""

import os
import unittest
from sasci360apidigitalassets import revisions


class TestRevisions(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingDigitalAssets"
		encoding = "UTF-8"
		host = os.environ.get("SASCI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ["SASCI360_SECRET_KEY"]
		tenant_id = os.environ["SASCI360_TENANT_ID"]

		self.revisions = revisions.Revisions(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_revisions(self):
		"""
		1. get_revisions(self, digital_asset_id: str, **kwargs) -> requests.Response
		"""
		digital_asset_id = "0"
		result = self.revisions.get_revisions(digital_asset_id=digital_asset_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_revision(self):
		"""
		2. create_revision(self, digital_asset_id: str, payload: dict) -> requests.Response
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
			"state": "act", "locked": True,
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
							"value": [{"label": "string"}],
							"attributeCode": "string",
							"type": "string",
							"visible": True,
							"obsolete": True,
							"adHoc": True,
							"dynamic": True,
							"validator": [{"required": True}],
							"dataProvider": [{"key": "string", "text": "string"}]
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
			"relatedSource":
				{
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
		result = self.revisions.create_revision(digital_asset_id=digital_asset_id, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_revision_headers(self):
		"""
		3. get_revision_headers(self, digital_asset_id: str, revision_number: int) -> requests.Response
		"""
		digital_asset_id = "0"
		revision_number = 0
		result = self.revisions.get_revision_headers(digital_asset_id=digital_asset_id, revision_number=revision_number)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_revision_from_revision(self):
		"""
		4. create_revision_from_revision(self, digital_asset_id: str, revision_number: int, **kwargs) -> requests.Response
		"""
		digital_asset_id = "0"
		revision_number = 0
		result = self.revisions.create_revision_from_revision(digital_asset_id=digital_asset_id, revision_number=revision_number)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_delete_revision(self):
		"""
		5. delete_revision(self, digital_asset_id: str, revision_number: int) -> requests.Response
		"""
		digital_asset_id = "0"
		revision_number = 0
		result = self.revisions.delete_revision(digital_asset_id=digital_asset_id, revision_number=revision_number)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
