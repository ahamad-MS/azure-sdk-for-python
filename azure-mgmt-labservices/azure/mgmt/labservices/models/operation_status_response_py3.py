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


class OperationStatusResponse(Model):
    """Status Details of the long running operation for an environment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar status: status of the long running operation for an environment
    :vartype status: str
    """

    _validation = {
        'status': {'readonly': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(OperationStatusResponse, self).__init__(**kwargs)
        self.status = None
