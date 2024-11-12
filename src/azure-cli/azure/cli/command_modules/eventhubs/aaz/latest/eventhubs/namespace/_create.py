# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "eventhubs namespace create",
)
class Create(AAZCommand):
    """Create a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent.

    :example: Creates a new namespace.
        az eventhubs namespace create --resource-group myresourcegroup --name mynamespace --location westus --tags tag1=value1 tag2=value2 --sku Standard --enable-auto-inflate

    :example: Creates a new namespace with Identity & Encryption Enabled
        az eventhubs namespace create --resource-group myresourcegroup --name mynamespace --location westus --sku Premium --mi-user-assigned /subscriptions/{subscriptionId}/resourceGroups/{resourcegroup}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MSIName --encryption-config key-name=key1 key-vault-uri=https://mykeyvault.vault.azure.net/ user-assigned-identity=/subscriptions/{subscriptionId}}/resourceGroups/{resourcegroup}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MSIName --encryption-config key-name=key1 key-vault-uri=https://mykeyvault.vault.azure.net/ user-assigned-identity=/subscriptions/{subscriptionId}}/resourceGroups/{resourcegroup}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MSIName
    """

    _aaz_info = {
        "version": "2024-05-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.eventhub/namespaces/{}", "2024-05-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.namespace_name = AAZStrArg(
            options=["-n", "--name", "--namespace-name"],
            help="The Namespace name",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z][a-zA-Z0-9-]{6,50}[a-zA-Z0-9]$",
                max_length=50,
                min_length=6,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="Parameters",
            help="Properties of BYOK Identity description",
        )
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Parameters",
            help="Resource location.",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.sku = AAZObjectArg(
            options=["--sku"],
            arg_group="Parameters",
            help="Properties of sku resource",
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags.",
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="Type of managed service identity.",
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned, UserAssigned": "SystemAssigned, UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
            help="Properties for User Assigned Identities",
        )

        user_assigned_identities = cls._args_schema.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            blank={},
        )

        sku = cls._args_schema.sku
        sku.capacity = AAZIntArg(
            options=["capacity"],
            help="The Event Hubs throughput units for Basic or Standard tiers, where value should be 0 to 20 throughput units. The Event Hubs premium units for Premium tier, where value should be 0 to 10 premium units.",
            fmt=AAZIntArgFormat(
                minimum=0,
            ),
        )
        sku.name = AAZStrArg(
            options=["name"],
            help="Name of this SKU.",
            required=True,
            enum={"Basic": "Basic", "Premium": "Premium", "Standard": "Standard"},
        )
        sku.tier = AAZStrArg(
            options=["tier"],
            help="The billing tier of this particular SKU.",
            enum={"Basic": "Basic", "Premium": "Premium", "Standard": "Standard"},
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.alternate_name = AAZStrArg(
            options=["--alternate-name"],
            arg_group="Properties",
            help="Alternate name specified when alias and namespace names are same.",
        )
        _args_schema.cluster_arm_id = AAZStrArg(
            options=["--cluster-arm-id"],
            arg_group="Properties",
            help="Cluster ARM ID of the Namespace.",
        )
        _args_schema.disable_local_auth = AAZBoolArg(
            options=["--disable-local-auth"],
            arg_group="Properties",
            help="This property disables SAS authentication for the Event Hubs namespace.",
        )
        _args_schema.encryption = AAZObjectArg(
            options=["--encryption"],
            arg_group="Properties",
            help="Properties of BYOK Encryption description",
        )
        _args_schema.geo_data_replication = AAZObjectArg(
            options=["--geo-data-replication"],
            arg_group="Properties",
            help="Geo Data Replication settings for the namespace",
        )
        _args_schema.enable_auto_inflate = AAZBoolArg(
            options=["--enable-auto-inflate"],
            arg_group="Properties",
            help="Value that indicates whether AutoInflate is enabled for eventhub namespace.",
        )
        _args_schema.kafka_enabled = AAZBoolArg(
            options=["--kafka-enabled"],
            arg_group="Properties",
            help="Value that indicates whether Kafka is enabled for eventhub namespace.",
        )
        _args_schema.maximum_throughput_units = AAZIntArg(
            options=["--maximum-throughput-units"],
            arg_group="Properties",
            help="Upper limit of throughput units when AutoInflate is enabled, value should be within 0 to 20 throughput units. ( '0' if AutoInflateEnabled = true)",
            fmt=AAZIntArgFormat(
                minimum=0,
            ),
        )
        _args_schema.minimum_tls_version = AAZStrArg(
            options=["--minimum-tls-version"],
            arg_group="Properties",
            help="The minimum TLS version for the cluster to support, e.g. '1.2'",
            enum={"1.0": "1.0", "1.1": "1.1", "1.2": "1.2"},
        )
        _args_schema.private_endpoint_connections = AAZListArg(
            options=["--endpoint-connections", "--private-endpoint-connections"],
            arg_group="Properties",
            help="List of private endpoint connections.",
        )
        _args_schema.public_network_access = AAZStrArg(
            options=["--public-network-access"],
            arg_group="Properties",
            help="This determines if traffic is allowed over public network. By default it is enabled.",
            default="Enabled",
            enum={"Disabled": "Disabled", "Enabled": "Enabled", "SecuredByPerimeter": "SecuredByPerimeter"},
        )
        _args_schema.zone_redundant = AAZBoolArg(
            options=["--zone-redundant"],
            arg_group="Properties",
            help="Enabling this property creates a Standard Event Hubs Namespace in regions supported availability zones.",
        )

        encryption = cls._args_schema.encryption
        encryption.key_source = AAZStrArg(
            options=["key-source"],
            help="Enumerates the possible value of keySource for Encryption",
            default="Microsoft.KeyVault",
            enum={"Microsoft.KeyVault": "Microsoft.KeyVault"},
        )
        encryption.key_vault_properties = AAZListArg(
            options=["key-vault-properties"],
            help="Properties of KeyVault",
        )
        encryption.require_infrastructure_encryption = AAZBoolArg(
            options=["require-infrastructure-encryption"],
            help="Enable Infrastructure Encryption (Double Encryption)",
        )

        key_vault_properties = cls._args_schema.encryption.key_vault_properties
        key_vault_properties.Element = AAZObjectArg()

        _element = cls._args_schema.encryption.key_vault_properties.Element
        _element.user_assigned_identity = AAZStrArg(
            options=["user-assigned-identity"],
            help="ARM ID of user Identity selected for encryption",
        )
        _element.key_name = AAZStrArg(
            options=["key-name"],
            help="Name of the Key from KeyVault",
        )
        _element.key_vault_uri = AAZStrArg(
            options=["key-vault-uri"],
            help="Uri of KeyVault",
        )
        _element.key_version = AAZStrArg(
            options=["key-version"],
            help="Key Version",
        )

        geo_data_replication = cls._args_schema.geo_data_replication
        geo_data_replication.locations = AAZListArg(
            options=["locations"],
            help="A list of regions where replicas of the namespace are maintained.",
        )
        geo_data_replication.max_replication_lag_duration_in_seconds = AAZIntArg(
            options=["max-lag", "max-replication-lag-duration-in-seconds"],
            help="The maximum acceptable lag for data replication operations from the primary replica to a quorum of secondary replicas.  When the lag exceeds the configured amount, operations on the primary replica will be failed.",
        )

        locations = cls._args_schema.geo_data_replication.locations
        locations.Element = AAZObjectArg()

        _element = cls._args_schema.geo_data_replication.locations.Element
        _element.cluster_arm_id = AAZStrArg(
            options=["cluster-arm-id"],
            help="Optional property that denotes the ARM ID of the Cluster. This is required, if a namespace replica should be placed in a Dedicated Event Hub Cluster",
        )
        _element.location_name = AAZStrArg(
            options=["location-name"],
            help="Azure regions where a replica of the namespace is maintained",
        )
        _element.role_type = AAZStrArg(
            options=["role-type"],
            help="GeoDR Role Types",
            enum={"Primary": "Primary", "Secondary": "Secondary"},
        )

        private_endpoint_connections = cls._args_schema.private_endpoint_connections
        private_endpoint_connections.Element = AAZObjectArg()

        _element = cls._args_schema.private_endpoint_connections.Element
        _element.private_endpoint = AAZObjectArg(
            options=["private-endpoint"],
            help="The Private Endpoint resource for this Connection.",
        )
        _element.private_link_service_connection_state = AAZObjectArg(
            options=["private-link-service-connection-state"],
            help="Details about the state of the connection.",
        )
        _element.provisioning_state = AAZStrArg(
            options=["provisioning-state"],
            help="Provisioning state of the Private Endpoint Connection.",
            enum={"Canceled": "Canceled", "Creating": "Creating", "Deleting": "Deleting", "Failed": "Failed", "Succeeded": "Succeeded", "Updating": "Updating"},
        )

        private_endpoint = cls._args_schema.private_endpoint_connections.Element.private_endpoint
        private_endpoint.id = AAZStrArg(
            options=["id"],
            help="The ARM identifier for Private Endpoint.",
        )

        private_link_service_connection_state = cls._args_schema.private_endpoint_connections.Element.private_link_service_connection_state
        private_link_service_connection_state.description = AAZStrArg(
            options=["description"],
            help="Description of the connection state.",
        )
        private_link_service_connection_state.status = AAZStrArg(
            options=["status"],
            help="Status of the connection.",
            enum={"Approved": "Approved", "Disconnected": "Disconnected", "Pending": "Pending", "Rejected": "Rejected"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.NamespacesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NamespacesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "namespaceName", self.ctx.args.namespace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-05-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("identity", AAZObjectType, ".identity")
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("sku", AAZObjectType, ".sku")
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type")
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("alternateName", AAZStrType, ".alternate_name")
                properties.set_prop("clusterArmId", AAZStrType, ".cluster_arm_id")
                properties.set_prop("disableLocalAuth", AAZBoolType, ".disable_local_auth")
                properties.set_prop("encryption", AAZObjectType, ".encryption")
                properties.set_prop("geoDataReplication", AAZObjectType, ".geo_data_replication")
                properties.set_prop("isAutoInflateEnabled", AAZBoolType, ".enable_auto_inflate")
                properties.set_prop("kafkaEnabled", AAZBoolType, ".kafka_enabled")
                properties.set_prop("maximumThroughputUnits", AAZIntType, ".maximum_throughput_units")
                properties.set_prop("minimumTlsVersion", AAZStrType, ".minimum_tls_version")
                properties.set_prop("privateEndpointConnections", AAZListType, ".private_endpoint_connections")
                properties.set_prop("publicNetworkAccess", AAZStrType, ".public_network_access")
                properties.set_prop("zoneRedundant", AAZBoolType, ".zone_redundant")

            encryption = _builder.get(".properties.encryption")
            if encryption is not None:
                encryption.set_prop("keySource", AAZStrType, ".key_source")
                encryption.set_prop("keyVaultProperties", AAZListType, ".key_vault_properties")
                encryption.set_prop("requireInfrastructureEncryption", AAZBoolType, ".require_infrastructure_encryption")

            key_vault_properties = _builder.get(".properties.encryption.keyVaultProperties")
            if key_vault_properties is not None:
                key_vault_properties.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.encryption.keyVaultProperties[]")
            if _elements is not None:
                _elements.set_prop("identity", AAZObjectType)
                _elements.set_prop("keyName", AAZStrType, ".key_name")
                _elements.set_prop("keyVaultUri", AAZStrType, ".key_vault_uri")
                _elements.set_prop("keyVersion", AAZStrType, ".key_version")

            identity = _builder.get(".properties.encryption.keyVaultProperties[].identity")
            if identity is not None:
                identity.set_prop("userAssignedIdentity", AAZStrType, ".user_assigned_identity")

            geo_data_replication = _builder.get(".properties.geoDataReplication")
            if geo_data_replication is not None:
                geo_data_replication.set_prop("locations", AAZListType, ".locations")
                geo_data_replication.set_prop("maxReplicationLagDurationInSeconds", AAZIntType, ".max_replication_lag_duration_in_seconds")

            locations = _builder.get(".properties.geoDataReplication.locations")
            if locations is not None:
                locations.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.geoDataReplication.locations[]")
            if _elements is not None:
                _elements.set_prop("clusterArmId", AAZStrType, ".cluster_arm_id")
                _elements.set_prop("locationName", AAZStrType, ".location_name")
                _elements.set_prop("roleType", AAZStrType, ".role_type")

            private_endpoint_connections = _builder.get(".properties.privateEndpointConnections")
            if private_endpoint_connections is not None:
                private_endpoint_connections.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.privateEndpointConnections[]")
            if _elements is not None:
                _elements.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties.privateEndpointConnections[].properties")
            if properties is not None:
                properties.set_prop("privateEndpoint", AAZObjectType, ".private_endpoint")
                properties.set_prop("privateLinkServiceConnectionState", AAZObjectType, ".private_link_service_connection_state")
                properties.set_prop("provisioningState", AAZStrType, ".provisioning_state")

            private_endpoint = _builder.get(".properties.privateEndpointConnections[].properties.privateEndpoint")
            if private_endpoint is not None:
                private_endpoint.set_prop("id", AAZStrType, ".id")

            private_link_service_connection_state = _builder.get(".properties.privateEndpointConnections[].properties.privateLinkServiceConnectionState")
            if private_link_service_connection_state is not None:
                private_link_service_connection_state.set_prop("description", AAZStrType, ".description")
                private_link_service_connection_state.set_prop("status", AAZStrType, ".status")

            sku = _builder.get(".sku")
            if sku is not None:
                sku.set_prop("capacity", AAZIntType, ".capacity")
                sku.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                sku.set_prop("tier", AAZStrType, ".tier")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.identity = AAZObjectType()
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.sku = AAZObjectType()
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _CreateHelper._build_schema_system_data_read(_schema_on_200_201.system_data)
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200_201.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200_201.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200_201.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.alternate_name = AAZStrType(
                serialized_name="alternateName",
            )
            properties.cluster_arm_id = AAZStrType(
                serialized_name="clusterArmId",
            )
            properties.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            properties.disable_local_auth = AAZBoolType(
                serialized_name="disableLocalAuth",
            )
            properties.encryption = AAZObjectType()
            properties.geo_data_replication = AAZObjectType(
                serialized_name="geoDataReplication",
            )
            properties.is_auto_inflate_enabled = AAZBoolType(
                serialized_name="isAutoInflateEnabled",
            )
            properties.kafka_enabled = AAZBoolType(
                serialized_name="kafkaEnabled",
            )
            properties.maximum_throughput_units = AAZIntType(
                serialized_name="maximumThroughputUnits",
            )
            properties.metric_id = AAZStrType(
                serialized_name="metricId",
                flags={"read_only": True},
            )
            properties.minimum_tls_version = AAZStrType(
                serialized_name="minimumTlsVersion",
            )
            properties.private_endpoint_connections = AAZListType(
                serialized_name="privateEndpointConnections",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_network_access = AAZStrType(
                serialized_name="publicNetworkAccess",
            )
            properties.service_bus_endpoint = AAZStrType(
                serialized_name="serviceBusEndpoint",
                flags={"read_only": True},
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.updated_at = AAZStrType(
                serialized_name="updatedAt",
                flags={"read_only": True},
            )
            properties.zone_redundant = AAZBoolType(
                serialized_name="zoneRedundant",
            )

            encryption = cls._schema_on_200_201.properties.encryption
            encryption.key_source = AAZStrType(
                serialized_name="keySource",
            )
            encryption.key_vault_properties = AAZListType(
                serialized_name="keyVaultProperties",
            )
            encryption.require_infrastructure_encryption = AAZBoolType(
                serialized_name="requireInfrastructureEncryption",
            )

            key_vault_properties = cls._schema_on_200_201.properties.encryption.key_vault_properties
            key_vault_properties.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.encryption.key_vault_properties.Element
            _element.identity = AAZObjectType()
            _element.key_name = AAZStrType(
                serialized_name="keyName",
            )
            _element.key_vault_uri = AAZStrType(
                serialized_name="keyVaultUri",
            )
            _element.key_version = AAZStrType(
                serialized_name="keyVersion",
            )

            identity = cls._schema_on_200_201.properties.encryption.key_vault_properties.Element.identity
            identity.user_assigned_identity = AAZStrType(
                serialized_name="userAssignedIdentity",
            )

            geo_data_replication = cls._schema_on_200_201.properties.geo_data_replication
            geo_data_replication.locations = AAZListType()
            geo_data_replication.max_replication_lag_duration_in_seconds = AAZIntType(
                serialized_name="maxReplicationLagDurationInSeconds",
            )

            locations = cls._schema_on_200_201.properties.geo_data_replication.locations
            locations.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.geo_data_replication.locations.Element
            _element.cluster_arm_id = AAZStrType(
                serialized_name="clusterArmId",
            )
            _element.location_name = AAZStrType(
                serialized_name="locationName",
            )
            _element.replica_state = AAZStrType(
                serialized_name="replicaState",
                flags={"read_only": True},
            )
            _element.role_type = AAZStrType(
                serialized_name="roleType",
            )

            private_endpoint_connections = cls._schema_on_200_201.properties.private_endpoint_connections
            private_endpoint_connections.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.private_endpoint_connections.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _CreateHelper._build_schema_system_data_read(_element.system_data)
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties.private_endpoint_connections.Element.properties
            properties.private_endpoint = AAZObjectType(
                serialized_name="privateEndpoint",
            )
            properties.private_link_service_connection_state = AAZObjectType(
                serialized_name="privateLinkServiceConnectionState",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )

            private_endpoint = cls._schema_on_200_201.properties.private_endpoint_connections.Element.properties.private_endpoint
            private_endpoint.id = AAZStrType()

            private_link_service_connection_state = cls._schema_on_200_201.properties.private_endpoint_connections.Element.properties.private_link_service_connection_state
            private_link_service_connection_state.description = AAZStrType()
            private_link_service_connection_state.status = AAZStrType()

            sku = cls._schema_on_200_201.sku
            sku.capacity = AAZIntType()
            sku.name = AAZStrType(
                flags={"required": True},
            )
            sku.tier = AAZStrType()

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    _schema_system_data_read = None

    @classmethod
    def _build_schema_system_data_read(cls, _schema):
        if cls._schema_system_data_read is not None:
            _schema.created_at = cls._schema_system_data_read.created_at
            _schema.created_by = cls._schema_system_data_read.created_by
            _schema.created_by_type = cls._schema_system_data_read.created_by_type
            _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
            _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
            _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type
            return

        cls._schema_system_data_read = _schema_system_data_read = AAZObjectType(
            flags={"read_only": True}
        )

        system_data_read = _schema_system_data_read
        system_data_read.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data_read.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data_read.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data_read.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data_read.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data_read.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.created_at = cls._schema_system_data_read.created_at
        _schema.created_by = cls._schema_system_data_read.created_by
        _schema.created_by_type = cls._schema_system_data_read.created_by_type
        _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
        _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
        _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type


__all__ = ["Create"]
