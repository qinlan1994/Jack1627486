# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 23:49:31 2019

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

def obtainAllElems(head):
    node = head
    elems = []
    while node:
        elems.append(node.elem)
        node = node.next
    return elems

#两两交换链表中的节点
def func(head):
    dumb = ListNode(None)
    dumb.next = head
    node = dumb
    while node.next and node.next.next:
        p  = node.next
        q = p.next
        p.next = q.next
        q.next = p
        node.next = q
        node = p
    return dumb.next

if __name__ == '__main__':
    L = SingleLinkList()
    n = int(input('链表长度? n = '))
    for i in range(n):
        L.append(np.random.randint(0,10))
    print('\n初始链表:',obtainAllElems(L.head))
    dumb = func(L.head)
    print('\n处理结果:',obtainAllElems(dumb))
















