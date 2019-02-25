# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class KubernetesClusterPatch(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            'connected': 'bool'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'connected': 'connected'
        }
        return attributes

    def __init__(self, connected=None, *args, **kwargs):

        self._connected = None
        self.discriminator = None

        self.connected = connected

    @property
    def connected(self):
        """Gets the connected of this KubernetesClusterPatch.

        Shows if the Kubernetes cluster is accessible by the Bitmovin Agent

        :return: The connected of this KubernetesClusterPatch.
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this KubernetesClusterPatch.

        Shows if the Kubernetes cluster is accessible by the Bitmovin Agent

        :param connected: The connected of this KubernetesClusterPatch.
        :type: bool
        """

        if connected is not None:
            if not isinstance(connected, bool):
                raise TypeError("Invalid type for `connected`, type has to be `bool`")

            self._connected = connected

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(KubernetesClusterPatch, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KubernetesClusterPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
