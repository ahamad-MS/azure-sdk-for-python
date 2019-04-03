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

from .resource import Resource


class BatchAccount(Resource):
    """Contains information about an Azure Batch account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar location: The location of the resource.
    :vartype location: str
    :ivar tags: The tags of the resource.
    :vartype tags: dict[str, str]
    :ivar account_endpoint: The account endpoint used to interact with the
     Batch service.
    :vartype account_endpoint: str
    :ivar provisioning_state: The provisioned state of the resource. Possible
     values include: 'Invalid', 'Creating', 'Deleting', 'Succeeded', 'Failed',
     'Cancelled'
    :vartype provisioning_state: str or
     ~azure.mgmt.batch.models.ProvisioningState
    :ivar pool_allocation_mode: The allocation mode to use for creating pools
     in the Batch account. Possible values include: 'BatchService',
     'UserSubscription'
    :vartype pool_allocation_mode: str or
     ~azure.mgmt.batch.models.PoolAllocationMode
    :ivar key_vault_reference: A reference to the Azure key vault associated
     with the Batch account.
    :vartype key_vault_reference: ~azure.mgmt.batch.models.KeyVaultReference
    :ivar auto_storage: The properties and status of any auto-storage account
     associated with the Batch account.
    :vartype auto_storage: ~azure.mgmt.batch.models.AutoStorageProperties
    :ivar dedicated_core_quota: The dedicated core quota for the Batch
     account. For accounts with PoolAllocationMode set to UserSubscription,
     quota is managed on the subscription so this value is null.
    :vartype dedicated_core_quota: int
    :ivar low_priority_core_quota: The low-priority core quota for the Batch
     account. For accounts with PoolAllocationMode set to UserSubscription,
     quota is managed on the subscription so this value is null.
    :vartype low_priority_core_quota: int
    :ivar dedicated_core_quota_per_vm_family: A list of the dedicated core
     quota per Virtual Machine family for the Batch account. For accounts with
     PoolAllocationMode set to UserSubscription, quota is managed on the
     subscription so this value is null.
    :vartype dedicated_core_quota_per_vm_family:
     list[~azure.mgmt.batch.models.VirtualMachineFamilyCoreQuota]
    :ivar dedicated_core_quota_per_vm_family_enforced: A value indicating
     whether the core quota for the Batch Account is enforced per Virtual
     Machine family or not. Batch is transitioning its core quota system for
     dedicated cores to be enforced per Virtual Machine family. During this
     transitional phase, the dedicated core quota per Virtual Machine family
     may not yet be enforced. If this flag is false, dedicated core quota is
     enforced via the old dedicatedCoreQuota property on the account and does
     not consider Virtual Machine family. If this flag is true, dedicated core
     quota is enforced via the dedicatedCoreQuotaPerVMFamily property on the
     account, and the old dedicatedCoreQuota does not apply.
    :vartype dedicated_core_quota_per_vm_family_enforced: bool
    :ivar pool_quota: The pool quota for the Batch account.
    :vartype pool_quota: int
    :ivar active_job_and_job_schedule_quota: The active job and job schedule
     quota for the Batch account.
    :vartype active_job_and_job_schedule_quota: int
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'tags': {'readonly': True},
        'account_endpoint': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'pool_allocation_mode': {'readonly': True},
        'key_vault_reference': {'readonly': True},
        'auto_storage': {'readonly': True},
        'dedicated_core_quota': {'readonly': True},
        'low_priority_core_quota': {'readonly': True},
        'dedicated_core_quota_per_vm_family': {'readonly': True},
        'dedicated_core_quota_per_vm_family_enforced': {'readonly': True},
        'pool_quota': {'readonly': True},
        'active_job_and_job_schedule_quota': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'account_endpoint': {'key': 'properties.accountEndpoint', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'pool_allocation_mode': {'key': 'properties.poolAllocationMode', 'type': 'PoolAllocationMode'},
        'key_vault_reference': {'key': 'properties.keyVaultReference', 'type': 'KeyVaultReference'},
        'auto_storage': {'key': 'properties.autoStorage', 'type': 'AutoStorageProperties'},
        'dedicated_core_quota': {'key': 'properties.dedicatedCoreQuota', 'type': 'int'},
        'low_priority_core_quota': {'key': 'properties.lowPriorityCoreQuota', 'type': 'int'},
        'dedicated_core_quota_per_vm_family': {'key': 'properties.dedicatedCoreQuotaPerVMFamily', 'type': '[VirtualMachineFamilyCoreQuota]'},
        'dedicated_core_quota_per_vm_family_enforced': {'key': 'properties.dedicatedCoreQuotaPerVMFamilyEnforced', 'type': 'bool'},
        'pool_quota': {'key': 'properties.poolQuota', 'type': 'int'},
        'active_job_and_job_schedule_quota': {'key': 'properties.activeJobAndJobScheduleQuota', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(BatchAccount, self).__init__(**kwargs)
        self.account_endpoint = None
        self.provisioning_state = None
        self.pool_allocation_mode = None
        self.key_vault_reference = None
        self.auto_storage = None
        self.dedicated_core_quota = None
        self.low_priority_core_quota = None
        self.dedicated_core_quota_per_vm_family = None
        self.dedicated_core_quota_per_vm_family_enforced = None
        self.pool_quota = None
        self.active_job_and_job_schedule_quota = None
