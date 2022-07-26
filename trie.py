class TrieNode:
    def __init__(self, char):
        # set char in node
        self.char = char
        # set list of child nodes
        self.children = []
        # check if end of word
        self.is_finished = False
        # count for the num of matching char in a given word
        self.counter = 1
    
    def add(self, root, word):
        # create node pointer to point to root
        node = root

        # loop thru the word and extract the letters
        for char in word:
            # set a found flag 
            found = False
            # loop thru the children of the root word if similar word already exists
            for child in node.children:
                # check if the child char matches the char of the word we're adding
                if child.char == char:
                    # increment the count of the letter since they match
                    child.counter += 1
                    # move the node pointer to the child 
                    node = child
                    # set the found flag to true
                    found = True
                    break
            # if we didn't find any matching characters, create a new node with the char and add to the children list
            if not found:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
        # mark node as finished 
        node.is_finished = True
    
    def find_prefix(self, root, prefix):
        # check if there is a prefix
        if not prefix:
            return False, 0
        # create a node pointer
        node = root
        # loop thru char of prefix
        for char in prefix:
            # create a flag to check if we found the letter or not
            char_not_found = True
            # loop thru each of the child 
            for child in node.children:
                # if we found a matching letter we mark the flag to false and point to child
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
            # if we didn't find any matching characters, return False
            if char_not_found:
                return False, 0
        # return True and the count of the matching char
        return True, node.counter
    
    def remove(self, root, word):
        return self.remove_word(word, 0, root)
    
    def remove_word(self, word, i, node):

        # check if index is len of the word
        if i == len(word):
            # if the word is finished return false
            if not node.is_finished:
                return False
            # mark the finished word as false
            node.is_finished = False
            return len(node.children) == 0
        
        # get the first char of the word
        char = word[i]

        for n in node.children:
            print(n.char)
        
        # if char not in our trie, return False
        if char not in node.children:
            return False

        # point to next char in our trie
        next_node = node.children[char]
        # recursive call to next index with new pointer to next char
        should_delete = self.remove_word(word, i+1, next_node)
        # if we reached the end of the word, delete the child char
        if should_delete:
            del node.children[char]
            return len(node.children) == 0
        
        # otherwise return False
        return False

        


if __name__ == "__main__":
    root = TrieNode('*')
    root.add(root, "hackathon")
    root.add(root, 'hack')
    root.add(root, "apple")
    root.remove(root, "apple")

    print(root.find_prefix(root, 'apple'))
    # print(root.find_prefix(root, 'hac'))
    # print(root.find_prefix(root, 'hack'))
    # print(root.find_prefix(root, 'hackathon'))
    # print(root.find_prefix(root, 'ha'))
    # print(root.find_prefix(root, 'hammer'))

    
                    

