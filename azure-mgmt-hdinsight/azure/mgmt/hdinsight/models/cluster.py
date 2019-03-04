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

from .tracked_resource import TrackedResource


class Cluster(TrackedResource):
    """The HDInsight cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The Azure Region where the resource lives
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param etag: The ETag for the resource
    :type etag: str
    :param properties: The properties of the cluster.
    :type properties: ~azure.mgmt.hdinsight.models.ClusterGetProperties
    :param identity: The identity of the cluster, if configured.
    :type identity: ~azure.mgmt.hdinsight.models.ClusterIdentity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ClusterGetProperties'},
        'identity': {'key': 'identity', 'type': 'ClusterIdentity'},
    }

    def __init__(self, **kwargs):
        super(Cluster, self).__init__(**kwargs)
        self.etag = kwargs.get('etag', None)
        self.properties = kwargs.get('properties', None)
        self.identity = kwargs.get('identity', None)
