# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.filter_type_response import FilterTypeResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.response_error import ResponseError


class TypeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(TypeApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, filter_id, **kwargs):
        """Get Filter Type"""

        return self.api_client.get(
            '/encoding/filters/{filter_id}/type',
            path_params={'filter_id': filter_id},
            type=FilterTypeResponse,
            **kwargs
        )
