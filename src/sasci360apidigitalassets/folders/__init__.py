#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apidigitalassets.base import Base


class Folders(Base):
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

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_folders(self, **kwargs) -> requests.Response:
		"""
		Returns a collection of folders
		:keyword parent: str, optional - The child folders for the specified parent folder to return; folders are returned only if they match this value exactly
		:keyword start: int, optional - The index of the first folder to return
		:keyword limit: int, optional - The maximum number of folders to return
		:return: Returns a collection of folders based on the options for pagination, filtering, and sorting. The items in the collection use the application/vnd.sas.marketing.folder.summary media type.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
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
			api_path = "/folders{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_folder(self, payload: dict, **kwargs) -> requests.Response:
		"""
		Create a new folder
		:param payload: required - The representation of a folder
		:keyword parent: str, optional - The unique identifier for the parent folder under which the current sub-folder is created. If the parent parameter is not provided then the folderPath attribute from folder representation is used to set the parent for current sub-folder
		:return: Creates a new folder based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "parent" in kwargs:
				query_string.join("parent={0}&".format(kwargs["parent"]))
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/vnd.sas.marketing.folder+json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/folders{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_folder(self, folder_id: str) -> requests.Response:
		"""
		Get a folder
		:param folder_id: required - The unique identifier for the folder
		:return: Returns the representation of the specified folder.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if folder_id is None:
			raise Exception("Folder ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/vnd.sas.marketing.folder+json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/folders/{0}".format(folder_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_folder_headers(self, folder_id: str) -> requests.Response:
		"""
		Get the headers for a folder
		:param folder_id: required - The unique identifier for the folder
		:return: Returns the HTTP headers for a folder. The method can also be used to determine whether a folder exists.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if folder_id is None:
			raise Exception("Folder ID is missing.")
		try:
			action = "HEAD"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/folders/{0}".format(folder_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_folder(self, folder_id: str, payload: dict) -> requests.Response:
		"""
		Update a folder
		:param folder_id: required - The unique identifier for the folder
		:param payload: required - The representation of a folder
		:return: Updates the specified folder based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if folder_id is None:
			raise Exception("Folder ID is missing.")
		try:
			action = "PUT"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/folders/{0}".format(folder_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_folder(self, folder_id: str) -> requests.Response:
		"""
		Delete a folder
		:param folder_id: required - The unique identifier for the folder
		:return: Deletes the specified folder.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if folder_id is None:
			raise Exception("Folder ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/folders/{0}".format(folder_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def patch_folder(self, folder_id: str, payload: dict) -> requests.Response:
		"""
		Update a folder
		:param folder_id: required - The unique identifier for the folder
		:param payload: required - The representation of a patch operation for folder
		:return: Updates the specified folder based on the representation in the request body.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if folder_id is None:
			raise Exception("Folder ID is missing.")
		try:
			action = "PATCH"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/folders/{0}".format(folder_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Folders()
