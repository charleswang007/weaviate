import weaviate
import os

with weaviate.connect_to_wcs(
    cluster_url=os.getenv("WCS_CLUSTER_URL"),  # Replace with your WCS URL
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCS_API_KEY"))  # Replace with your WCS key
) as client:  # Use this context manager to ensure the connection is closed
    print("connection established")
    print("schema:", client.collections.list_all())