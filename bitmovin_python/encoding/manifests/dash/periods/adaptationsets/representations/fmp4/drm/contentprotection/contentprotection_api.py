# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.content_protection import ContentProtection
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError
from bitmovin_python.encoding.manifests.dash.periods.adaptationsets.representations.fmp4.drm.contentprotection.content_protections_list_query_params import ContentProtectionsListQueryParams


class ContentprotectionApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ContentprotectionApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, adaptationset_id, representation_id, content_protection=None, **kwargs):
        """Add Content Protection to DRM fMP4 Representation"""

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/fmp4/drm/{representation_id}/contentprotection',
            content_protection,
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=ContentProtection,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, representation_id, contentprotection_id, **kwargs):
        """Delete DRM fMP4 Representation Content Protection"""

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/fmp4/drm/{representation_id}/contentprotection/{contentprotection_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id, 'contentprotection_id': contentprotection_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, representation_id, contentprotection_id, **kwargs):
        """DRM fMP4 Representation Content Protection Details"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/fmp4/drm/{representation_id}/contentprotection/{contentprotection_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id, 'contentprotection_id': contentprotection_id},
            type=ContentProtection,
            **kwargs
        )

    def list(self, manifest_id, period_id, adaptationset_id, representation_id, query_params: ContentProtectionsListQueryParams = None, **kwargs):
        """List all DRM fMP4 Representation Content Protections"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/fmp4/drm/{representation_id}/contentprotection',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            query_params=query_params,
            pagination_response=True,
            type=ContentProtection,
            **kwargs
        )
