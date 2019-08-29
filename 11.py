'''
29 08 2019
This problem was asked by Twitter.

Implement an autocomplete system. 
That is, given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isLeafNode = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, string):
        temp = self.root
        for character in string:
            index = ord(character) - ord('a')
            if temp.children[index] is None:
                temp.children[index]=TrieNode()
            temp=temp.children[index]
        temp.isLeafNode = True

    def search(self, string):
        temp = self.root
        for character in string:
            index = ord(character) - ord('a')
            if temp.children[index] is None:
                return False
            else:
                temp=temp.children[index]
        return temp and temp.isLeafNode
    
    def getAllStringsWithPrefix(self, string):
        ans=[]
        temp = self.root
        for character in string:
            index = ord(character) - ord('a')
            if temp.children[index] is None:
                return []
            else:
                temp=temp.children[index]
        for ind in range(26):
            if temp.children[ind] is not None:
                done = True
                ret=self.getString(temp.children[ind], string+str(chr(ind+ord('a'))))
                if ret is not []:
                    ans+=ret
        return ans
    
    def getString(self, temp, string):
        ans=[]
        if temp.isLeafNode:
            ans.append(string)
        for ind in range(26):
            if temp.children[ind] is not None:
                ans+=self.getString(temp.children[ind], string+str(chr(ind+ord('a'))))
        return ans

def main():
    t = int(input("Enter testcases : "))
    while t > 0:
        string = input("Enter string : ") 
        listOfStrings = [i for i in input("Enter list of strings : ").split()]
        trie = Trie()
        for i in listOfStrings:
            trie.add(i)
        # for i in listOfStrings:
        #     print(trie.search(i))
        print(trie.getAllStringsWithPrefix(string))
        t-=1

if __name__=="__main__":
    main()
