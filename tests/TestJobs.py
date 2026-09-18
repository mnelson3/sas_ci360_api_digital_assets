#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Jobs Module
Contains operations for a jobs that are related to digital assets.
	1. get_asset_jobs(self, **kwargs) -> requests.Response
	2. batch_upload(self, payload: dict) -> requests.Response
	3. batch_catalog(self, payload: dict) -> requests.Response
	4. batch_standard_attribute_update(self, payload: dict) -> requests.Response
	5. batch_custom_attribute_update(self, payload: dict) -> requests.Response
	6. batch_externalization(self, payload: dict) -> requests.Response
	7. get_asset_job(self, job_id: str) -> requests.Response
	8. get_asset_job_headers(self, job_id: str) -> requests.Response
	9. delete_asset_job(self, job_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apidigitalassets import jobs


class TestJobs(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingDigitalAssets"
		encoding = "UTF-8"
		host = os.environ.get("SASCI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ["SASCI360_SECRET_KEY"]
		tenant_id = os.environ["SASCI360_TENANT_ID"]

		self.jobs = jobs.Jobs(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_asset_jobs(self):
		"""
		1. get_asset_jobs(self, **kwargs) -> requests.Response
		"""
		result = self.jobs.get_asset_jobs()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_batch_upload(self):
		"""
		2. batch_upload(self, payload: dict) -> requests.Response
		"""
		payload = {
			"type": "batchAssetUpload",
			"defaultParentFolderId": "string",
			"version": 0,
			"digitalAssets": [
				{
					"id": "string",
					"name": "string",
					"version": 0,
					"description": "string",
					"expiredTimeStamp": "2019-08-24T14:15:22Z",
					"parentFolderId": "string",
					"domainObjectTypeCode": "string",
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
									"href": "https://extapigwservice-<server>/<endpoint>/", "uri": "/<endpoint>", "type": "application/vnd.sas.collection"
								}
							]
						}
					]
				}
			]
		}
		result = self.jobs.batch_upload(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_batch_catalog(self):
		"""
		3. batch_catalog(self, payload: dict) -> requests.Response
		"""
		payload = {
			"type": "batchAssetUpload",
			"version": 0,
			"digitalAssets": [
				{
					"id": "string",
					"name": "string",
					"version": 0,
					"description": "string",
					"expiredTimeStamp": "2019-08-24T14:15:22Z",
					"parentFolderId": "string",
					"domainObjectTypeCode": "string",
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
					"contentType": "string",
					"contentSize": 0,
					"fileId": "string",
					"catalogFileName": "string",
					"catalogFilePath": "string",
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
					}
				}
			]
		}
		result = self.jobs.batch_catalog(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_batch_standard_attribute_update(self):
		"""
		4. batch_standard_attribute_update(self, payload: dict) -> requests.Response
		"""
		payload = {
			"type": "batchAssetUpload",
			"version": 0,
			"digitalAssetIds": [None],
			"digitalAssetAttributes":
				{
					"standardAttributes":
						{
							"name": "string",
							"version": 0,
							"value": [None]
						}
				}
		}
		result = self.jobs.batch_standard_attribute_update(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_batch_custom_attribute_update(self):
		"""
		5. batch_custom_attribute_update(self, payload: dict) -> requests.Response
		"""
		payload = {
			"id": "string",
			"name": "string",
			"localizedName": "string",
			"version": 0,
			"createdBy": "string",
			"creationTimeStamp": "2019-08-24T14:15:22Z",
			"modifiedBy": "string",
			"modifiedTimeStamp": "2019-08-24T14:15:22Z",
			"totalItems": 0,
			"application": "string",
			"type": "string",
			"parallelJobSteps": True,
			"state": "created",
			"steps": [
				{
					"name": "string",
					"version": 0,
					"type": "string",
					"state": "prepared",
					"creationTimeStamp": "2019-08-24T14:15:22Z",
					"asynchronous": True,
					"errorMessages": [None],
					"warningMessages": [None]
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
		result = self.jobs.batch_custom_attribute_update(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_batch_externalization(self):
		"""
		6. batch_externalization(self, payload: dict) -> requests.Response
		"""
		payload = {
			"version": 0,
			"externalizeData": [
				{
					"digitalAssetId": "string",
					"version": 0,
					"markAsExternal": "string"
				}
			]
		}
		result = self.jobs.batch_externalization(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_asset_job(self):
		"""
		7. get_asset_job(self, job_id: str) -> requests.Response
		"""
		job_id = "0"
		result = self.jobs.get_asset_job(job_id=job_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_asset_job_headers(self):
		"""
		8. get_asset_job_headers(self, job_id: str) -> requests.Response
		"""
		job_id = "0"
		result = self.jobs.get_asset_job_headers(job_id=job_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_delete_asset_job(self):
		"""
		9. delete_asset_job(self, job_id: str) -> requests.Response
		"""
		job_id = "0"
		result = self.jobs.delete_asset_job(job_id=job_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
