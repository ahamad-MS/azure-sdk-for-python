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

from .sub_resource_py3 import SubResource


class RunOutput(SubResource):
    """Represents an output that was created by running an image template.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :param name: Required. Resource name
    :type name: str
    :ivar type: Resource type
    :vartype type: str
    :param artifact_id: The resource id of the artifact.
    :type artifact_id: str
    :ivar provisioning_state: Provisioning state of the resource. Possible
     values include: 'Creating', 'Succeeded', 'Failed', 'Deleting'
    :vartype provisioning_state: str or ~azure.mgmt.imagebuilder.models.enum
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'required': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'artifact_id': {'key': 'properties.artifactId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, name: str, artifact_id: str=None, **kwargs) -> None:
        super(RunOutput, self).__init__(name=name, **kwargs)
        self.artifact_id = artifact_id
        self.provisioning_state = None
