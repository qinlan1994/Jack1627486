# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:15:58 2019

@author: Bob
"""
import numpy as np

class ListNode(object):
    def __init__(self,elem,link=None):
        self.elem = elem
        self.next = link

class SingleLinkList(object):
    def __init__(self):
        self.head = None
    
    def prepend(self,elem):
        self.head = ListNode(elem,self.head)
    def append(self,elem):
        if self.head == None:
            self.head = ListNode(elem)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = ListNode(elem)
    def targetInsert(self,i,e):
        n = self.obtainListLen()
        if i == 0:self.prepend(e)
        elif i == n:self.append(e)
        else:
            node = self.head
            while node and i > 1:
                node = node.next
                i -= 1
            p = ListNode(e)
            p.next = node.next
            node.next = p

#输出环形链表的首结点
def func(head):
    if head == None or head.next == None:
        return None
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast == None or fast.next == None:
        return None
    else:
        tmp = head
        while tmp != slow:
            tmp = tmp.next
            slow = slow.next
        return tmp
        
if __name__ == '__main__':
    L = SingleLinkList()
    for i in range(8):
        L.append(np.random.randint(0,10))
    print('初始链表:',obtainAllElems(L.head))
    node = L.head
    while node.next:
        node = node.next
    node.next = L.head.next.next
    dumb = func(L.head)
    node,elems = dumb,[]
    while True:
        elems.append(node.elem)
        node = node.next
        if node == dumb:break
    print('环形链表:',elems)               
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
