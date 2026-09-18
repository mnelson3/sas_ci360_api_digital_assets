#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apidigitalassets.base import Base


class Jobs(Base):
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

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_asset_jobs(self, **kwargs) -> requests.Response:
		"""
		Get a collection of jobs for digital assets in SAS Customer Intelligence 360
		:keyword type: str, optional - The type of the jobs to return. The jobs are returned only if they match this value exactly
		:keyword start: int, optional - The index of the first job to return
		:keyword limit: int, optional - The maximum number of jobs to return
		:return: Returns a collection of jobs for the Assets service based on the options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.job media type.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "type" in kwargs:
				query_string.join("type={0}&".format(kwargs["type"]))
			if "start" in kwargs:
				query_string.join("start={0}&".format(kwargs["start"]))
			if "limit" in kwargs:
				query_string.join("limit={0}&".format(kwargs["limit"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/assetJobs{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def batch_upload(self, payload: dict) -> requests.Response:
		"""
		Create a job that creates new digital assets that are based on the representation in the request body
		:param payload: required - The representation of batch upload details for the digital asset
		:return: Creates one or more digital assets through a batch job. Digital media files are uploaded from the location that is provided. These media files are used to create the new digital assets and renditions for the respective digital assets. The request body also contains the standard properties like expiration date and description.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/batchUpload"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def batch_catalog(self, payload: dict) -> requests.Response:
		"""
		Create a job to catalog and create the new digital assets based on the representation in the request body
		:param payload: required - The representation of batch cataloging details for the digital asset
		:return: Creates one or more digital assets through a batch job by cataloging the existing digital contents from Amazon Web Service's S3 location. The request body contains the information of existing digital content. This content is actual digital media files that are used by applications like SAS 360 Plan. The media files are used to create new digital assets and corresponding renditions.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			action = "GET"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/batchCatalog"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def batch_standard_attribute_update(self, payload: dict) -> requests.Response:
		"""
		Create a job to update the digital assets based on the representation in the request body
		:param payload: required - The representation of batch update of standard properties for the digital asset
		:return: Creates a batch job to update standard properties of one or more digital assets. You can update properties such as description and the expired-on date by using this service.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/batchStandardAttributeUpdate"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def batch_custom_attribute_update(self, payload: dict) -> requests.Response:
		"""
		Create a job to update the custom properties (metadata properties) for the digital assets
		:param payload: required
		:return: Creates a batch job to update the custom properties of one or more digital assets. Custom properties are defined in an Excel file that contains the details about the properties and the types of assets that use them. You must upload the Excel file as part of this service.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/batchCustomAttributeUpdate"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def batch_externalization(self, payload: dict) -> requests.Response:
		"""
		Create a job to externalize the digital assets based on the representation in the request body
		:param payload: required - The representation of batch externalization for the digital asset
		:return: Creates a batch job to mark digital assets for external sharing. Externally shared assets can be used by other systems (for example, to use as advertising through various channels). After a digital asset is marked for external sharing, a public URL is associated with the asset. Third-party systems can use the URL to embed the digital media into emails or web pages.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/batchExternalization"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_asset_job(self, job_id: str) -> requests.Response:
		"""
		Get an asset job
		:param job_id: required - The unique identifier for the job
		:return: Returns the representation of the specified asset job.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if job_id is None:
			raise Exception("Job ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/assetJobs/{}".format(job_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_asset_job_headers(self, job_id: str) -> requests.Response:
		"""
		Get the headers for a digital asset job
		:param job_id: required - The unique identifier for the job
		:return: Returns the HTTP headers for a digital asset's job. The method can also be used to determine whether a job exists.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if job_id is None:
			raise Exception("Job ID is missing.")
		try:
			action = "HEAD"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/assetJobs/{}".format(job_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_asset_job(self, job_id: str) -> requests.Response:
		"""
		Delete a job
		:param job_id: required - The unique identifier for the job
		:return: Deletes the specified job.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if job_id is None:
			raise Exception("Job ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/assetJobs/{}".format(job_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Jobs()
