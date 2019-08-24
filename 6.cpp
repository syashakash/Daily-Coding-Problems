/*
* This problem was asked by Google.
*
* An XOR linked list is a more memory efficient doubly linked list. 
* Instead of each node holding next and prev fields, it holds a field named both, 
* which is an XOR of the next node and the previous node. 
* Implement an XOR linked list; it has an add(element) which adds the element to the end, 
* and a get(index) which returns the node at index.
*
* If using a language that has no pointers (such as Python), 
* you can assume you have access to get_pointer and dereference_pointer 
* functions that converts between nodes and memory addresses.
*/
#include<bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode* xorPrevNext;
    ListNode(int val): val(val), xorPrevNext(NULL) {}
};

ListNode* XOR(ListNode* A, ListNode* B)
{
    return (ListNode*)((uintptr_t)(A) ^ (uintptr_t)(B));
}

void insert(ListNode** head, int val)
{
    //cout<<"called insert"<<endl;
    ListNode *newNode=new ListNode(val);
    newNode->xorPrevNext=XOR(*head, NULL);
    if(*head != NULL) {
        ListNode *next=XOR((*head)->xorPrevNext, NULL);
        (*head)->xorPrevNext=XOR(newNode,next);
    }
    *head=newNode;
    //cout<<"changed head " <<(*head)->val << " " <<endl;
}

void printList(ListNode* head)
{
    ListNode *curr = head;  
    ListNode *prev = NULL;  
    ListNode *next;  
  
    cout << "Following are the nodes of Linked List: \n";  
  
    while (curr != NULL)  
    {   
        cout<<curr->val<<" ";   
        next = XOR (prev, curr->xorPrevNext);    
        prev = curr;  
        curr = next;
    }
    cout<<endl;
}

int main()
{
    int t;
    scanf("%d",&t);
    while(t--) {
        ListNode* head=NULL;
        int n;
        scanf("%d",&n);
        while(n--) {
            int x;
            scanf("%d",&x);
            insert(&head,x);
        }
        //cout<<"here"<<endl;
        printList(head);
    }
    return 0;
}