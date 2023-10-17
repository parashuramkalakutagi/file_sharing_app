from rest_framework import serializers
from .models import *
import shutil


class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(max_length=1000000, allow_empty_file=False, use_url=False)
    )
    folder = serializers.CharField(required=False)

    def Zip_files(self,folder):
        shutil.make_archive(f'media/{folder}','zip',f'media/{folder}')
    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')

        files_objs = [
            Files(folder=folder, file=file) for file in files
        ]

        # Using bulk_create for optimized database insertion
        Files.objects.bulk_create(files_objs)

        return {'files': {}, 'folder': str(folder.uid)}