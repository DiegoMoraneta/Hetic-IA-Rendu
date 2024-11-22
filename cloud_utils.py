import boto3
import os

def get_pdfs_from_s3(bucket_name, prefix=""):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    
    pdf_files = []
    for obj in response.get('Contents', []):
        file_key = obj['Key']
        local_file_path = f"downloads/{file_key.split('/')[-1]}"
        os.makedirs("downloads", exist_ok=True)  # Crée un dossier local pour stocker les fichiers
        s3.download_file(bucket_name, file_key, local_file_path)
        pdf_files.append(local_file_path)
    return pdf_files
