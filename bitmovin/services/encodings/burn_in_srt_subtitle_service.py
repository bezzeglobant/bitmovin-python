from bitmovin.errors import MissingArgumentError
from bitmovin.resources.models import BurnInSrtSubtitle as BurnInSrtSubtitleResource
from bitmovin.services.rest_service import RestService


class BurnInSrtSubtitleService(RestService):
    BASE_ENDPOINT_URL = 'encoding/encodings/{encoding_id}/streams/{stream_id}/burn-in-subtitles/srt'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=BurnInSrtSubtitleResource)

    def _get_endpoint_url(self, encoding_id, stream_id):
        if not encoding_id:
            raise MissingArgumentError('encoding_id must be given')
        if not stream_id:
            raise MissingArgumentError('stream_id must be given')

        endpoint_url = self.BASE_ENDPOINT_URL\
            .replace('{encoding_id}', encoding_id)\
            .replace('{stream_id}', stream_id)

        return endpoint_url

    def create(self, object_, encoding_id, stream_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id, stream_id=stream_id)
        return super().create(object_)

    def delete(self, encoding_id, stream_id, burn_in_subtitle_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id, stream_id=stream_id)
        return super().delete(id_=burn_in_subtitle_id)

    def retrieve(self, encoding_id, stream_id, burn_in_subtitle_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id, stream_id=stream_id)
        return super().retrieve(id_=burn_in_subtitle_id)

    def list(self, encoding_id, stream_id, offset=None, limit=None):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id, stream_id=stream_id)
        return super().list(offset, limit)

    def retrieve_custom_data(self, encoding_id, stream_id, burn_in_subtitle_id):
        self.relative_url = self._get_endpoint_url(encoding_id=encoding_id, stream_id=stream_id)
        return super().retrieve_custom_data(id_=burn_in_subtitle_id)
