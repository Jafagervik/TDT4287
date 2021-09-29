#include <iostream>
#include <string.h>
#include <string_view>
#include <algorithm>
#include <utility>

enum class NodeType
{
    ROOT = 0,
    INTERNAL = 1,
    LEAF = 2
};

struct Node
{
    std::pair<unsigned int, unsigned int> label;
    NodeType type;
    Node(unsigned int from, unsigned int to, NodeType type) : first{from}, to { to }
};