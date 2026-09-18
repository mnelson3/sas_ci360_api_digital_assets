#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apidigitalassets.base import Base


class Renditions(Base):
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

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_renditions(self, digital_asset_id: str, revision_number: int, **kwargs) -> requests.Response:
		"""
		Get a collection of renditions
		:param digital_asset_id: required - The unique identifier for the digital asset that is associated with the specified revision number
		:param revision_number: required - The revision number for the digital asset
		:keyword start: int, optional - The index of the first rendition to return
		:keyword limit: int, optional - The maximum number of renditions to return
		:return: Returns a collection of renditions based on the digital asset and revision that you specify.
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
			api_path = "/digitalAssets/{0}/revisions/{1}/renditions{2}".format(digital_asset_id, revision_number, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_rendition(self, digital_asset_id: str, revision_number: int, payload: dict) -> requests.Response:
		"""
		Create a rendition for a digital asset and revision
		:param digital_asset_id: required - The unique identifier for the digital asset that is associated with the specified revision number
		:param revision_number: required - The revision number for the digital asset
		:param payload: required
		:return: Creates a rendition for a digital asset and revision based on the representation in the request body.
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
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}/revisions/{1}/renditions".format(digital_asset_id, revision_number)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_rendition(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response:
		"""
		Get a rendition by ID for a digital asset and revision number
		:param digital_asset_id: required - The unique identifier for the digital asset
		:param revision_number: required - The revision number for the digital asset
		:param rendition_id: required - The unique identifier for the rendition
		:return: Returns the representation of the specified rendition based on what is specified for the digital asset, revision number, and revision ID.
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
		if rendition_id is None:
			raise Exception("Rendition ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}/revisions/{1}/renditions/{2}".format(digital_asset_id, revision_number, rendition_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_rendition_headers(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response:
		"""
		Get the headers for a rendition based on the ID
		:param digital_asset_id: required - The unique identifier for the digital asset
		:param revision_number: required - The revision number for the digital asset
		:param rendition_id: required - The unique identifier for the rendition
		:return: Returns the HTTP headers for a rendition that is associated with the digital asset and revision that you specify in the request. The method can also be used to determine whether a rendition exists.
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
		if rendition_id is None:
			raise Exception("Rendition ID is missing.")
		try:
			action = "HEAD"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}/revisions/{1}/renditions/{2}".format(digital_asset_id, revision_number, rendition_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_rendition(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response:
		"""
		Delete a rendition by ID
		:param digital_asset_id: required - The unique identifier for the digital asset
		:param revision_number: required - The revision number for the digital asset
		:param rendition_id: required - The unique identifier for the rendition
		:return: Deletes the rendition based on the ID, the digital asset, and the revision that you specify.
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
		if rendition_id is None:
			raise Exception("Rendition ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}/revisions/{1}/renditions/{2}".format(digital_asset_id, revision_number, rendition_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def patch_rendition(self, digital_asset_id: str, revision_number: int, rendition_id: str, payload: dict) -> requests.Response:
		"""
		Update a rendition by ID
		:param digital_asset_id: required - The unique identifier for the digital asset
		:param revision_number: required - The revision number for the digital asset
		:param rendition_id: required - The unique identifier for the rendition
		:param payload: required - The representation of a patch operation for rendition
		:return: Updates the specified rendition of the given digital asset and revision based on the representation in the request body.
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
		if rendition_id is None:
			raise Exception("Rendition ID is missing.")
		try:
			action = "PATCH"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}/revisions/{1}/renditions/{2}/download".format(digital_asset_id, revision_number, rendition_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_preview(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response:
		"""
		Get the preview of a digital asset's rendition
		:param digital_asset_id: required - The unique identifier for the digital asset
		:param revision_number: required - The revision number for the digital asset
		:param rendition_id: required - The unique identifier for the rendition
		:return: Returns the content of preview based on the rendition ID, digital asset, and revision that you specify. The content can be like image/jpg (for digital images), video/quicktime (for movie files), etc.
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
		if rendition_id is None:
			raise Exception("Rendition ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}/revisions/{1}/renditions/{2}/download".format(digital_asset_id, revision_number, rendition_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_content(self, digital_asset_id: str, revision_number: int, rendition_id: str) -> requests.Response:
		"""
		Download a revision's content
		:param digital_asset_id: required - The unique identifier for the digital asset
		:param revision_number: required - The revision number for the digital asset
		:param rendition_id: required - The unique identifier for the rendition
		:return: Download the rendition of a digital asset based on the rendition's ID, digital asset, and revision that you specify. You can download the digital file of the type actual (original), preview, thumbnail, or custom rendition. The file can be an image, video, pdf, etc.
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
		if rendition_id is None:
			raise Exception("Rendition ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/{0}/revisions/{1}/renditions/{2}/download".format(digital_asset_id, revision_number, rendition_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Renditions()
