# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.drm import Drm
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.encodings.muxings.fmp4.drm.widevine.widevine_api import WidevineApi
from bitmovin_python.encoding.encodings.muxings.fmp4.drm.playready.playready_api import PlayreadyApi
from bitmovin_python.encoding.encodings.muxings.fmp4.drm.primetime.primetime_api import PrimetimeApi
from bitmovin_python.encoding.encodings.muxings.fmp4.drm.fairplay.fairplay_api import FairplayApi
from bitmovin_python.encoding.encodings.muxings.fmp4.drm.marlin.marlin_api import MarlinApi
from bitmovin_python.encoding.encodings.muxings.fmp4.drm.clearkey.clearkey_api import ClearkeyApi
from bitmovin_python.encoding.encodings.muxings.fmp4.drm.cenc.cenc_api import CencApi


class DrmApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DrmApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.widevine = WidevineApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.playready = PlayreadyApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.primetime = PrimetimeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.fairplay = FairplayApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.marlin = MarlinApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.clearkey = ClearkeyApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.cenc = CencApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, muxing_id, **kwargs):
        """List all DRMs of FMP4 Muxing"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            pagination_response=True,
            type=Drm,
            **kwargs
        )
