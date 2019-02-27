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


class ImageTemplateLastRunStatus(Model):
    """ImageTemplateLastRunStatus.

    :param start_time: Start time of the last run (UTC)
    :type start_time: datetime
    :param end_time: End time of the last run (UTC)
    :type end_time: datetime
    :param run_state: State of the last run. Possible values include: 'ready',
     'running', 'succeeded', 'partiallySucceeded', 'failed'
    :type run_state: str or ~azure.mgmt.imagebuilder.models.enum
    :param run_sub_state: Sub state of the last run. Possible values include:
     'queued', 'building', 'customizing', 'distributing'
    :type run_sub_state: str or ~azure.mgmt.imagebuilder.models.enum
    :param message: Verbose information about the last run state
    :type message: str
    """

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'run_state': {'key': 'runState', 'type': 'str'},
        'run_sub_state': {'key': 'runSubState', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, start_time=None, end_time=None, run_state=None, run_sub_state=None, message: str=None, **kwargs) -> None:
        super(ImageTemplateLastRunStatus, self).__init__(**kwargs)
        self.start_time = start_time
        self.end_time = end_time
        self.run_state = run_state
        self.run_sub_state = run_sub_state
        self.message = message
