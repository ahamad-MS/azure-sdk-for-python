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

from msrest.serialization import Model


class PurchaseRequestPropertiesAdvancedProperties(Model):
    """PurchaseRequestPropertiesAdvancedProperties.

    :param instance_flexibility: Possible values include: 'true', 'false'
    :type instance_flexibility: str or
     ~azure.mgmt.reservations.models.InstanceFlexibility
    """

    _attribute_map = {
        'instance_flexibility': {'key': 'instanceFlexibility', 'type': 'str'},
    }

    def __init__(self, *, instance_flexibility=None, **kwargs) -> None:
        super(PurchaseRequestPropertiesAdvancedProperties, self).__init__(**kwargs)
        self.instance_flexibility = instance_flexibility
