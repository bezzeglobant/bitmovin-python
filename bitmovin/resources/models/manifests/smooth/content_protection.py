from bitmovin.resources.models import AbstractModel


class SmoothContentProtection(AbstractModel):

    def __init__(self, encoding_id, muxing_id, drm_id, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.encodingId = encoding_id
        self.muxingId = muxing_id
        self.drmId = drm_id

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        custom_data = json_object.get('customData')
        encoding_id = json_object.get('encodingId')
        muxing_id = json_object.get('muxingId')
        drm_id = json_object.get('drmId')
        content_protection = SmoothContentProtection(id_=id_,
                                                     custom_data=custom_data,
                                                     encoding_id=encoding_id,
                                                     muxing_id=muxing_id,
                                                     drm_id=drm_id)
        return content_protection
