"""
Handshaking Lemma and Interesting Tree Properties

What is Handshaking Lemma?

Handshaking lemma is about undirected graph. In every finite undirected graph, an
even number of vertices will always have odd degree. The handshaking lemma is a 
consequence of the degree sum formula (also sometimes called the handshaking lemma)

Sum base(vev) deg(v) =2 | E |

How is Handshaking Lemma useful in Tree Data Structure?

:- Following are  some interesting facts that can be proved using Handshaking lemma.
1) In a k-ary tree where every node has either 0 or k children, following property is 
always true.

L = (k - 1) * I + 1
Where L = Number of leaf nodes
      I = Number of internal nodes

Proof:

can be divided in two cases.

case 1: (Root is Leaf): There is only one node in tree. The above formula is true for
a single node as L = 1, I = 0

Case 2: (Root is Internal Node): For trees with more than 1 node, the root is always
an internal node. The above formula can be proved using Handshaking Lemmma for this
case. A tree is an undirected acyclic graph.

Total number of edges in Tree is  number of nodes minus 1, i.e. |E| = L+I-1

All internal nodes except root in the given type of tree have degree k+1. Root has
a degree k. All leaves have degree 1. Applying the Handshaking lemma to such trees,
we get the following relation.

sum of all degrees = 2 * (sum of edges)

sum of degrees of leaves +

sum of degrees for Internal Node except root +

Root's degree = 2 * (No. of nodes - 1)

putting values of above terms, 

L + (I-1) * (k+1) + k = 2 * (L + I -1)
L + k *I - k + I -1 + k = 2*L + 2I - 2
L + k*I+I - 1 = 2 * L + 2 * I - 2
K *I + 1 - I = L
(K-1) * I + 1 = L


So the above property is proved using Handhsking Lemma.


Aternate Proof: (Without using Handshaking Theorem)

Since there are I internal nodes, each having K children, therefore total children 
in the tree = K * I.

There are I - 1 internal nodes which are children of some other node (root has been
excluded hence one less than the total number of internal nodes)

That is, out of these K * I children, I-1 are internal nodes and therefore the rest
(K*I - (I-1)) are leaves.

Hence L = (K-1) * I+ 1.

2) In Binary tree, a number of leaf nodes is always one more than nodes with two
children

L = T + 1

WHERE   L = Number of leaf nodes
        T = Number of internal nodew with two children

proof:

Let a number of nodes with 2 children T. Proof can be divided in three cases.

Case 1: There is only one node, the relationship holds as T = 0, L = 1.

Case 2: Root has two children, i.e., degree of root is 2

Sum of degrees of nodes with two children except root + 
Sum of degrees of nodes with one child +
Sum of degrees of leaves + Root's degree = 2 * (No. of Nodes - 1)

Putting values of above terms, 
(T-1) * 3 + S * 2 + L + 2 = (S + T + L -1) * 2

Cancelling 2S from both sides
(T -1) * 3 + L + 2 = (T + L -1) * 2
T - 1 = L -2
T = L -1

Case 3: Root has one child, i.e., degree of  root is 1.

Sum of degrees of nodes with two children +

Sum of degrees of nodes with one child except root +

SUm of degrees of leaves + Root's degree = 2 * (No. of Nodes  - 1)

Putting values of above terms,

T * 3 + (S-1) * 2 + L+ 1 = (S + T + L - 1) * 2

Cancelling 2S from both sides.
3*T + L -1 = 2 *T + 2*L -2
T -L = L - 2
T = L -1


Therefore, in all three cases, we get T = L -1.



"""

