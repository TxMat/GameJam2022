class Node():
    def __init__(self,
                 id: int,
                 perk_name: str = "",
                 parents: set = set()):
        self.id = id
        self.perk = perk_name
        self.parents = parents
        self.children = set()

    def add_child(self, node):
        self.children.add(node)

    def del_child(self, node):
        self.children.remove(node)

    def node_info(self):
        print("perk: " + self.perk)
        print("id: " + str(self.id))
        print("nb_parents: " + str(len(self.parents)))
        if (self.children == set()):
            print("leaf reached")
        else:
            print("nb_children: " + str(len(self.children)))
        print("")

    def display_child(self):
        self.node_info()
        if (self.children != set()):
            for child in self.children:
                child.display_child()


class SkillTree():
    # Actually not an n-ary tree, but a graph
    def __init__(self, cock_name, root, nodes):
        self.cock_name = ""
        self.root = root
        self.nodes = nodes
        # transition_cost: {(parent_node_id, children_node_id): ("material",cost)}
        self.cost_per_transition = {}

    def scramble(self, ritual_name):
        pass

    def debug_transitions(self):
        self.cost_per_transition[(1, 2)] = ('grain 1', 10)
        self.cost_per_transition[(1, 3)] = ('grain 2', 20)
        self.cost_per_transition[(1, 4)] = ('grain 3', 30)
        self.cost_per_transition[(2, 5)] = ('grain 4', 40)
        self.cost_per_transition[(2, 6)] = ('grain 5', 50)
        self.cost_per_transition[(3, 7)] = ('grain 6', 60)
        self.cost_per_transition[(4, 12)] = ('grain 7', 70)
        self.cost_per_transition[(5, 8)] = ('grain 8', 80)
        self.cost_per_transition[(6, 9)] = ('grain 9', 90)
        self.cost_per_transition[(6, 10)] = ('grain 10', 100)
        self.cost_per_transition[(7, 10)] = ('grain 11', 110)
        self.cost_per_transition[(7, 11)] = ('grain 12', 120)
        self.cost_per_transition[(12, 13)] = ('grain 13', 130)
        self.cost_per_transition[(12, 14)] = ('grain 14', 140)

    def display_transitions(self):
        trans_list = self.cost_per_transition
        for trans in trans_list:
            print("transition " + str(trans[0]) + "-" + str(trans[1]) + " requires " + str(
                trans_list[trans][1]) + " " + str(trans_list[trans][0]))

    def display_tree(self):
        self.root.display_child()


def debug_tree():
    a = Node(1, "perk 1")
    b = Node(2, "perk 2", {a})
    c = Node(3, "perk 3", {a})
    d = Node(4, "perk 4", {a})
    e = Node(5, "perk 5", {b})
    f = Node(6, "perk 6", {b})
    g = Node(7, "perk 7", {c})
    h = Node(8, "perk 8", {e})
    i = Node(9, "perk 9", {f})
    j = Node(10, "perk 10", {f, g})
    k = Node(11, "perk 11", {g})
    l = Node(12, "perk 12", {d})
    m = Node(13, "perk 13", {l})
    n = Node(14, "perk 14", {l})
    a.add_child(b)
    a.add_child(c)
    a.add_child(d)
    b.add_child(e)
    b.add_child(f)
    c.add_child(g)
    e.add_child(h)
    g.add_child(j)
    f.add_child(i)
    f.add_child(j)
    g.add_child(k)
    d.add_child(l)
    l.add_child(m)
    l.add_child(n)
    tree = SkillTree("poulet test", a, (b, c, d, e, f, g, h, i, j, k, l, m, n))
    return tree


def debug_test():
    tree = debug_tree()
    tree.display_tree()
    tree.debug_transitions()
    tree.display_transitions()
