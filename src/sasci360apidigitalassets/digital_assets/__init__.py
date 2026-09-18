#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apidigitalassets.base import Base


class DigitalAssets(Base):
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

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_digital_assets(self, **kwargs) -> requests.Response:
		"""
		Get a collection of digital assets
		:keyword parent: str, required - The ID of the folder where digital assets are stored in the system; Digital assets are returned only if the parent folder matches this value
		:keyword start: int, optional - The index of the first digital asset to return; Note: If the Accept header does not specify version 1, this parameter is required
		:keyword limit: int, optional - The maximum number of digital assets to return; Note: If the Accept header does not specify version 1, this parameter is required
		:return: Returns a collection of digital assets based on the options for pagination, filtering, and sorting; The items in the collection use the application/vnd.sas.marketing.asset.summary media type
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if kwargs["parent"] is None:
			raise Exception("Parent is missing.")
		try:
			query_string = "?"
			if "parent" in kwargs:
				query_string.join("parent={0}&".format(kwargs["parent"]))
			if "start" in kwargs:
				query_string.join("start={0}&".format(kwargs["start"]))
			if "limit" in kwargs:
				query_string.join("limit={0}&".format(kwargs["limit"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/vnd.sas.collection+json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/digitalAssets{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_digital_asset_headers(self, digital_asset_id: str) -> requests.Response:
		"""
		Get Digital Asset Headers
		:param digital_asset_id: required - The unique identifier for the digital asset
		:return: Returns the HTTP headers for a digital asset. The method can also be used to determine whether a digital asset exists.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if digital_asset_id is None:
			raise Exception("Digital Asset ID is missing.")
		try:
			action = "HEAD"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}".format(digital_asset_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_digital_asset(self, digital_asset_id: str) -> requests.Response:
		"""
		Get Digital Asset
		:param digital_asset_id: required - The unique identifier for the digital asset
		:return: Returns the representation of the specified digital asset for the current (latest) revision. The link for renditions will have the current revision number.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if digital_asset_id is None:
			raise Exception("Digital Asset ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}".format(digital_asset_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_digital_asset(self, payload: dict) -> requests.Response:
		"""
		Create a new digital asset
		:param payload: required - Representation of a digital asset
		:return: Creates a new digital asset based on the representation in the request body
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
			api_path = "/digitalAssets"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_digital_asset(self, digital_asset_id: str, payload: dict) -> requests.Response:
		"""
		Update a digital asset
		:param digital_asset_id: required - The unique identifier for the digital asset
		:param payload: required - The representation of a digital asset
		:return: Updates the specified digital asset based on the representation in the request body
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if digital_asset_id is None:
			raise Exception("Digital Asset ID is missing.")
		try:
			action = "PUT"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}".format(digital_asset_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def patch_digital_asset(self, digital_asset_id: str, payload: dict) -> requests.Response:
		"""
		Update a digital asset
		:param digital_asset_id: required - The unique identifier for the digital asset
		:param payload: required - The representation of a patch operation for a digital asset
		:return: Updates the specified digital asset based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if digital_asset_id is None:
			raise Exception("Digital Asset ID is missing.")
		try:
			action = "PATCH"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}".format(digital_asset_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_digital_asset_current(self, digital_asset_id: str) -> requests.Response:
		"""
		Get the current revision of a digital asset
		:param digital_asset_id: required - The unique identifier for the digital asset
		:return: Returns the representation of the specified digital asset with the current revision. The links for the renditions (related resource) will have the current revision number.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if digital_asset_id is None:
			raise Exception("Digital Asset ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}/revisions/current".format(digital_asset_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_digital_asset_by_revision(self, digital_asset_id: str, revision_number: int) -> requests.Response:
		"""
		Get a digital asset for a specified revision
		:param digital_asset_id: required - The unique identifier for the digital asset
		:param revision_number: required - The revision number for the digital asset; the revision number is a unique incremental number that is specified for the digital asset revision
		:return: Returns the representation of the specified digital asset for the revision that is specified. The links for renditions (related resource) will have the specified revision number.
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
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/vnd.sas.marketing.asset+json",
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
	DigitalAssets()
