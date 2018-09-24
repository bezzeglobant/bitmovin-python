from .drm_service import DRMService
from .widevine_drm_service import WidevineDRM
from .playready_drm_service import PlayReadyDRM
from .marlin_drm_service import MarlinDRM
from .clearkey_drm_service import ClearKeyDRM
from .cenc_drm_service import CENCDRM


class MP4DRMService(DRMService):

    MUXING_TYPE_URL = 'mp4'

    def __init__(self, http_client):
        super().__init__(http_client=http_client)
        self.Widevine = WidevineDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
        self.PlayReady = PlayReadyDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
        self.Marlin = MarlinDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
        self.ClearKey = ClearKeyDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
        self.CENC = CENCDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
