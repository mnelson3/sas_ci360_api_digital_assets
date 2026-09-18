#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apidigitalassets.base import Base


class Revisions(Base):
	"""
	Revisions Module
	Contains operations for collections of revisions.
		1. get_revisions(self, digital_asset_id: str, **kwargs) -> requests.Response
		2. create_revision(self, digital_asset_id: str, payload: dict) -> requests.Response
		3. get_revision_headers(self, digital_asset_id: str, revision_number: int) -> requests.Response
		4. create_revision_from_revision(self, digital_asset_id: str, revision_number: int, **kwargs) -> requests.Response
		5. delete_revision(self, digital_asset_id: str, revision_number: int) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_revisions(self, digital_asset_id: str, **kwargs) -> requests.Response:
		"""
		Get a collection of revisions for a digital asset
		:param digital_asset_id: required - The ID of the digital asset under which the revisions are associated
		:keyword start: int, optional - The index of the first rendition to return
		:keyword limit: int, optional - The maximum number of renditions to return
		:return: Returns a collection of revisions based on options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.revision media type.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if digital_asset_id is None:
			raise Exception("Digital Asset ID is missing.")
		try:
			query_string = "?"
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
			api_path = "/digitalAssets/{0}/revisions{1}".format(digital_asset_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_revision(self, digital_asset_id: str, payload: dict) -> requests.Response:
		"""
		Create a new revision for a digital asset
		:param digital_asset_id: required - The unique identifier for the digital asset under which the revisions are associated
		:param payload: required - The representation of a digital asset with which new revision needs to be created
		:return: Creates a new revision based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if digital_asset_id is None:
			raise Exception("Digital Asset ID is missing.")
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}/revisions".format(digital_asset_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_revision_headers(self, digital_asset_id: str, revision_number: int) -> requests.Response:
		"""
		Get the headers for a revision of the specified digital asset
		:param digital_asset_id: required - The unique identifier for the digital asset
		:param revision_number: required - The revision number for the digital asset. The revision number is a unique, incrementing number for the specified digital asset
		:return: Returns the HTTP headers for a revision of the specified digital asset. The method can also be used to determine whether a revision exists for the specified digital asset.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if digital_asset_id is None:
			raise Exception("Digital Asset ID is missing.")
		if revision_number is None:
			raise Exception("Revision Number is missing.")
		try:
			action = "HEAD"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}/revisions/{1}".format(digital_asset_id, revision_number)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_revision_from_revision(self, digital_asset_id: str, revision_number: int, **kwargs) -> requests.Response:
		"""
		Create a new revision for a digital asset by using existing revision
		:param digital_asset_id: required - The unique identifier for the digital asset under which the revisions are associated
		:param revision_number: required - The revision number for the digital asset that is used to create the new revision
		:keyword action: str, required - The query parameter that specifies the action to take. Specify the action as "makelatest" when you want to create a new revision and mark it as current revision.
		:return: Creates a new revision that is based on an existing revision. Specify the existing revision by revision number in the path.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if digital_asset_id is None:
			raise Exception("Digital Asset ID is missing.")
		if revision_number is None:
			raise Exception("Revision Number is missing.")
		try:
			query_string = "?"
			if "action" in kwargs:
				query_string.join("action={0}&".format(kwargs["action"]))
			action = "POST"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/digitalAssets/{0}/revisions/{1}{2}".format(digital_asset_id, revision_number, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_revision(self, digital_asset_id: str, revision_number: int) -> requests.Response:
		"""
		Delete a revision
		:param digital_asset_id: required - The unique identifier for the digital asset under which the revisions are associated
		:param revision_number: required - The revision number for the digital asset
		:return: Deletes the revision for the specified digital asset.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if digital_asset_id is None:
			raise Exception("Digital Asset ID is missing.")
		if revision_number is None:
			raise Exception("Revision Number is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}/revisions/{1}".format(digital_asset_id, revision_number)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Revisions()
