# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .image_template_source import ImageTemplateSource


class ImageTemplateIsoSource(ImageTemplateSource):
    """Describes an image source that is an installation ISO. Currently only
    supports Red Hat Enterprise Linux 7.2-7.5 ISO's.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param source_uri: Required. URL to get the ISO image. This URL has to be
     accessible to the resource provider at the time of the imageTemplate
     creation.
    :type source_uri: str
    :param sha256_checksum: Required. SHA256 Checksum of the ISO image.
    :type sha256_checksum: str
    """

    _validation = {
        'type': {'required': True},
        'source_uri': {'required': True},
        'sha256_checksum': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'source_uri': {'key': 'sourceURI', 'type': 'str'},
        'sha256_checksum': {'key': 'sha256Checksum', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageTemplateIsoSource, self).__init__(**kwargs)
        self.source_uri = kwargs.get('source_uri', None)
        self.sha256_checksum = kwargs.get('sha256_checksum', None)
        self.type = 'ISO'
