from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def uploadImage(image, key):    
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=reunionimages;AccountKey=hygEs2p3/CyF1FNjXp9QuVYz0jOY9LsprjC+9KEw4S4MDnR5Cz5sSJFOkHoOAyaobdgtOUnSthnS+ASt9Z8pYQ==;EndpointSuffix=core.windows.net'
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    container_name = "images"
    blob_name = f"{key}-{image.filename}"

    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    blob_client.upload_blob(image.stream, overwrite=True)

    image_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}"
    return image_url