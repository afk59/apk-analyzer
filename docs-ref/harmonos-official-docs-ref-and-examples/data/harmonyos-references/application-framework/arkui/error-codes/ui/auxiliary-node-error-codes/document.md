# Auxiliary Node Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/6IugdFQgSzuBnZtlCTkNmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37B5132A67FD49197F1730E48E50556B6E45463CD2731E1627AC069EE2992E7D)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 106206 The Node Has Been Accepted as an Auxiliary Node

**Error Message**

The node has already been adopted.

**Description**

This error code is reported when the node has been accepted as an auxiliary node and cannot be mounted as a child node.

Adoption: establishes a parent-child-like relationship where the parent node provides lifecycle callbacks to the child without actually adding it as a regular child node. The adopted node does not receive events from the parent or respond to events like normal child nodes.

**Possible Causes**

The node has been accepted as an auxiliary node and cannot be mounted as a child node.

**Solution**

Cancel the acceptance of the node and then mount it as a child node.

#### 106207 The Auxiliary Node to Accept Has a Parent Node

**Error Message**

This node already has a parent node.

**Description**

This error code is reported when the node already has a parent node and cannot be accepted by other nodes.

Adoption: establishes a parent-child-like relationship where the parent node provides lifecycle callbacks to the child without actually adding it as a regular child node. The adopted node does not receive events from the parent or respond to events like normal child nodes.

**Possible Causes**

The node already has a parent node and cannot be accepted by other nodes.

**Solution**

Remove the node from its parent node and then accept the node.

#### 106208 The Node Cannot Be Accepted as an Auxiliary Node

**Error Message**

The node cannot be adopted.

**Description**

This error code is reported when the node cannot be accepted as an auxiliary node.

Adoption: establishes a parent-child-like relationship where the parent node provides lifecycle callbacks to the child without actually adding it as a regular child node. The adopted node does not receive events from the parent or respond to events like normal child nodes.

**Possible Causes**

1.  The node is a null pointer.
2.  The node does not meet the criteria for adopting other nodes. Only the following types of nodes can adopt other nodes:
    -   Imperative node on the TS side.
    -   Imperative node on the CAPI side.
    -   Root node of BuilderNode.

**Solution**

Pass a node that meets the criteria for adoption.

#### 106209 The Node Cannot Accept Other Nodes

**Error Message**

The node cannot adopt children.

**Description**

This error code is reported when the node cannot accept other auxiliary nodes.

Adoption: establishes a parent-child-like relationship where the parent node provides lifecycle callbacks to the child without actually adding it as a regular child node. The adopted node does not receive events from the parent or respond to events like normal child nodes.

**Possible Causes**

1.  The node is a null pointer.
2.  The node does not meet the criteria for adopting other nodes. Only the following types of nodes can adopt other nodes:
    -   Imperative node on the TS side.
    -   Imperative node on the CAPI side.

**Solution**

Use a node that meets the criteria for adoption.

#### 106210 The Node Is Not an Affiliated Node Accepted by the Target Node

**Error Message**

This child is not adopted by the parent node.

**Description**

This error code is reported when the child node is not accepted by the target parent node.

Adoption: establishes a parent-child-like relationship where the parent node provides lifecycle callbacks to the child without actually adding it as a regular child node. The adopted node does not receive events from the parent or respond to events like normal child nodes.

**Possible Causes**

1.  The child node has not been accepted by any parent node.
2.  The child node has been accepted, but the accepting parent node is not the current target node.

**Solution**

If the node is not accepted as an affiliated node by the target node, there is no need to perform the removal operation for this node.
