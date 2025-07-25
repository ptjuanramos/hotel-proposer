from typing import Any, Optional

import os, io
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseUpload

SCOPES = ['https://www.googleapis.com/auth/drive']

class GoogleDrive:

    def __build_service(self) -> Resource:
        creds = self.__authenticate_google_drive()
        return build('drive', 'v3', credentials=creds)

    def __authenticate_google_drive(self) -> Any:
        # creds = None
        #
        # if os.path.exists('token.json'):
        #     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        #
        # if not creds or not creds.valid:
        #     if creds and creds.expired and creds.refresh_token:
        #         creds.refresh(Request())
        #     else:
        #         flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        #         creds = flow.run_local_server(port=0)
        #     with open('token.json', 'w') as token:
        #         token.write(creds.to_json())
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        return creds

    def create_folder_if_not_exists(self, folder_name: str) -> Optional[str]:
        """
        Creates a folder in Google Drive if it doesn't already exist.
        Returns the folder ID.
        """
        try:
            service = self.__build_service()
            query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
            results = service.files().list(q=query, spaces="drive", fields="files(id, name)").execute()
            items = results.get("files", [])

            if items:
                print(f"Folder '{folder_name}' already exists. ID: {items[0]['id']}")
                return items[0]["id"]
            else:
                # Create the folder
                file_metadata = {
                    "name": folder_name,
                    "mimeType": "application/vnd.google-apps.folder",
                }
                folder = service.files().create(body=file_metadata, fields="id").execute()
                print(f"Folder '{folder_name}' created. ID: {folder.get('id')}")
                return folder.get("id")
        except HttpError as error:
            print(f"An error occurred while checking/creating folder: {error}")
            return None

    def create_folder(self, folder_name):
        service = self.__build_service()

        # Metadata for the folder
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }

        # Create the folder
        folder = service.files().create(body=folder_metadata, fields='id').execute()
        print(f"Folder '{folder_name}' created with ID: {folder.get('id')}")

    def create_google_doc_in_folder(self, folder_id: str, doc_name: str, content: Optional[str] = None) -> Optional[str]:
        """
        Creates a Google Doc in the specified folder with optional content.
        Returns the document ID.
        """
        try:
            file_metadata = {
                "name": doc_name,
                "mimeType": "application/vnd.google-apps.document",
                "parents": [folder_id],
            }

            media = None
            if content:
                content_bytes = content.encode("utf-8")
                media = MediaIoBaseUpload(io.BytesIO(content_bytes), mimetype="text/plain", resumable=True)

            service = self.__build_service()
            doc = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
            print(f"Google Doc '{doc_name}' created in folder. ID: {doc.get('id')}")
            return doc.get("id")
        except HttpError as error:
            print(f"An error occurred while creating Google Doc: {error}")
            return None