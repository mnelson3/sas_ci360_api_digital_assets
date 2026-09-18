#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apidigitalassets.base import Base


class PropertiesFile(Base):
	"""
	Properties File Module
	Contains operations to upload standard properties and custom properties for digital assets.
		1. create_properties_file(self, payload: dict) -> requests.Response
		2. get_properties_file(self, attribute_file_id: str) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def create_properties_file(self, payload: list) -> requests.Response:
		"""
		Create an Excel file to define properties for the specified digital assets
		:param payload: required - The string array of digital asset identifiers that properties will be extracted for
		:return: Creates a Microsoft Excel file with standard properties and custom properties based on the JSON in the request body. The same file is used for the batch update for custom properties (/digitalAssets/batchCustomAttributeUpdate).
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
			api_path = "/digitalAssets/attributeFile"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_properties_file(self, attribute_file_id: str) -> requests.Response:
		"""
		Download the attribute Excel file
		:param attribute_file_id: required - The unique identifier for the properties file
		:return: Downloads the Excel file that contains the standard properties and custom properties. The same file is used for the batch update of custom properties (/digitalAssets/batchCustomAttributeUpdate).
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if attribute_file_id is None:
			raise Exception("Attribute File ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/digitalAssets/attributeFile/{0}/download".format(attribute_file_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	PropertiesFile()
