# coding: utf-8
import pprint
import six
from datetime import datetime
from enum import Enum


class Link(object):
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
            'href': 'str',
            'title': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'href': 'href',
            'title': 'title'
        }
        return attributes

    def __init__(self, href=None, title=None, *args, **kwargs):

        self._href = None
        self._title = None
        self.discriminator = None

        self.href = href
        if title is not None:
            self.title = title

    @property
    def href(self):
        """Gets the href of this Link.

        webpage target URL

        :return: The href of this Link.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Link.

        webpage target URL

        :param href: The href of this Link.
        :type: str
        """

        if href is not None:
            if not isinstance(href, str):
                raise TypeError("Invalid type for `href`, type has to be `str`")

            self._href = href


    @property
    def title(self):
        """Gets the title of this Link.

        Short description of the linked page

        :return: The title of this Link.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Link.

        Short description of the linked page

        :param title: The title of this Link.
        :type: str
        """

        if title is not None:
            if not isinstance(title, str):
                raise TypeError("Invalid type for `title`, type has to be `str`")

            self._title = title

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
            if issubclass(Link, dict):
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
        if not isinstance(other, Link):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
